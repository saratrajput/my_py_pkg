#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
 
 
class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__("number_publisher")

        self.number_ = 2
        # Create publisher
        self.publisher_ = self.create_publisher(Int64, "number", 10)
        # Start timer and publish in the given frequency
        self.timer = self.create_timer(0.5, self.publish_number)
        # Log that the publisher has started
        self.get_logger().info("Robot News Station has been started.")

    def publish_number(self):
        msg = Int64()
        msg.data = self.number_
        self.publisher_.publish(msg)
 
 
def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
