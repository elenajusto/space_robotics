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
[particle_filter_localisation-7]  -2.62128761e-01 -3.37643469e-01  1.32493458e+00 -3.86939824e-01
[particle_filter_localisation-7]  -7.36578259e-01 -6.54916655e-01 -2.82164855e-01  2.28750711e-01
[particle_filter_localisation-7]  -2.96518155e-01  3.78630927e-01 -8.10049123e-01  1.23522093e-01
[particle_filter_localisation-7]  -1.52313895e-01  1.83499574e-01  1.44216287e-01 -1.21512048e+00
[particle_filter_localisation-7]  -6.77554645e-01 -3.03823939e-01 -3.96565117e-01  1.54294465e-01
[particle_filter_localisation-7]   1.36291312e-01  3.64289446e-01 -7.34279246e-01  1.49927631e-01
[particle_filter_localisation-7]   5.08494369e-01  1.29784247e-01 -3.54533128e-01  2.62990875e-01
[particle_filter_localisation-7]   6.43147457e-01  4.65307682e-01  3.80018796e-01  1.34608733e-01
[particle_filter_localisation-7]   6.00383804e-01  1.69957318e-01  4.77878851e-01 -4.42072294e-02
[particle_filter_localisation-7]  -7.00329199e-01  3.06477299e-01  3.72298718e-01 -8.32364563e-02
[particle_filter_localisation-7]   1.22308955e-01 -1.22302230e-02  5.76695527e-01  5.05402842e-01
[particle_filter_localisation-7]   6.01641852e-01  1.07195849e-01 -9.54190924e-02  2.33900019e-01
[particle_filter_localisation-7]   2.54951231e-01 -4.47388082e-01  5.23296302e-01 -1.86125732e-01
[particle_filter_localisation-7]  -4.36662809e-01 -1.05084557e+00  2.12738082e-01  8.43354242e-01
[particle_filter_localisation-7]   5.35631674e-01 -9.61568810e-02  1.78948173e-01 -2.50338603e-01
[particle_filter_localisation-7]   2.41745845e-01  7.14426764e-01  3.89027934e-01  2.92983514e-01
[particle_filter_localisation-7]   2.88262526e-01 -3.46352291e-01 -1.59347115e-01 -3.29548863e-01
[particle_filter_localisation-7]   3.56135928e-01 -5.35113440e-02  1.21354622e-01 -1.87379269e-01
[particle_filter_localisation-7]   3.71687551e-01  7.42929426e-01 -2.03555517e-01  7.91732441e-01
[particle_filter_localisation-7]   5.90039115e-01 -1.15296645e-01  1.46923405e-01  8.32099855e-01
[particle_filter_localisation-7]  -3.02983018e-01 -1.48044516e-01  1.39370863e-01 -3.94472588e-01
[particle_filter_localisation-7]   3.45535150e-01 -7.79481665e-01  2.54547838e-01  1.17311951e+00
[particle_filter_localisation-7]  -2.27218918e-01  4.71807093e-02  1.82756477e-01  1.06039636e+00
[particle_filter_localisation-7]   7.15769801e-01  1.09399179e+00 -6.30605341e-02 -3.07635730e-01
[particle_filter_localisation-7]  -6.68878799e-01  1.06893839e-02  9.53937205e-01  2.38351575e-01
[particle_filter_localisation-7]   3.43404627e-02 -3.34814750e-01 -5.09398200e-01  7.52952136e-02
[particle_filter_localisation-7]  -4.31682552e-01 -1.24091549e+00  3.05450398e-01 -2.91916533e-01
[particle_filter_localisation-7]   2.15476135e-01 -8.48420233e-01 -3.62802779e-01 -1.01820725e-01
[particle_filter_localisation-7]  -8.96495355e-01  8.59205726e-01  1.97681376e-01  4.24038814e-01
[particle_filter_localisation-7]   1.57450238e-01  5.91051100e-01 -2.08256094e-01 -2.08041219e-01
[particle_filter_localisation-7]   3.93237947e-01  5.43994107e-01  6.42520188e-01  1.65468727e-01
[particle_filter_localisation-7]   1.83143751e-01  4.22626709e-01  1.53234937e-01  1.13675261e-01
[particle_filter_localisation-7]  -2.99281980e-01  5.52374252e-02  2.79664844e-01  2.98804095e-01
[particle_filter_localisation-7]  -3.84168539e-01 -5.59448582e-01  3.03536761e-01  4.64032539e-02
[particle_filter_localisation-7]   2.24377295e-01 -3.60880233e-01 -1.92120195e-01 -1.15078783e+00
[particle_filter_localisation-7]   1.02497740e+00 -2.40683498e-01  2.59048525e-01 -7.02673767e-01
[particle_filter_localisation-7]   5.34264525e-01 -8.91531944e-02 -1.49178376e-01  3.49943241e-01
[particle_filter_localisation-7]  -1.06440342e-01  4.10223181e-01 -7.84569209e-01  8.45187593e-01
[particle_filter_localisation-7]  -2.71059359e-01 -4.11613098e-01  1.68875192e-01  1.46726869e-02
[particle_filter_localisation-7]  -5.42501884e-01 -7.66138308e-02 -3.42390047e-01 -2.03589956e-01
[particle_filter_localisation-7]  -4.90998123e-01 -3.33640193e-01  9.97657259e-02  1.15507148e-01
[particle_filter_localisation-7]   2.59048153e-02 -1.14897244e+00  5.16426359e-01 -4.03196228e-01
[particle_filter_localisation-7]  -3.27695100e-01 -3.48054562e-01  3.11117656e-01 -1.04606042e-01
[particle_filter_localisation-7]  -6.76510788e-02 -7.89772890e-01  9.94768606e-01 -8.28244548e-01
[particle_filter_localisation-7]   1.78225574e-01  2.02932689e-01  5.74173527e-01  5.20538460e-01
[particle_filter_localisation-7]  -6.28535387e-02 -5.60780781e-01 -2.84640115e-01  3.20689407e-01
[particle_filter_localisation-7]  -1.78700312e-01  2.27327091e-01 -4.74149550e-01 -8.80620612e-01
[particle_filter_localisation-7]  -1.94416469e-01  3.58556445e-01  3.11623440e-01 -2.54407200e-01
[particle_filter_localisation-7]   5.00122085e-01  3.40279847e-01  5.27346738e-01 -2.38620565e-01
[particle_filter_localisation-7]   9.41115548e-01  3.44391334e-01  1.79469886e-01 -7.06717987e-01
[particle_filter_localisation-7]  -1.14177243e+00  1.66682058e-01 -5.69953600e-01  1.49915646e-01
[particle_filter_localisation-7]   3.01134862e-01  4.36561035e-01 -4.54447400e-01  2.14714379e-01
[particle_filter_localisation-7]   8.37540647e-02  5.32848191e-02 -1.81222685e-01 -3.25450191e-02
[particle_filter_localisation-7]  -7.39147784e-01 -7.46966252e-02 -6.22028717e-01  9.12746723e-02
[particle_filter_localisation-7]   2.13386635e-01 -7.71114261e-01 -8.96433060e-02 -1.00097273e-02
[particle_filter_localisation-7]  -1.11538357e-01 -4.25604967e-02 -5.33422183e-02  1.23375264e-01
[particle_filter_localisation-7]   4.46926481e-02  5.07938171e-01  5.30393744e-01 -2.78344147e-01
[particle_filter_localisation-7]   5.31108381e-01 -1.28078012e-01 -2.58027883e-01  9.41167490e-02
[particle_filter_localisation-7]   2.86196307e-01  4.41122158e-01  2.33761583e-01  1.41872475e+00
[particle_filter_localisation-7]  -5.18607568e-01  3.14941312e-01  9.38782932e-02 -9.29767964e-01
[particle_filter_localisation-7]  -2.66063985e-01 -2.96933965e-01  8.41181877e-02 -4.60443132e-01
[particle_filter_localisation-7]   1.58840116e-01 -2.09459886e-01 -6.54210957e-01  1.87729357e-01
[particle_filter_localisation-7]  -1.09344429e+00 -3.84449530e-01  3.44269185e-01  4.50123067e-01
[particle_filter_localisation-7]  -8.70243571e-01  1.35266737e-01  4.49018577e-01 -5.16706324e-01
[particle_filter_localisation-7]  -2.41470469e-01  7.56242262e-01  1.19205295e-01  8.20464066e-01
[particle_filter_localisation-7]   3.70762886e-01 -2.82184637e-01 -5.25437602e-01 -1.54599439e-01
[particle_filter_localisation-7]   3.76331507e-01  1.32860866e-01 -2.11840202e-01 -3.13123344e-02
[particle_filter_localisation-7]   4.76383991e-01  8.40344813e-01 -5.52097572e-02  2.04636380e-02
[particle_filter_localisation-7]   4.60192980e-01 -1.55880614e-01 -1.11514726e+00  6.97338245e-01
[particle_filter_localisation-7]   1.47240999e-02  4.12943657e-01  1.46400179e+00 -9.92659291e-02
[particle_filter_localisation-7]   8.23309190e-01  3.28134570e-01  8.84231104e-02  8.34761261e-01
[particle_filter_localisation-7]   9.67155126e-01 -3.36699634e-01 -5.72446332e-02 -2.28031038e-01
[particle_filter_localisation-7]   1.16409677e+00  8.39130639e-01  1.13214486e-01  6.28898468e-01
[particle_filter_localisation-7]   7.34918325e-01 -6.59443389e-01 -3.80527197e-01 -1.03930852e-02
[particle_filter_localisation-7]  -1.97774065e-01  1.16382405e+00  5.58709395e-01 -7.12776813e-01
[particle_filter_localisation-7]   3.63415972e-01  1.15740329e+00  1.08768294e-01  2.71535399e-01
[particle_filter_localisation-7]  -3.07589986e-01 -4.80861781e-01 -7.67243442e-01 -4.44628184e-01
[particle_filter_localisation-7]  -1.43823886e-01 -6.23944725e-02 -5.89326254e-01 -4.27667006e-01
[particle_filter_localisation-7]   3.41881915e-01  1.59839415e-01  8.51458039e-02 -1.77335036e-01
[particle_filter_localisation-7]  -1.25660964e-03  6.32880543e-01 -2.11875164e-01 -2.74715630e-01
[particle_filter_localisation-7]   1.46537116e-01  2.43236916e-01 -3.27984406e-01  4.96572881e-02
[particle_filter_localisation-7]  -1.34311180e-01 -4.21072041e-01  6.11973560e-01  4.97087161e-01
[particle_filter_localisation-7]  -5.21134821e-02  4.42858296e-01  2.87315708e-01  6.98345944e-02
[particle_filter_localisation-7]   1.06117248e+00 -5.81759135e-02 -6.49878474e-03 -3.63999925e-01
[particle_filter_localisation-7]   6.73472056e-02  2.49333400e-01 -1.55846392e-01  3.93387419e-01
[particle_filter_localisation-7]  -1.63442947e-01  2.57520731e-02  8.58422902e-02  3.31711414e-01
[particle_filter_localisation-7]  -1.33296763e-01  1.00326013e-01 -9.11627249e-01 -5.15167394e-02
[particle_filter_localisation-7]  -1.60940169e-01  2.23036739e-01  2.83745696e-01  1.06287361e+00
[particle_filter_localisation-7]  -6.22188471e-01  1.00240236e-01 -1.35914747e-02  2.96814240e-01
[particle_filter_localisation-7]  -3.02574223e-01  3.10731217e-01  9.81585244e-03  7.68879966e-01
[particle_filter_localisation-7]   3.00544257e-01  6.07888093e-01 -1.37154090e-01  4.58564226e-01
[particle_filter_localisation-7]  -2.84468479e-01 -3.00916507e-01 -1.25564893e+00  3.58523449e-01
[particle_filter_localisation-7]   6.17402671e-01  5.26264866e-01  1.04534281e+00 -7.63772046e-02
[particle_filter_localisation-7]  -3.39343232e-01  7.58638498e-01  1.04471615e-01  1.03163183e-01
[particle_filter_localisation-7]   9.89302285e-01  7.47881161e-01 -1.61035098e-01  1.32985297e+00
[particle_filter_localisation-7]   3.39597921e-01 -8.21229123e-01 -2.73242329e-01  1.44549557e+00
[particle_filter_localisation-7]  -6.02635243e-01  5.30628392e-01 -5.11554306e-02 -4.10085514e-01
[particle_filter_localisation-7]  -7.04039962e-01  3.54356625e-01  4.94011652e-01  2.35420772e-01
[particle_filter_localisation-7]   2.84893680e-02  2.05868898e-01  5.33072160e-01 -4.12325049e-02
[particle_filter_localisation-7]   3.31335088e-01  7.51595773e-01 -9.06253695e-01  2.81293839e-02
[particle_filter_localisation-7]   3.15467863e-01  3.08857667e-01  2.90791043e-01  5.00896953e-02
[particle_filter_localisation-7]  -3.64959584e-01  9.21997106e-01 -3.35686457e-01  6.42274251e-02
[particle_filter_localisation-7]  -3.94591761e-01  1.20050867e+00  4.13682410e-01 -4.86591358e-01
[particle_filter_localisation-7]   6.10931520e-02 -1.65888484e-01 -9.22428857e-02  6.29886784e-01
[particle_filter_localisation-7]   8.89224173e-01 -1.02871038e+00  6.62316547e-01 -1.77910205e-01
[particle_filter_localisation-7]   4.23662146e-01  2.46456985e-01  6.18665590e-01  2.83359325e-02
[particle_filter_localisation-7]   3.19250645e-01  2.53685402e-01  2.36018832e-01  2.66033962e-02
[particle_filter_localisation-7]  -2.73771493e-01 -1.92640476e-01 -3.03041308e-01  5.53474504e-01
[particle_filter_localisation-7]   4.30302439e-02 -1.30104921e-01  4.60290848e-01 -4.60768358e-02
[particle_filter_localisation-7]   5.14559019e-01  2.42301395e-01  2.77216078e-01  1.29850606e-01
[particle_filter_localisation-7]   6.03786398e-01  4.94896080e-01  3.18969809e-01  6.12836093e-02
[particle_filter_localisation-7]  -3.48726562e-03 -2.81519890e-01  1.99817906e-01 -4.68822854e-01
[particle_filter_localisation-7]  -3.25682779e-02 -3.54271333e-01 -2.61700082e-01 -1.66229857e-01
[particle_filter_localisation-7]  -5.96331104e-02  1.96497075e-01  1.56285667e-01 -2.03878810e-01
[particle_filter_localisation-7]   1.44213019e-01  9.84483808e-01  1.03247113e-01 -8.13852720e-02
[particle_filter_localisation-7]  -1.82405142e-01  1.79575604e-01 -1.38581301e-01  4.40784148e-02
[particle_filter_localisation-7]  -2.41010530e-01 -7.03562387e-02  9.03846638e-01  7.45007107e-01
[particle_filter_localisation-7]  -2.33716769e-01  9.06616963e-01 -5.12141842e-02  8.08250129e-01
[particle_filter_localisation-7]   5.90612238e-01  8.32874462e-01 -7.90534513e-02  5.73568911e-01]
[particle_filter_localisation-7] [Elena Debug - Task 3] Gaussian distribution y:  [ 9.45681005e-01  3.84445033e-01  2.75103392e-01 -6.32081241e-01
[particle_filter_localisation-7]   9.88949713e-03 -1.03622964e-01 -6.15597175e-02 -3.80433167e-01
[particle_filter_localisation-7]  -2.47823927e-01  2.55818433e-01 -8.52828870e-02  1.71494127e-01
[particle_filter_localisation-7]   6.46844001e-02 -7.13638277e-01  3.29524910e-01  7.73588746e-02
[particle_filter_localisation-7]   2.01153801e-01  1.51252839e+00  3.85202144e-01 -1.14708714e+00
[particle_filter_localisation-7]   9.01577390e-01  4.99722533e-01 -4.11747233e-01 -5.19619601e-01
[particle_filter_localisation-7]  -4.46492490e-01  5.94524706e-04  3.91321959e-01 -9.55861082e-01
[particle_filter_localisation-7]  -2.23222234e-01 -4.47552768e-01  4.60882243e-01  3.18570283e-02
[particle_filter_localisation-7]  -4.46336820e-01 -1.12547264e+00  4.07163292e-02  2.32605923e-01
[particle_filter_localisation-7]  -5.68824460e-02 -2.05076303e-01 -4.57831583e-01  3.22076782e-01
[particle_filter_localisation-7]  -2.89996578e-01 -2.62818425e-01 -6.16427565e-01 -3.32750270e-01
[particle_filter_localisation-7]   5.11399699e-01  8.00429660e-01 -1.33442434e-01 -7.87492828e-01
[particle_filter_localisation-7]  -3.22554860e-01 -1.63446679e-01 -4.02722869e-01  2.93189531e-01
[particle_filter_localisation-7]  -4.92875604e-01 -5.18872547e-02  2.27878500e-01 -1.19631795e-01
[particle_filter_localisation-7]   1.90425207e-01 -9.12200811e-02 -1.68276082e-01 -5.29615486e-01
[particle_filter_localisation-7]   3.95197544e-01  9.68089555e-02 -4.12838710e-02 -2.07262474e-02
[particle_filter_localisation-7]  -2.96673118e-01 -1.06311841e-01  2.06091826e-01 -7.17963434e-01
[particle_filter_localisation-7]   2.97819246e-01  2.13323387e-01  1.83279008e-01 -6.89730351e-01
[particle_filter_localisation-7]  -2.68363085e-01 -7.49286943e-01  1.27719883e+00  3.51513631e-01
[particle_filter_localisation-7]   5.78690873e-01  1.03235744e+00 -4.26605436e-01  3.13039378e-01
[particle_filter_localisation-7]  -2.56345394e-01 -3.28265905e-01  4.52918797e-01 -2.70738740e-01
[particle_filter_localisation-7]  -8.31192081e-01 -5.56963485e-01 -4.33996562e-02 -4.72571679e-01
[particle_filter_localisation-7]  -1.63625956e-01  1.45518872e-01 -7.18826188e-01 -1.39434204e-01
[particle_filter_localisation-7]  -1.49239270e-01 -2.48444695e-01  1.41366462e-01 -6.14412416e-01
[particle_filter_localisation-7]   7.01874152e-01  1.22951484e+00 -7.70617387e-03  3.00135052e-01
[particle_filter_localisation-7]  -2.38090819e-01  2.64970699e-01 -6.04236641e-01 -6.71954015e-01
[particle_filter_localisation-7]  -2.11914656e-01  1.08757381e-01  6.62227254e-01 -1.11282506e+00
[particle_filter_localisation-7]   3.36172115e-01 -3.44023830e-01 -1.24113708e+00  1.33610552e+00
[particle_filter_localisation-7]   6.76633694e-01 -4.62753256e-01 -4.71752948e-01 -2.50769814e-02
[particle_filter_localisation-7]  -4.45849160e-01 -7.89995415e-01 -3.13849371e-01 -2.33485563e-01
[particle_filter_localisation-7]  -1.26891123e-01 -2.18829380e-01  4.88651223e-02  7.74902406e-01
[particle_filter_localisation-7]  -9.12404341e-01  4.79133694e-01 -6.57973263e-01  1.59630454e-01
[particle_filter_localisation-7]  -1.40212791e+00  2.29597296e-01 -6.57611716e-01  4.23424784e-01
[particle_filter_localisation-7]  -1.26295851e-01 -7.39504788e-02  1.52753624e-01  6.69802555e-01
[particle_filter_localisation-7]   5.34584440e-02 -5.91880926e-01 -2.95503243e-01  6.77044916e-01
[particle_filter_localisation-7]   2.24996967e-01 -6.77052920e-01 -1.00751213e+00  5.81839836e-01
[particle_filter_localisation-7]   6.51086177e-01 -2.94568605e-01 -4.13675187e-01 -1.08747506e+00
[particle_filter_localisation-7]   2.65824006e-01  5.06433507e-02  5.73341664e-02 -1.75425262e-02
[particle_filter_localisation-7]  -5.19240392e-01  4.53072633e-01 -4.76641135e-01 -2.38954595e-01
[particle_filter_localisation-7]   2.87486901e-01  9.75346975e-01  3.74068897e-01 -6.02713489e-01
[particle_filter_localisation-7]   1.51770437e-01  3.10906810e-01  4.21242252e-02 -6.08689866e-01
[particle_filter_localisation-7]   9.86846444e-01  8.28144328e-01 -6.14122265e-01 -8.55567083e-01
[particle_filter_localisation-7]   1.89076206e-01  4.77485792e-01  2.56329402e-01  2.30489941e-01
[particle_filter_localisation-7]  -2.99396030e-01 -4.65731671e-03 -5.39897311e-01  1.35471231e-01
[particle_filter_localisation-7]  -2.55734071e-01 -6.62034189e-01 -1.30537276e-01 -1.46676162e-01
[particle_filter_localisation-7]  -2.35217450e-01  2.67941326e-01 -3.94229578e-01 -4.39017308e-01
[particle_filter_localisation-7]   3.62474231e-01  8.49951166e-01 -1.98663779e-01  9.79842555e-01
[particle_filter_localisation-7]  -1.33306132e-01 -1.00232839e-01 -5.35544174e-01 -7.02568168e-01
[particle_filter_localisation-7]   5.18034622e-01  2.27650287e-01  3.78343466e-01 -2.17542361e-01
[particle_filter_localisation-7]   6.37846123e-01 -8.63136990e-01 -7.58024937e-01 -1.55232291e-01
[particle_filter_localisation-7]  -1.23149397e-01  4.93006822e-01  2.49548156e-01 -7.02351887e-02
[particle_filter_localisation-7]   8.87889885e-03 -1.39425648e-01  4.63300391e-01  4.52437860e-01
[particle_filter_localisation-7]  -5.22495100e-01 -2.46017451e-01 -6.90502499e-01  3.85457283e-01
[particle_filter_localisation-7]  -6.05569168e-01 -9.60828900e-01  4.21427053e-01  7.40172004e-01
[particle_filter_localisation-7]  -2.86356861e-01  1.55558693e-01 -2.84710383e-01 -7.56196968e-02
[particle_filter_localisation-7]  -6.43362756e-01 -5.57733478e-01 -5.02352444e-01  2.76855820e-01
[particle_filter_localisation-7]  -8.74459890e-02 -3.01136931e-01  4.69550594e-01  5.78360913e-01
[particle_filter_localisation-7]   1.46684519e-01  1.34294876e-01 -3.57355981e-01  2.93937084e-01
[particle_filter_localisation-7]  -1.15438840e-01  3.06923328e-01 -1.81788237e-01  2.97321238e-01
[particle_filter_localisation-7]   3.22659004e-02  8.81036239e-01  1.06275318e+00 -1.46477645e-01
[particle_filter_localisation-7]  -2.15858262e-01 -6.25362004e-01 -1.23380297e+00 -3.28914898e-01
[particle_filter_localisation-7]   6.01423983e-01  6.53303841e-01 -2.64039280e-01  6.75605379e-01
[particle_filter_localisation-7]   9.68850111e-01 -1.83547019e-01  6.53939678e-02 -1.80353860e-01
[particle_filter_localisation-7]   1.12321460e-01  8.60116716e-01 -1.86478560e-01 -7.87142288e-01
[particle_filter_localisation-7]   1.75465701e-01  3.61824020e-01  1.82333318e-01 -3.77698253e-01
[particle_filter_localisation-7]   4.37676469e-01 -3.16516428e-01 -8.19167585e-01 -5.82618524e-02
[particle_filter_localisation-7]  -1.32919945e+00 -4.59081776e-01 -1.04206400e-01 -5.54225932e-01
[particle_filter_localisation-7]   1.51175949e-01 -2.89790133e-01 -2.30971257e-01 -5.55854700e-01
[particle_filter_localisation-7]   6.52098359e-02  1.36300123e-01 -7.10271930e-02 -3.45145748e-01
[particle_filter_localisation-7]  -8.55372941e-01  1.00231243e-01 -8.07926419e-01  5.40610805e-01
[particle_filter_localisation-7]  -1.52806956e-01  3.15247242e-01  6.87967378e-01  2.71292138e-01
[particle_filter_localisation-7]  -2.31987064e-01  4.23731506e-01 -4.31717733e-01  1.23658103e+00
[particle_filter_localisation-7]  -9.63183112e-02 -5.53325767e-01  1.61205187e-01 -5.56189722e-01
[particle_filter_localisation-7]   8.26544961e-01  2.66047692e-01  1.95594291e-01  1.74750663e-01
[particle_filter_localisation-7]   3.50825423e-01  2.58742203e-01  4.01957901e-02  7.53802683e-01
[particle_filter_localisation-7]  -9.69107654e-01 -6.00885110e-01 -4.73211193e-01  2.57639165e-01
[particle_filter_localisation-7]  -7.82407481e-02 -5.36568270e-01 -6.88875729e-01 -1.29721342e+00
[particle_filter_localisation-7]  -1.44145629e-01 -6.04043285e-01 -4.54544416e-01 -3.06168672e-01
[particle_filter_localisation-7]   1.76072230e-02  1.41254763e-01  8.45947866e-01 -1.90506225e-01
[particle_filter_localisation-7]  -6.40302823e-02 -7.09541264e-01  4.79968677e-01  3.37061445e-01
[particle_filter_localisation-7]  -8.96865699e-01  3.50191494e-01  2.06094830e-01  1.74425426e-01
[particle_filter_localisation-7]  -3.92742189e-01 -9.33719555e-02  1.66518883e-01 -3.21278535e-01
[particle_filter_localisation-7]   2.21090713e-01  6.51705961e-02 -5.74604272e-02 -6.30250226e-01
[particle_filter_localisation-7]   8.96217395e-02 -3.26317796e-01 -5.09323214e-01  6.03201255e-01
[particle_filter_localisation-7]   4.88440099e-01 -1.49869315e+00  1.18686413e-02 -4.30704144e-01
[particle_filter_localisation-7]  -1.33022400e-01  6.01715602e-01  3.49001659e-02 -2.17356883e-01
[particle_filter_localisation-7]   5.57271875e-01 -9.35827930e-01  6.15720196e-01  1.16496726e-01
[particle_filter_localisation-7]   2.84846991e-02 -1.01893443e+00 -3.71005822e-01 -1.73348688e-01
[particle_filter_localisation-7]   4.12130031e-01 -1.51932491e-01  7.70100659e-02 -3.83253348e-01
[particle_filter_localisation-7]  -4.61775780e-01  2.58479173e-01  9.18711848e-01  3.83198314e-01
[particle_filter_localisation-7]   1.83849604e-02  6.88040839e-01 -2.52274658e-01 -4.53097796e-01
[particle_filter_localisation-7]   1.62602978e-01 -3.70362401e-01  4.79520181e-01  6.17832136e-01
[particle_filter_localisation-7]  -1.13574995e+00 -1.56771701e-01 -2.83456397e-01  2.73196923e-01
[particle_filter_localisation-7]  -6.59183733e-01 -9.35401916e-01  7.58418992e-01  3.81789509e-01
[particle_filter_localisation-7]  -3.07423427e-01  2.60170146e-01  5.07022477e-01  7.49136938e-01
[particle_filter_localisation-7]  -1.41966359e+00 -8.96215835e-01 -2.84685431e-01 -9.93114594e-01
[particle_filter_localisation-7]   2.17344506e-01 -1.73782291e-01 -2.19469538e-01 -2.18383202e-01
[particle_filter_localisation-7]  -2.37129783e-01 -5.13823841e-01  6.35291441e-01  3.36500741e-01
[particle_filter_localisation-7]   1.17510104e-01  4.60304974e-01  6.26899815e-03  1.64791540e+00
[particle_filter_localisation-7]  -6.86191254e-01 -1.39228975e+00  5.10609282e-02 -1.69811779e-02
[particle_filter_localisation-7]  -2.14974861e-01 -1.84763069e-01  3.78253125e-01  2.24795754e-01
[particle_filter_localisation-7]   3.98303865e-01 -1.92776478e-01  1.71141685e-01  1.51810519e-01
[particle_filter_localisation-7]  -5.14809440e-01  7.17578601e-01 -6.65384894e-01 -6.91331380e-02
[particle_filter_localisation-7]  -1.00215981e+00 -7.78950576e-03  7.99179213e-03 -3.56245280e-01
[particle_filter_localisation-7]  -1.15834259e+00 -4.59169248e-01  2.68496949e-01  4.54438617e-01
[particle_filter_localisation-7]  -3.98717559e-01 -1.01756815e+00  5.08029732e-01  1.11877982e-01
[particle_filter_localisation-7]  -2.52866174e-01  3.27365319e-02  6.97852268e-02  2.13043736e-01
[particle_filter_localisation-7]   2.58301569e-03 -8.04014028e-01 -3.28778151e-01  2.11935246e-01
[particle_filter_localisation-7]  -5.79858355e-01  2.03386990e-01  1.61856064e-01 -2.40155328e-01
[particle_filter_localisation-7]  -2.10371559e-01  1.30995471e-03  8.13997716e-02 -7.34433067e-01
[particle_filter_localisation-7]  -5.22812004e-02 -1.69252410e-01  3.74785964e-01 -2.35754367e-01
[particle_filter_localisation-7]  -1.35293465e+00  5.89786573e-01 -6.03399455e-02 -8.43973605e-02
[particle_filter_localisation-7]  -6.32068906e-01  4.40095796e-01 -1.11628957e-02 -1.71403981e-01
[particle_filter_localisation-7]   2.01551851e-01  4.81073299e-01 -4.38514319e-01  8.06883324e-01
[particle_filter_localisation-7]   8.34932594e-01 -2.69017302e-01 -9.20290357e-01 -8.24327029e-02
[particle_filter_localisation-7]  -2.94984466e-01  3.03635588e-01 -2.86462235e-01  1.73856767e-01
[particle_filter_localisation-7]   5.26608169e-02  3.59311747e-01 -4.67801873e-02  6.47615112e-02
[particle_filter_localisation-7]   3.00653870e-01 -1.42406818e-01 -1.06773217e+00 -8.51172989e-01
[particle_filter_localisation-7]  -3.56854611e-01 -3.30096395e-02 -2.95862061e-02 -1.53257208e-01
[particle_filter_localisation-7]  -1.36951411e-01 -1.49699693e-01 -6.34902506e-01 -1.61038265e-01
[particle_filter_localisation-7]  -8.13908161e-01 -6.24803145e-01 -8.95824772e-01  2.69886448e-01
[particle_filter_localisation-7]  -6.52209505e-02  9.11120361e-01  5.03126827e-01  7.67759747e-01
[particle_filter_localisation-7]   5.07150134e-01 -3.18302771e-01 -1.06222604e+00  8.95685602e-01
[particle_filter_localisation-7]   4.21954101e-01  1.57399808e-01  2.72924982e-01  7.22709538e-02
[particle_filter_localisation-7]   8.77123835e-01 -3.44810438e-01  6.80431062e-01 -7.14297755e-01]
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  0 : x= -0.509867834443009 , y= 0.9456810053854128
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  1 : x= 0.9027960692153134 , y= 0.3844450333245517
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  2 : x= 0.26346783329216295 , y= 0.27510339224212155
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  3 : x= 0.29506582022172967 , y= -0.6320812414438572
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  4 : x= 0.5782187086998152 , y= 0.009889497131505526
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  5 : x= -0.04420192977163426 , y= -0.1036229635602067
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  6 : x= -0.09524978329982758 , y= -0.06155971751502365
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  7 : x= 0.6069995782945407 , y= -0.3804331674491415
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  8 : x= -0.12146543679267802 , y= -0.24782392725511945
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  9 : x= 0.18402122345760147 , y= 0.25581843285071554
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  10 : x= 0.055291166015280925 , y= -0.08528288695201384
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  11 : x= -0.057884524583446034 , y= 0.17149412713547588
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  12 : x= -0.016115999491834912 , y= 0.06468440007946938
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  13 : x= 0.3497458688385299 , y= -0.7136382766910403
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  14 : x= 0.7177317298755402 , y= 0.32952490984800736
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  15 : x= -0.21048888712972436 , y= 0.07735887463584651
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  16 : x= -0.16107205309634487 , y= 0.201153801343658
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  17 : x= -0.5248389873023749 , y= 1.5125283877798783
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  18 : x= 0.04245821478446522 , y= 0.3852021442943513
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  19 : x= 0.6125901266236063 , y= -1.1470871431453664
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  20 : x= 0.1709693539332943 , y= 0.9015773899222216
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  21 : x= 0.7458927723744428 , y= 0.49972253285394563
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  22 : x= 0.08721191700198763 , y= -0.4117472330939345
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  23 : x= -0.1615081739129547 , y= -0.5196196008791614
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  24 : x= -0.2621287610179754 , y= -0.4464924903348217
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  25 : x= -0.33764346872574935 , y= 0.0005945247064790687
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  26 : x= 1.3249345826539882 , y= 0.3913219594867088
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  27 : x= -0.38693982383253717 , y= -0.9558610818544464
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  28 : x= -0.7365782591663941 , y= -0.22322223439959846
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  29 : x= -0.6549166549811546 , y= -0.44755276809457284
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  30 : x= -0.2821648554977969 , y= 0.4608822428511764
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  31 : x= 0.2287507106257663 , y= 0.03185702833458251
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  32 : x= -0.29651815520507374 , y= -0.44633681973569556
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  33 : x= 0.37863092692399364 , y= -1.1254726413138214
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  34 : x= -0.8100491231553384 , y= 0.0407163291853605
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  35 : x= 0.12352209321569824 , y= 0.2326059234507808
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  36 : x= -0.15231389510068383 , y= -0.056882445978467644
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  37 : x= 0.18349957427150818 , y= -0.20507630268611377
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  38 : x= 0.14421628734576583 , y= -0.45783158348468744
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  39 : x= -1.2151204770347026 , y= 0.3220767816316082
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  40 : x= -0.6775546453257958 , y= -0.2899965775033697
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  41 : x= -0.3038239387761996 , y= -0.26281842519602555
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  42 : x= -0.39656511671896566 , y= -0.6164275652954211
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  43 : x= 0.15429446543046713 , y= -0.3327502698571653
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  44 : x= 0.13629131214214307 , y= 0.511399699008617
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  45 : x= 0.3642894462909274 , y= 0.8004296596130699
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  46 : x= -0.7342792463285123 , y= -0.1334424338925665
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  47 : x= 0.14992763082812757 , y= -0.787492828249573
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  48 : x= 0.5084943692655829 , y= -0.3225548604962866
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  49 : x= 0.12978424689883347 , y= -0.16344667857833933
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  50 : x= -0.3545331275869387 , y= -0.402722869013337
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  51 : x= 0.26299087544473687 , y= 0.29318953056538494
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  52 : x= 0.6431474573194352 , y= -0.4928756040154374
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  53 : x= 0.46530768180659826 , y= -0.05188725466866048
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  54 : x= 0.3800187963704839 , y= 0.22787850049112401
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  55 : x= 0.13460873327497974 , y= -0.11963179480638114
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  56 : x= 0.6003838038784635 , y= 0.19042520658283796
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  57 : x= 0.16995731830468855 , y= -0.09122008110167115
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  58 : x= 0.47787885092835125 , y= -0.16827608214824036
[particle_filter_localisation-7] [Elena Debug - Task 3] Creating particle  59 : x= -0.04420722940268837 , y= -0.5296154860558726
```
Image:

![task_3](https://github.com/elenajusto/space_robotics/blob/main/images/task_3.png)


# python_tutorial
Diagram to help conceptulise what is happening regarding coordinates.

![coordinates](https://github.com/elenajusto/space_robotics/blob/main/images/coordinates.png)