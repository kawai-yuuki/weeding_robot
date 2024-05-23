#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import Sensor
import pigpio

class DrivingMotorNode(Node):
    def __init__(self):
        super().__init__("driving_motor")

        self.pi = pigpio.pi()

        self.MOT_R_1 = 23
        self.MOT_R_2 = 22
        self.MOT_L_1 = 18
        self.MOT_L_2 = 17
        self.pi.set_mode(self.MOT_R_1, pigpio.OUTPUT)
        self.pi.set_mode(self.MOT_R_2, pigpio.OUTPUT)
        self.pi.set_mode(self.MOT_L_1, pigpio.OUTPUT)
        self.pi.set_mode(self.MOT_L_2, pigpio.OUTPUT)
        self.pi.set_PWM_frequency(self.MOT_R_1, 1000)
        self.pi.set_PWM_frequency(self.MOT_R_2, 1000)
        self.pi.set_PWM_frequency(self.MOT_L_1, 1000)
        self.pi.set_PWM_frequency(self.MOT_L_2, 1000)
        self.pi.set_PWM_range(self.MOT_R_1, 100)
        self.pi.set_PWM_range(self.MOT_R_2, 100)
        self.pi.set_PWM_range(self.MOT_L_1, 100)
        self.pi.set_PWM_range(self.MOT_L_2, 100)
        
        self.front_range = 0.0
        self.rear_range = 0.0
        self.range_error = 0.0
        self.subscribe_rear_sensor_ = self.create_subscription(
            Sensor, "sensor", self.control_robot, 10)
        
        self.get_logger().info("Driving motor has been started.")

        #self.pi.set_PWM_dutycycle(self.MOT_R_1, 20)
        #self.pi.set_PWM_dutycycle(self.MOT_R_2, 0)
        #self.pi.set_PWM_dutycycle(self.MOT_L_1, 19)
        #self.pi.set_PWM_dutycycle(self.MOT_L_2, 0)

    def control_robot(self, msg):
        self.front_range = msg.front_sensor_data
        self.rear_range = msg.rear_sensor_data
        #self.get_logger().info("front_range: " + str(self.front_range))
        #self.get_logger().info("rear_range: " + str(self.rear_range))
        self.range_error = self.front_range - (self.rear_range - 1.73)
        self.get_logger().info("range_error: " + str(self.range_error))

        if 4.0 <= self.range_error < 20.0:
            self.pi.set_PWM_dutycycle(self.MOT_R_1, 0)
            self.pi.set_PWM_dutycycle(self.MOT_R_2, 0)
        elif -20.0 < self.range_error < -4.0:
            self.pi.set_PWM_dutycycle(self.MOT_L_1, 0)
            self.pi.set_PWM_dutycycle(self.MOT_L_2, 0)
        else:
            self.pi.set_PWM_dutycycle(self.MOT_R_1, 20)
            self.pi.set_PWM_dutycycle(self.MOT_R_2, 0)
            self.pi.set_PWM_dutycycle(self.MOT_L_1, 19)
            self.pi.set_PWM_dutycycle(self.MOT_L_2, 0)





def main(args=None):
    rclpy.init(args=args)
    node = DrivingMotorNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
