import math
import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class Location:
    def __init__(self, x, y):

        # Save the input arguments as object variables
        self.x = x
        self.y = y


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

        # Create the WeightedAverager object
        # weighted_averager = WeightedAverager(self, origin, landmarks)

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
