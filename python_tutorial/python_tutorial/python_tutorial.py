import math
import random
import numpy as np

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class Location:
    def __init__(self, x, y):

        # Save the input arguments as object variables
        self.x = x  # location in x-axis
        self.y = y  # location in y-axis


class WeightedAverager:
    def __init__(self, node, origin, landmarks):

        # Save the input arguments as object variables
        self.origin = origin
        self.landmarks = landmarks

        # Define parameters
        self.threshold = 10.0  # outliers beyond this distance should be ignored

        # Setup ROS publisher
        self.average_pub = node.create_publisher(Float32, 'average', 1)

        # Save the node logger for later use
        # To print things later, you can use it with self.parent_logger.info(...)
        self.parent_logger = node.get_logger()

    def weighted_average(self):
        distances = [] # List to hold distances

        # Task 2 - Calculate Distance
        for landmark in self.landmarks:
            distance = math.sqrt((landmark.x - self.origin.x) ** 2 + (landmark.y - self.origin.y) ** 2)
            distances.append(distance)
            print("Distance from origin to landmark at (" + str(landmark.x) + ", " + str(landmark.y) + ") is " + str(distance))
        
        print("Distance List: ", distances) # TODO: Debug

        # Task 3 - Calculate Average
        # Avg = Sum of each value / # of values
        avgSum = 0
        avgValNum = 0
        for i in range(len(distances)):
            avgSum += distances[i]
            avgValNum += 1
        avgDistance = avgSum / avgValNum

        print("Average distance: ", avgDistance) # TODO: Debug

        # Task 4 - Compute weighted average
        weights = []
        for i in range(len(distances)):
            random = np.random.rand()
            weights.append(random)

        print("Raw Weights: ", weights) # TODO: Debug

        weight_sum = 0
        for w in weights:
            weight_sum += w

        print("Raw Weight Sum: ", weight_sum) # TODO: Debug

        for i in range(len(weights)):
            weights[i] = weights[i] / weight_sum    

        print("Normalized Weights:", weights)

        weighted_sum = 0
        for i in range(len(distances)):
            weighted_sum += weights[i] * distances[i]

        print("Weighted average distance:", weighted_sum)

        return


class PythonTutorialNode(Node):
    def __init__(self):
        # Initialise this node
        super().__init__('python_tutorial_node')

        # Print message
        # In ROS, we use this syntax to get the 'logger' attached to this node then use the 'info'
        # category for this message
        self.get_logger().info('Finished setting up python_tutorial ROS node.')

        # Setup the data
        origin = Location(5.0, 5.0)
        landmarks = [Location(6.0, 7.0), Location(5.1, 4.9), Location(15.0, 20.0), Location(
            8.0, 0.0), Location(-3.0, 2.0), Location(-10.0, -10.0), Location(5.0, 5.0), Location(0.0, 0.0)]

        # Task 1 - Print Elements
        counter = 0
        while counter < len(landmarks):
            print("coordinate " + str(counter) + ": " + str(landmarks[counter].x) + "," + str(landmarks[counter].y))
            counter += 1
        
        # Create the WeightedAverager object
        weighted_averager = WeightedAverager(self, origin, landmarks)

        weighted_averager.weighted_average() # Call the loop of distances

        # Call the averaging function
        # answer = weighted_averager.weighted_average()


def main():
    # Initialise
    rclpy.init()

    # Create a ROS2 node where our code will run
    python_tutorial_node = PythonTutorialNode()
    
    while rclpy.ok():
        rclpy.spin(python_tutorial_node)


if __name__ == '__main__':
    main()
