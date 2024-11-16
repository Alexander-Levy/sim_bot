# Simulated Robots Package 
This package will provide all of the necesarry files to get a simulated robot up and running. This includes the urdf, configuartion and launch files for a robot capable of mapping and localization as well as autonamous and tele-operated navigation. There 2 robot types available at the moment: 2-wheeled and 4-wheeled differential drive. The package is being written for humble, and has been ported to foxy, it will be upgraded to jazzy in the future. 

## Supported on
Currently supported:
 - [Ubuntu 20.04 LTS](https://releases.ubuntu.com/focal/) & [ROS2 Foxy](https://docs.ros.org/en/foxy/Installation.html),
 - [Ubuntu 22.04 LTS](https://releases.ubuntu.com/jammy/) & [ROS2 Humble](https://docs.ros.org/en/rolling/Releases/Release-Humble-Hawksbill.html)

Support for jazzy is planned.


## Usage 
### Differential Drive Robot
The differential drive robot simulation can be run with the following command:
```bash
ros2 launch sim_bot diff_bot_sim.launch.py 
```

### Four Wheel Drive Robot
The four wheel drive robot simulation can be run with the following command:
```bash
ros2 launch sim_bot four_wheel_sim.launch.py 
```

### Controlling the robot
By default a tele-op joy node will be launched that will listen for a controller(xbox, ps4, etc) input. If that is not a suitable option, the robot can also be controlled with this command:
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard 
```

### Launch configurations
The simulation launch files offer serveral launch configurations to modify its behaviour. All of the launch configurations available are listed below:
```bash
Config      Options         Default     Description
world:=     <path_to_world> test.world  Relative path to test world                       
headless:=  True/False      False       Gazebo is visualized if False
rviz:=      True/False      True        Rviz is opened if True
slam:=      True/False      True        Localization and mapping is run if True
nav:=       True/False      True        Navigation stack is launched if True
```

These configurations are the same no matter the robot type. Example launch command with custom arguments:
```bash 
ros2 launch sim_bot four_wheel_sim.launch.py rviz:=False slam:=False nav:=False
```


## Dependencies
This packages is designed to be require minimal set-up for robot simulations, so i tried to keep the dependencies to a minimum. Xacro is used for urdf flexibility, gazebo is the simulator being used, and slam-toolbox and navigation2 are a commonly used tools to give autonomy to a robot.
```bash
sudo apt install -y                     \
    ros-<ros-distro>-xacro              \
    ros-<ros-distro>-twist-mux          \
    ros-<ros-distro>-navigation2        \
    ros-<ros-distro>-slam-toolbox       \
    ros-<ros-distro>-gazebo-ros-pkgs    \
```


## Install
To use this package please download all of the necesary dependencies first and then follow these steps
```bash
mkdir -p sim_ws/src
cd sim_ws/src
git clone https://github.com/Alexander-Levy/sim_bot.git 
cd ..
colcon build --symlink-install
```
Launch the simulation to test the package
```bash
source ./install/setup.bash
ros2 launch sim_bot diff_bot_sim.launch.py 
```


## TODO 
Package is still being worked on, however the core funtionality is pretty much done, will be adding these feature over the next couple of days.
 - [ ] add ackerman-type robot support 
 - [ ] port to jazzy
 - [ ] update readme 
