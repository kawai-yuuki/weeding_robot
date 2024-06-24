#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import RearSensor
import pigpio

class RearSensorNode(Node):
    def __init__(self):
        super().__init__("rear_sensor")
        self.declare_parameter("HC_SR04_trig", 5)
        self.declare_parameter("HC_SR04_echo", 6)
        self.declare_parameter("publish_frequency", 2.0)

        self.HC_SR04_trig_ = self.get_parameter("HC_SR04_trig").value
        self.HC_SR04_echo_ = self.get_parameter("HC_SR04_echo").value
        self.publish_frequency_ = self.get_parameter("publish_frequency").value

        self.pi = pigpio.pi()
        self.pi.set_mode(self.HC_SR04_trig_, pigpio.OUTPUT)
        self.pi.set_mode(self.HC_SR04_echo_, pigpio.INPUT)

        self.t_rise = 0
        self.t_fall = 0
        self.d = 0.0

        self.lenge_publisher_ = self.create_publisher(
            RearSensor, "rear_sensor", 10)
        self.number_timer_ = self.create_timer(
            1.0 / self.publish_frequency_, self.publish_lenge)
        self.get_logger().info("rear sensor has been started.")

    def cbf(self, gpio, level, tick):  # call back function for pulse detect _/~~\__
        #global t_rise, t_fall, d

        if (level == 1):  # right after the rising edge
            self.t_rise = tick
        else:            # right after the falling edge
            self.t_fall = tick
            if (self.t_fall >= self.t_rise):  # if wrapped 32bit value,
                timepassed = self.t_fall - self.t_rise
            else:
                timepassed = self.t_fall + (0xffffffff + 1 - self.t_rise)

            # meter to cm, microseconds to seconds, divide by 2
            self.d = 340 * 100 * timepassed / 1000000 / 2
            #print('"distance_cm": %.2f' % (d))

    def publish_lenge(self):
        cb = self.pi.callback(self.HC_SR04_echo_, pigpio.EITHER_EDGE, self.cbf)
        self.pi.gpio_trigger(self.HC_SR04_trig_, 10, 1)  # Trig (10μs pulse)
        msg = RearSensor()
        msg.rear_sensor_data = self.d
        self.lenge_publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = RearSensorNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
