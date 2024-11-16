import os
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.conditions import IfCondition
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, GroupAction


def generate_launch_description():

    # Package name
    package_name='sim_bot' 

    # Launch configurations
    world = LaunchConfiguration('world')
    headless = LaunchConfiguration('headless')
    rviz = LaunchConfiguration('rviz')
    slam = LaunchConfiguration('slam')
        
    # Path to default world 
    world_path = os.path.join(get_package_share_directory(package_name),'worlds', 'test.world')

    # Launch Arguments
    declare_world = DeclareLaunchArgument(
        name='world', default_value=world_path,
        description='Full path to the world model file to load')
    
    declare_headless = DeclareLaunchArgument(
        'headless', default_value='False',
        description='Decides if the simulation is visualized')
    
    declare_rviz = DeclareLaunchArgument(
        name='rviz', default_value='True',
        description='Opens rviz is set to True')
    
    declare_slam = DeclareLaunchArgument(
        name='slam', default_value='True',
        description='Activates simultaneous localization and mapping')
     
    # Launch Robot State Publisher
    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )
    
    # Launch Joystick Tele Operation
    joystick = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','teleop.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Launch the gazebo server to initialize the simulation
    #gazebo_params_file = os.path.join(get_package_share_directory(package_name),'config','gazebo_params.yaml')
    gazebo_server = IncludeLaunchDescription(
                    PythonLaunchDescriptionSource([os.path.join(
                        get_package_share_directory('gazebo_ros'), 'launch', 'gzserver.launch.py'
                    )]), launch_arguments={'world': world}.items()
    )

    # Launch the gazebo client to visualize the simulation only if headless is declared as False
    gazebo_client = GroupAction(
        condition=IfCondition(PythonExpression(['not ', headless])),
        actions=[IncludeLaunchDescription(
                    PythonLaunchDescriptionSource([os.path.join(
                        get_package_share_directory('gazebo_ros'), 'launch', 'gzclient.launch.py')]))]
    )

    # Run the spawner node from the gazebo_ros package. 
    spawn_diff_bot = Node(
                        package='gazebo_ros', 
                        executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'diff_bot'],
                        output='screen'
    )
    
    # Launch Rviz with diff bot rviz file
    rviz_config_file = os.path.join(get_package_share_directory(package_name), 'rviz', 'diff_bot.rviz')
    rviz2 = GroupAction(
        condition=IfCondition(rviz),
        actions=[Node(
                    package='rviz2',
                    executable='rviz2',
                    arguments=['-d', rviz_config_file],
                    output='screen',
                    remappings=[('/map', 'map'),
                                ('/tf', 'tf'),
                                ('/tf_static', 'tf_static'),
                                ('/goal_pose', 'goal_pose'),
                                ('/clicked_point', 'clicked_point'),
                                ('/initialpose', 'initialpose')])]
    )

    # Launch Simultaneous Localization and Mapping
    slam_node = GroupAction(
        condition=IfCondition(slam),
        actions=[IncludeLaunchDescription(
                    PythonLaunchDescriptionSource([os.path.join(
                        get_package_share_directory(package_name),'launch','slam.launch.py'
                    )]), launch_arguments={'use_sim_time': 'true'}.items())]
    )

    # Launch them all!
    return LaunchDescription([
        # Declare launch arguments
        declare_headless,
        declare_rviz,
        declare_world,
        declare_slam,

        # Launch the nodes
        rviz2,
        rsp,
        joystick,
        gazebo_server,
        gazebo_client,
        spawn_diff_bot,
        slam_node
    ])