import math
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class WeightedAverager:
    def __init__(self, node, origin, landmarks):
        self.origin = origin
        self.landmarks = landmarks
        self.threshold = 10.0
        self.parent_logger = node.get_logger()
        self.average_pub = node.create_publisher(Float32, 'average', 1)

    def calculate_distances(self):
        distances = []
        for lm in self.landmarks:
            dist = math.hypot(lm.x - self.origin.x, lm.y - self.origin.y)
            distances.append(dist)
        return distances

    def filter_distances(self, distances):
        valid_distances = []
        for dist in distances:
            if dist <= self.threshold:
                valid_distances.append(dist)
            else:
                continue
        return valid_distances

    def compute_weighted_average(self, distances):
        if not distances:
            self.parent_logger.warn("No valid distances to compute weighted average.")
            return None

        weights = np.random.rand(len(distances))
        weights /= weights.sum()  # Normalize weights

        weighted_sum = sum(w * d for w, d in zip(weights, distances))

        return weighted_sum

    def weighted_average(self):
        distances = self.calculate_distances()
        valid_distances = self.filter_distances(distances)
        return self.compute_weighted_average(valid_distances)


class PythonTutorialNode(Node):
    def __init__(self):
        super().__init__('python_tutorial_node')
        self.get_logger().info('Initialized python_tutorial ROS node.')

        origin = Location(5.0, 5.0)
        landmarks = [
            Location(6.0, 7.0), Location(5.1, 4.9), Location(15.0, 20.0),
            Location(8.0, 0.0), Location(-3.0, 2.0), Location(-10.0, -10.0),
            Location(5.0, 5.0), Location(0.0, 0.0)
        ]

        for idx, lm in enumerate(landmarks):
            self.get_logger().info(f"Coordinate {idx}: ({lm.x}, {lm.y})")

        self.weighted_averager = WeightedAverager(self, origin, landmarks)

        self.counter = 0
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.get_logger().info('Python node initialized with a 2-second timer.')

    def timer_callback(self):
        self.counter += 1
        self.answer = self.weighted_averager.weighted_average()
        self.get_logger().info(f'Timer callback #{self.counter}, Weighted Average: {self.answer}')


def main():
    rclpy.init()
    node = PythonTutorialNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
