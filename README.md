# Space Robotics Repository
Repo to hold code and notes I have for the Space Robotics subject at UTS.

# Assessment 1: Particle Filter Localisation
**Name:** Elena Justo

**Student Number:** 24429298

This will be the directory for assignment 1 located in `ros_ws/src/particle_filter_localisation`

Each task involves adding new code within the template code file:
`particle_filter_localisation/particle_filter_localisation.py`

### Summary of what was achieved
Qualitatively, my filter is able to predict the robot’s pose reasonably well some of the time.

Pose estimation works fairly accurately in placing the estimated pose where the highest-likelihood particles concentrate.

A key limitation is that while the filter predicts pose consistently at the particle clusters, it is still prone to noise and drift. For example, over time the predicted pose can remain consistent but steadily shift away from the robot’s true location.

I did not complete Task 8 due to time constraints.

### Reflection on development methodology
With the provided template code, I relied heavily on debug statements to confirm variable states and used code navigation to understand the data structures.

Once I built up that working understanding of the variables, implementing the tasks themselves became fairly straightforward.

### Sensor Performance
The LIDAR sensor performed much better than the terrain sensor. This makes sense, as LIDAR can detect unique environmental features (like rocks or barriers), whereas terrain measurements can remain constant over large areas of the map.

If a magnetometer had been available, I expect it would have reduced drift and minimised the offset between predicted and actual pose.

### Improvements if I had more time
Implement a system to be able to quantiatively log and measure accuracy of pose estimation and how much each new sensor or code implementation affects accuracy (maybe in the form of interactive graph or something).

