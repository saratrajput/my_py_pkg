#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.msg import String
 
 
class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("number_counter")

        self.counter_ = 0
        # Create subscriber
        self.subscriber_ = self.create_subscription(Int64, "number",
                                                    self.callback_number_counter,
                                                    10)
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
        #self.timer_ = self.create_timer(0.5, self.callback_number_counter)
                                                
        self.get_logger().info("Number counter has started.")

    def callback_number_counter(self, msg):
        self.counter_ += msg.data
        self.get_logger().info("Number count is: " + str(self.counter_))

        new_msg = Int64()
        new_msg.data = self.counter_
        self.publisher_.publish(new_msg)

 
def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
