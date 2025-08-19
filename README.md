# Space Robotics Repository
Repo to hold code and notes I have for the Space Robotics subject at UTS.

# Commands

## Setup ROS Environment
You have to repeat the above two commands every time you open a new terminal.
```sh
source /opt/ros/humble/setup.bash
source ~/ros_ws/install/setup.bash
```

## Building code
Build all packages/nodes in the workspace by running:
```sh
colcon build
```

You can also build an individual package at a time using (in case other packages are causing issues)

```sh
colcon build --packages-select particle_filter_localisation
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
This will be the directory for assignment 1 located in `ros_ws/src/particle_filter_localisation`

Each task requires you to insert new code within the template code file
`particle_filter_localisation/particle_filter_localisation.py`

## Task 1: Initialise the particles
Terminal Excerpt:
```
particle_filter_localisation-7] [INFO] [1755404571.603887813] [particle_filter_localisation]: Map received
[particle_filter_localisation-7] Initialising particles...
[particle_filter_localisation-7] ELENA CODE IS HERE: 
[particle_filter_localisation-7] Number of particles:  500
[particle_filter_localisation-7] Particle  0 : x= 4.802749871556899 , y= 3.8302880390734293 , theta= 0.6746124818402024 , weight= 0.002
[particle_filter_localisation-7] Particle  1 : x= -0.5229773589749893 , y= -4.7229086151963715 , theta= 1.7002927009419688 , weight= 0.002
[particle_filter_localisation-7] Particle  2 : x= -0.4664302560862774 , y= -1.6076763492630453 , theta= 3.8277917338689647 , weight= 0.002
[particle_filter_localisation-7] Particle  3 : x= -3.9102432520196118 , y= -3.253604137372422 , theta= 5.42550954922847 , weight= 0.002
[particle_filter_localisation-7] Particle  4 : x= -2.0655768112026145 , y= 1.6927649275807228 , theta= 2.729673207339105 , weight= 0.002
[particle_filter_localisation-7] Particle  5 : x= 2.264821200207198 , y= 4.277370542768261 , theta= 2.239795537470206 , weight= 0.002
[particle_filter_localisation-7] Particle  6 : x= 1.5792594994093587 , y= 0.5904668610032324 , theta= 1.5427906502797077 , weight= 0.002
[particle_filter_localisation-7] Particle  7 : x= 2.9334253809914683 , y= 3.421619791008937 , theta= 0.5052109012528094 , weight= 0.002
[particle_filter_localisation-7] Particle  8 : x= -1.186220578104575 , y= -3.344614988691592 , theta= 4.933105919283807 , weight= 0.002
[particle_filter_localisation-7] Particle  9 : x= 3.6041430833921018 , y= -4.981059427457782 , theta= 5.683933362095419 , weight= 0.002
[particle_filter_localisation-7] Particle  10 : x= -1.4921747614040384 , y= 3.3719331054620065 , theta= 5.770384222157356 , weight= 0.002
[particle_filter_localisation-7] Particle  11 : x= -0.01993272115254019 , y= 4.121128922415655 , theta= 2.338780944032725 , weight= 0.002
[particle_filter_localisation-7] Particle  12 : x= -2.7957243332753183 , y= -0.5077539012945484 , theta= 1.5735061686141982 , weight= 0.002
[particle_filter_localisation-7] Particle  13 : x= -1.172201228997387 , y= -0.11003810503811717 , theta= 2.924245753029327 , weight= 0.002
[particle_filter_localisation-7] Particle  14 : x= -4.59568163160722 , y= 4.263694171892371 , theta= 0.2832402184766078 , weight= 0.002
[particle_filter_localisation-7] Particle  15 : x= 4.924174519731246 , y= 1.919509177967277 , theta= 4.717187153455599 , weight= 0.002
[particle_filter_localisation-7] Particle  16 : x= -4.556332908235405 , y= 1.1618618737691744 , theta= 2.5770607302975974 , weight= 0.002
[particle_filter_localisation-7] Particle  17 : x= -0.34561858527917 , y= -2.0908780271970713 , theta= 5.9379163883994694 , weight= 0.002
[particle_filter_localisation-7] Particle  18 : x= 0.07599464439467507 , y= -2.5136308739855266 , theta= 5.962661037234014 , weight= 0.002
```

Image:
![task_1](https://github.com/elenajusto/space_robotics/blob/main/images/task_1.png)


## Task 2: Normalise the weights
Terminal Excerpt:
```sh
[Task 1 Items]
[particle_filter_localisation-7] [Elena Debug] Particle  495 : x= 0.7837390144723768 , y= 1.0290591824138469 , theta= 0.6731380848859895 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug] Particle  496 : x= -1.6363628222335067 , y= 0.382219434015715 , theta= 5.700813535467078 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug] Particle  497 : x= -0.17485779971350635 , y= 3.8697129706192 , theta= 3.2665586641192776 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug] Particle  498 : x= -3.657429146662379 , y= 3.110209245288929 , theta= 0.3937238382323943 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug] Particle  499 : x= -3.559582408533349 , y= 1.73400479097824 , theta= 0.6801380652133294 , weight= 0.002

[Task 2 Items]
[particle_filter_localisation-7] [Elena Debug] Normalised particle weight:  0.0019999999999999987
[particle_filter_localisation-7] [Elena Debug] Normalised particle weight:  0.0019999999999999987
[particle_filter_localisation-7] [Elena Debug] Normalised particle weight:  0.0019999999999999987
[particle_filter_localisation-7] [Elena Debug] Normalised particle weight:  0.0019999999999999987
[particle_filter_localisation-7] [Elena Debug] Normalised particle weight:  0.0019999999999999987
[particle_filter_localisation-7] [Elena Debug] Normalised particle weight:  0.0019999999999999987
[particle_filter_localisation-7] [Elena Debug] Normalised particle weight:  0.0019999999999999987
```
Image:
![task_2](https://github.com/elenajusto/space_robotics/blob/main/images/task_2.png)

# python_tutorial
Diagram to help conceptulise what is happening regarding coordinates.

![coordinates](https://github.com/elenajusto/space_robotics/blob/main/images/coordinates.png)