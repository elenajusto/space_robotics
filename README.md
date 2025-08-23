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
[particle_filter_localisation-7] Particle  12 : x= -2.7957243332753183 , y= -0.5077539012945484 , theta= 1.
...
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

## Task 3: Human operator input 
Terminal Excerpt:

```sh
[particle_filter_localisation-7] [Elena Debug - Task 3] Clicked point: x= 0.09914769232273102 , y= -0.06611382961273193
[particle_filter_localisation-7] [Elena Debug - Task 3] Gaussian distribution x:  [-5.09867834e-01  9.02796069e-01  2.63467833e-01  2.95065820e-01
[particle_filter_localisation-7]   5.78218709e-01 -4.42019298e-02 -9.52497833e-02  6.06999578e-01
[particle_filter_localisation-7]  -1.21465437e-01  1.84021223e-01  5.52911660e-02 -5.78845246e-02
[particle_filter_localisation-7]  -1.61159995e-02  3.49745869e-01  7.17731730e-01 -2.10488887e-01
[particle_filter_localisation-7]  -1.61072053e-01 -5.24838987e-01  4.24582148e-02  6.12590127e-01
[particle_filter_localisation-7]   1.70969354e-01  7.45892772e-01  8.72119170e-02 -1.61508174e-01
...
[particle_filter_localisation-7] [Elena Debug - Task 3] Gaussian distribution y:  [ 9.45681005e-01  3.84445033e-01  2.75103392e-01 -6.32081241e-01
[particle_filter_localisation-7]   9.88949713e-03 -1.03622964e-01 -6.15597175e-02 -3.80433167e-01
[particle_filter_localisation-7]  -2.47823927e-01  2.55818433e-01 -8.52828870e-02  1.71494127e-01
[particle_filter_localisation-7]   6.46844001e-02 -7.13638277e-01  3.29524910e-01  7.73588746e-02
[particle_filter_localisation-7]   2.01153801e-01  1.51252839e+00  3.85202144e-01 -1.14708714e+00
[particle_filter_localisation-7]   9.01577390e-01  4.99722533e-01 -4.11747233e-01 -5.19619601e-01
...
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  0 : x= -0.509867834443009 , y= 0.9456810053854128
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  1 : x= 0.9027960692153134 , y= 0.3844450333245517
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  2 : x= 0.26346783329216295 , y= 0.27510339224212155
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  3 : x= 0.29506582022172967 , y= -0.6320812414438572
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  4 : x= 0.5782187086998152 , y= 0.009889497131505526
...

```
Image:

![task_3](https://github.com/elenajusto/space_robotics/blob/main/images/task_3.png)

## Task 4: Motion Update
Terminal Excerpt:
```sh
[particle_filter_localisation-7] [Elena Debug - Task 4] Particle before motion update: x= 0.7499340822098212 , y= -0.30889787688876885 , theta= 1.0897263394868855 , weight= 0.0023310023310023154
[particle_filter_localisation-7] [Elena Debug - Task 4] Particle after motion update: x= 0.7587930546888315 , y= -0.27699274059996193 , theta= 1.1722191521637617 , weight= 0.0023310023310023154
[particle_filter_localisation-7] [Elena Debug - Task 4] Particle before motion update: x= -2.1653050288915976 , y= -0.8470391674637086 , theta= 3.1901042844964 , weight= 0.0023310023310023154
[particle_filter_localisation-7] [Elena Debug - Task 4] Particle after motion update: x= -2.191210293692166 , y= -0.8492060471734064 , theta= 3.1525013347594357 , weight= 0.0023310023310023154
```

Gif:

![task_4](https://github.com/elenajusto/space_robotics/blob/main/images/task_4_gif.gif)

## Task 5: Terrain Observation Update
Termainl excerpt not showing.

Gif:

![task_5](https://github.com/elenajusto/space_robotics/blob/main/images/task_5_gif.gif)


## Task 6: Pose estimate
Terminal excerpt:
```sh
...
[particle_filter_localisation-7] [Elena Debug - Task 1] Particle  497 : x= -4.850524473696125 , y= 4.914847139549949 , theta= 4.87659693515706 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug - Task 1] Particle  498 : x= 3.29678205553689 , y= -3.3984503722849966 , theta= 3.889552256853763 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug - Task 1] Particle  499 : x= 4.109906565107123 , y= 2.8822890474988787 , theta= 2.1479091142543005 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug - Task 6] estimated_pose_x =  -0.6202051730498539
[particle_filter_localisation-7] [Elena Debug - Task 6] estimated_pose_y =  1.62349180702847
[particle_filter_localisation-7] [Elena Debug - Task 6] estimated_pose_theta =  -1.3484048785351084
```

Gif:
![task_6](https://github.com/elenajusto/space_robotics/blob/main/images/task_6.gif)

# python_tutorial
Diagram to help conceptulise what is happening regarding coordinates.

![coordinates](https://github.com/elenajusto/space_robotics/blob/main/images/coordinates.png)