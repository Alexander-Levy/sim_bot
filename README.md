# Simulated Robots Package 
Minimal simulation for mobile robots using ROS2 and Gazebo(Classic and New). This package provides all of the necesarry files to get a simulated robot up and running. This includes the urdf, parameters and launch files for a robot capable of sensing its enviroment, mapping and localization, as well as autonamous and tele-operated navigation. There are two robots available: a 2-wheeled and a 4-wheeled differential drive robot. Currently four sensors are implemented: camera, depth camera, and 2D & 3D lidars. The package has been tested to work humble and foxy, it will be upgraded to work with jazzy in the near future. 

### Work in progress
The package is still being worked on and early in development

## Supported on
Currently supported:
Ubuntu Version | ROS 2 version | Gazebo
-- | -- | -- 
[Ubuntu 20.04 LTS](https://releases.ubuntu.com/focal/) | [ROS2 Foxy](https://docs.ros.org/en/foxy/Installation.html) | Gazebo Classic 
[Ubuntu 22.04 LTS](https://releases.ubuntu.com/jammy/)| [ROS2 Humble](https://docs.ros.org/en/rolling/Releases/Release-Humble-Hawksbill.html) | Gazebo Classic & Gazebo

Support for [Ubuntu 24.04](https://releases.ubuntu.com/noble/) & [ROS2 Jazzy](https://docs.ros.org/en/jazzy/Installation.html) is planned.


### Note
ROS Iron could work with the humble branches but this has not been tested.

## Branches
ROS 2 version | Gazebo version | Branch 
-- | -- | -- 
Foxy | Gazebo Classic | [foxy](https://github.com/Alexander-Levy/sim_bot/tree/foxy) 
Humble | Gazebo Classic | [humble](https://github.com/Alexander-Levy/sim_bot/tree/humble) 
Humble | Fortress | [humble-new-gazebo](https://github.com/Alexander-Levy/sim_bot/tree/humble-new-gazebo) 

## Usage
![alt text](https://github.com/Alexander-Levy/sim_bot/blob/humble-new-gazebo/media/new_gazebo_sim.png "Gazebo Simulation")

![alt text](https://github.com/Alexander-Levy/sim_bot/blob/humble-new-gazebo/media/simulation_sample.png "ROS Visualizer")


### Two Wheeled Differential Drive Robot
The 2-wheeled differential drive robot simulation can be run with the following command:
```bash
ros2 launch sim_bot diff_bot.launch.py 
```

### Four Wheeled Differential Drive Robot  
The 4-wheeled differential drive robot simulation can be run with the following command:
```bash
ros2 launch sim_bot four_wheel.launch.py 
```

### Ackermann Robot needs to be ported

### Controlling the robot
By default the simulation will launch a tele_op_joy node that will listen for a controller(xbox, ps4, etc) input. If that is not a suitable option, the robot can also be controlled with the keyboard using this command:
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard 
```

### Launch configurations
The simulation launch files offer serveral launch configurations to modify its behaviour. All of the launch configurations available are listed below:
```bash
Config      Options         Default     Description
world:=     <path_to_world> test.world  Relative path to test world                       
headless:=  True/False      False       Toggle the Gazebo graphical interface (visualized if False) 
rviz:=      True/False      True        Activates rviz is launch with pre-made view
slam:=      True/False      True        Activates localization and mapping 
nav:=       True/False      True        Activates the navigation stack  
octomap:=   True/False      True        Activates the octomap server  
```

These configurations are the same no matter the robot type. Example launch command with custom arguments:
```bash 
ros2 launch sim_bot diff_bot.launch.py rviz:=False slam:=False nav:=False
```


## Dependencies
This package is designed to require minimal set-up for robot simulation, the dependencies are as follows. xacro is used for urdf flexibility, gazebo is the simulator being used, twist-mux is used so that the robot can listen to multiple topics for velocity commands, slam-toolbox is used for localization and mapping, navigation2 is the navigation stack of the robot, and octomap lets us create a 3D representation of the enviroment.
```bash
sudo apt install -y            \
    ros-humble-xacro           \
    ros-humble-twist-mux       \
    ros-humble-navigation2     \
    ros-humble-slam-toolbox    \
    ros-humble-octomap*        \
    ros-humble-ros-gz          \ 
```


## Install
To use this package please download all of the necesary dependencies first and then follow these steps
```bash
mkdir -p sim_ws/src
cd sim_ws/src
git clone https://github.com/Alexander-Levy/sim_bot.git -b humble-new-gazebo
cd ..
colcon build --symlink-install
```
Launch the simulation to test the package
```bash
source ./install/setup.bash
ros2 launch sim_bot diff_bot.launch.py 
```


## TODO 
Package is still being worked on, however the core funtionality is pretty much done, will be adding some things over the next couple of days.
 - [ ] add ackerman 
 - [ ] update readme 
