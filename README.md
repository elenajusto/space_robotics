# Space Robotics Repository
Repo to hold code and notes I have for the Space Robotics subject at UTS.

# Commands

## Setup ROS Environment
You have to repeat the above two commands every time you open a new terminal.
```sh
source /opt/ros/humble/setup.bash
source ~/ros_ws/install/setup.bash
```

## Assignment 1 - particle_filter_localisation
1. Execute the program:
```sh
ros2 launch particle_filter_localisation particle_filter_localisation_launch.py
```
2. To control the robot:
```sh
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

# particle_filter_localisation
This will be the directory for assignment 1.

Located in `ros_ws/src/particle_filter_localisation`

# python_tutorial
Diagram to help conceptulise what is happening regarding coordinates.

![coordinates](https://github.com/elenajusto/space_robotics/blob/main/images/coordinates.png)