#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Bool
import pigpio

class WeedingMotorNode(Node):
    def __init__(self):
        super().__init__("weeding_motor")

        self.motor_signal = 19
        self.pi = pigpio.pi()
        self.pi.set_mode(self.motor_signal, pigpio.OUTPUT)

        self.subscribe_timer_ = self.create_subscription(Bool, "presense_of_weeds", self.controll_motor, 10)
        self.get_logger().info("Weeding motor has been started.")
    
    def controll_motor(self, msg):
        self.pi.hardware_PWM(self.motor_signal, 60, 80000)
        if msg.data==True:
            self.pi.hardware_PWM(self.motor_signal, 60, 72000)
            self.get_logger().info("motor on")
        else:
            self.pi.hardware_PWM(self.motor_signal, 60, 80000)
            self.get_logger().info("motor off")

def main(args=None):
    rclpy.init(args=args)
    node = WeedingMotorNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