### Video Demonstration
[![Demo](https://img.youtube.com/vi/BR6HmeLZgOo/hqdefault.jpg)](https://youtu.be/BR6HmeLZgOo)

The above video demonstrates the fully functioning system, however if you follow the below task outlines, there are images and gif's that demonstrate the features as each task is completed.

## Task 1: Initialise the particles
### Terminal Excerpt
```
particle_filter_localisation-7] [INFO] [1755404571.603887813] [particle_filter_localisation]: Map received
[particle_filter_localisation-7] Initialising particles...
[particle_filter_localisation-7] ELENA CODE IS HERE: 
[particle_filter_localisation-7] Number of particles:  500
[particle_filter_localisation-7] Particle  0 : x= 4.802749871556899 , y= 3.8302880390734293 , theta= 0.6746124818402024 , weight= 0.002
[particle_filter_localisation-7] Particle  1 : x= -0.5229773589749893 , y= -4.7229086151963715 , theta= 1.7002927009419688 , weight= 0.002
[particle_filter_localisation-7] Particle  2 : x= -0.4664302560862774 , y= -1.6076763492630453 , theta= 3.8277917338689647 , weight= 0.002
[particle_filter_localisation-7] Particle  3 : x= -3.9102432520196118 , y= -3.253604137372422 , theta= 5.42550954922847 , weight= 0.002
...
```
### Image
![task_1](https://github.com/elenajusto/space_robotics/blob/main/images/task_1.png)

### Code Excerpt
```python
print("[Elena Debug - Task 1] Number of particles: ", self.num_particles_)

for i in range(self.num_particles_):
    # Create a new particle
    particle_x = random_uniform(self.map_x_min_, self.map_x_max_)
    particle_y = random_uniform(self.map_y_min_, self.map_y_max_)
    particle_angle = random_uniform(0, 2 * math.pi)
    particle_weight = 1.0 / self.num_particles_ 

    # Save particle 
    self.particles_.append(Particle(particle_x, particle_y, particle_angle, particle_weight)) 

# View created particles - DEBUG
for i in range(self.num_particles_):
    print("[Elena Debug - Task 1] Particle ", i, ": x=", self.particles_[i].x, ", y=", self.particles_[i].y, ", theta=", self.particles_[i].theta, ", weight=", self.particles_[i].weight)

# Don't use the estimated pose just after initialisation
self.estimated_pose_valid_ = False

# Induce a sensing update
self.motion_update_count_laser_ = self.num_motion_updates_laser_
self.motion_update_count_terrain_ = self.num_motion_updates_terrain_

```
## Task 2: Normalise the weights
### Terminal Excerpt
```sh
...
[particle_filter_localisation-7] [Elena Debug] Particle  495 : x= 0.7837390144723768 , y= 1.0290591824138469 , theta= 0.6731380848859895 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug] Particle  496 : x= -1.6363628222335067 , y= 0.382219434015715 , theta= 5.700813535467078 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug] Particle  497 : x= -0.17485779971350635 , y= 3.8697129706192 , theta= 3.2665586641192776 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug] Particle  498 : x= -3.657429146662379 , y= 3.110209245288929 , theta= 0.3937238382323943 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug] Particle  499 : x= -3.559582408533349 , y= 1.73400479097824 , theta= 0.6801380652133294 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug] Normalised particle weight:  0.0019999999999999987
[particle_filter_localisation-7] [Elena Debug] Normalised particle weight:  0.0019999999999999987
[particle_filter_localisation-7] [Elena Debug] Normalised particle weight:  0.0019999999999999987
[particle_filter_localisation-7] [Elena Debug] Normalised particle weight:  0.0019999999999999987
[particle_filter_localisation-7] [Elena Debug] Normalised particle weight:  0.0019999999999999987
[particle_filter_localisation-7] [Elena Debug] Normalised particle weight:  0.0019999999999999987
[particle_filter_localisation-7] [Elena Debug] Normalised particle weight:  0.0019999999999999987
...
```
### Image
![task_2](https://github.com/elenajusto/space_robotics/blob/main/images/task_2.png)

### Code Excerpt
```python
# Since self.num_particles_ can be outdated
# We will work with the sum of weights of existing particles
total_weight = sum(p.weight for p in self.particles_)
if total_weight > 0:
    # Divide each paticle by the total weight
    for p in self.particles_:
        p.weight /= total_weight
        # TODO: Comment out this debug to see further tasks
        #print("[Elena Debug - Task 2] Normalised particle weight: ", p.weight)
else:
    # If all weights are zero, assign equal weights
    num_particles = len(self.particles_)
    if num_particles > 0:
        for p in self.particles_:
            p.weight = 1.0 / num_particles
```

## Task 3: Human operator input 

### Terminal Excerpt
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
### Image
![task_3](https://github.com/elenajusto/space_robotics/blob/main/images/task_3.png)

### Code Excerpt
```python
point_x = clicked_point_msg.point.x
point_y = clicked_point_msg.point.y

print("[Elena Debug - Task 3] Clicked point: x=", point_x, ", y=", point_y)

gaussian_distribution_x = np.random.normal(point_x, self.clicked_point_std_dev_, self.num_particles_)
gaussian_distribution_y = np.random.normal(point_y, self.clicked_point_std_dev_, self.num_particles_)

print("[Elena Debug - Task 3] Gaussian distribution x: ", gaussian_distribution_x)
print("[Elena Debug - Task 3] Gaussian distribution y: ", gaussian_distribution_y)

for i in range(self.num_particles_):
    print("[Elena Debug - Task 3] Creating particle ", i, ": x=", gaussian_distribution_x[i], ", y=", gaussian_distribution_y[i])
    particle_x = gaussian_distribution_x[i]
    particle_y = gaussian_distribution_y[i]
    particle_theta = random_uniform(0, 2 * math.pi)
    particle_weight = 1.0 / self.num_particles_
    self.particles_.append(Particle(particle_x, particle_y, particle_theta, particle_weight))

# Don't use the estimated pose just after initialisation
self.estimated_pose_valid_ = False

# Induce a sensing update
self.motion_update_count_laser_ = self.num_motion_updates_laser_
self.motion_update_count_terrain_ = self.num_motion_updates_terrain_
```

## Task 4: Motion Update
### Terminal Excerpt
```sh
[particle_filter_localisation-7] [Elena Debug - Task 4] Particle before motion update: x= 0.7499340822098212 , y= -0.30889787688876885 , theta= 1.0897263394868855 , weight= 0.0023310023310023154
[particle_filter_localisation-7] [Elena Debug - Task 4] Particle after motion update: x= 0.7587930546888315 , y= -0.27699274059996193 , theta= 1.1722191521637617 , weight= 0.0023310023310023154
[particle_filter_localisation-7] [Elena Debug - Task 4] Particle before motion update: x= -2.1653050288915976 , y= -0.8470391674637086 , theta= 3.1901042844964 , weight= 0.0023310023310023154
[particle_filter_localisation-7] [Elena Debug - Task 4] Particle after motion update: x= -2.191210293692166 , y= -0.8492060471734064 , theta= 3.1525013347594357 , weight= 0.0023310023310023154
```

### Gif
![task_4](https://github.com/elenajusto/space_robotics/blob/main/images/task_4_gif.gif)

### Code Excerpt
```python
# Iterate through each particle
for p in self.particles_:

    # Debug
    #print("[Elena Debug - Task 4] Particle before motion update: x=", p.x, ", y=", p.y, ", theta=", p.theta, ", weight=", p.weight)

    # Update x position
    # x = x + (distannce moved + distance noise) * cos(theta)
    # p.x = p.x + 0.05 # Random value to check update
    p.x = p.x + (distance + random_normal(self.motion_distance_noise_stddev_)) * math.cos(p.theta)

    # Update y position
    # y = y + (distance moved + distance noise) * sin(theta)
    p.y = p.y + (distance + random_normal(self.motion_distance_noise_stddev_)) * math.sin(p.theta)

    # Update angle
    # theta = wrap_angle(theta + rotation turned + rotation noise)
    p.theta = wrap_angle(p.theta + rotation + random_normal(self.motion_rotation_noise_stddev_))    

    # Debug
    #print("[Elena Debug - Task 4] Particle after motion update: x=", p.x, ", y=", p.y, ", theta=", p.theta, ", weight=", p.weight)
```

## Task 5: Terrain Observation Update

### Gif
![task_5](https://github.com/elenajusto/space_robotics/blob/main/images/task_5_gif.gif)

### Code Excerpt
```python
likelihood = 1.0
# Terrain type at particle - This is class y in the confusion matrix
terrain_at_particle = self.visual_terrain_map_.get_ground_truth(p.x, p.y)
#print("[Elena Debug - Task 5] Particle at x=", p.x, ", y=", p.y, " has terrain type: ", terrain_at_particle)

# Terrian type at robot - This is class z in the confusion matrix
terrain_at_robot = terrain_msg.data
#print("[Elena Debug - Task 5] Robot observers terrain type: ", terrain_at_robot)

# Print weight before terrain update
#print("[Elena Debug - Task 5] Particle weight before terrain update: ", p.weight)

# Compare terrain type of particle and robot
#if terrain_at_particle == terrain_at_robot:
#    print("[Elena Debug - Task 5] MATCH")
#else:
#    print("[Elena Debug - Task 5] NOT MATCH")

# Add noise using confusion matrix
if terrain_at_particle == 0:
    # Agree at 0
    if terrain_at_robot == 0:
        p.weight = 0.9 * p.weight  
    else:
        p.weight = 0.2 * p.weight
elif terrain_at_particle == 1:
    # Agree at 1
    if terrain_at_robot == 1:
        p.weight = 0.9 * p.weight  
    else:
        p.weight = 0.2 * p.weight
elif terrain_at_particle == 2:
    # Agree at 2
    if terrain_at_robot == 2:
        p.weight = 0.9 * p.weight  
    else:
        p.weight = 0.2 * p.weight
elif terrain_at_particle == 3:
    # Agree at 3
    if terrain_at_robot == 3:
        p.weight = 0.9 * p.weight  
    else:
        p.weight = 0.2 * p.weight
elif terrain_at_particle == 4:
    # Agree at 4
    if terrain_at_robot == 4:
        p.weight = 0.9 * p.weight  
    else:
        p.weight = 0.2 * p.weight
elif terrain_at_particle == 5:
    # Agree at 5
    if terrain_at_robot == 5:
        p.weight = 0.9 * p.weight  
    else:
        p.weight = 0.2 * p.weight

# Print weight after terrin update
#print("[Elena Debug - Task 5] Particle weight after terrain update: ", p.weight)

# Update the particle weight with the likelihood
p.weight *= likelihood
```

## Task 6: Pose estimate
### Terminal Excerpt
```sh
...
[particle_filter_localisation-7] [Elena Debug - Task 1] Particle  497 : x= -4.850524473696125 , y= 4.914847139549949 , theta= 4.87659693515706 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug - Task 1] Particle  498 : x= 3.29678205553689 , y= -3.3984503722849966 , theta= 3.889552256853763 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug - Task 1] Particle  499 : x= 4.109906565107123 , y= 2.8822890474988787 , theta= 2.1479091142543005 , weight= 0.002
[particle_filter_localisation-7] [Elena Debug - Task 6] estimated_pose_x =  -0.6202051730498539
[particle_filter_localisation-7] [Elena Debug - Task 6] estimated_pose_y =  1.62349180702847
[particle_filter_localisation-7] [Elena Debug - Task 6] estimated_pose_theta =  -1.3484048785351084
```

### Gif
![task_6](https://github.com/elenajusto/space_robotics/blob/main/images/task_6.gif)

### Code Excerpt
```python
# Assume weighted average approach
weighted_x = 0.0
weighted_y = 0.0
cos_sum = 0.0
sin_sum = 0.0

# Calculate weighted averages
for p in self.particles_:
    weighted_x += p.x * p.weight
    weighted_y += p.y * p.weight

# For angular values, we need to use circular mean
cos_sum += math.cos(p.theta) * p.weight
sin_sum += math.sin(p.theta) * p.weight

# Calculate final pose estimates
estimated_pose_x = weighted_x  # Weights should sum to 1.0
estimated_pose_y = weighted_y
estimated_pose_theta = math.atan2(sin_sum, cos_sum)

# Debug
print("[Elena Debug - Task 6] estimated_pose_x = ", estimated_pose_x)
print("[Elena Debug - Task 6] estimated_pose_y = ", estimated_pose_y)
print("[Elena Debug - Task 6] estimated_pose_theta = ", estimated_pose_theta)

# Set the estimated pose message
self.estimated_pose_.position.x = estimated_pose_x
self.estimated_pose_.position.y = estimated_pose_y

self.estimated_pose_.orientation.w = math.cos(estimated_pose_theta / 2.)
self.estimated_pose_.orientation.z = math.sin(estimated_pose_theta / 2.)

self.estimated_pose_theta_ = estimated_pose_theta
self.estimated_pose_valid_ = True
```
## Task 7: Laser scan observation update

### Gif
![task_7](https://github.com/elenajusto/space_robotics/blob/main/images/task_7.gif)

### Code Excerpt
```python
# Implementing the PDF of a Gaussian distribution function
ray_diff = particle_range - scan_range
ray_likelihood = (1.0 / math.sqrt(2.0 * math.pi * self.sensing_noise_stddev_**2)) * \
                math.exp(-(ray_diff**2) / (2.0 * self.sensing_noise_stddev_**2))

likelihood *= ray_likelihood

ray_diff = particle_range - scan_range

ray_likelihood = (1.0 / math.sqrt(2.0 * math.pi * self.sensing_noise_stddev_**2)) * \
                math.exp(-(ray_diff**2) / (2.0 * self.sensing_noise_stddev_**2))

likelihood *= ray_likelihood
```

# Lab 1 Tutorial
Diagram to help conceptulise what is happening regarding coordinates.

![coordinates](https://github.com/elenajusto/space_robotics/blob/main/images/coordinates.png)