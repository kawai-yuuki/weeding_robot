#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import Sensor
import pigpio

class SensorNode(Node):
    def __init__(self):
        super().__init__("sensor")
        self.declare_parameter("HC_SR04_trig_f", 20)
        self.declare_parameter("HC_SR04_echo_f", 21)
        self.declare_parameter("HC_SR04_trig_r", 5)
        self.declare_parameter("HC_SR04_echo_r", 6)
        self.declare_parameter("publish_frequency_", 4.0)

        self.HC_SR04_trig_f = self.get_parameter("HC_SR04_trig_f").value
        self.HC_SR04_echo_f = self.get_parameter("HC_SR04_echo_f").value
        self.HC_SR04_trig_r = self.get_parameter("HC_SR04_trig_r").value
        self.HC_SR04_echo_r = self.get_parameter("HC_SR04_echo_r").value
        self.publish_frequency_ = self.get_parameter("publish_frequency_").value

        self.pi = pigpio.pi()
        self.pi.set_mode(self.HC_SR04_trig_f, pigpio.OUTPUT)
        self.pi.set_mode(self.HC_SR04_echo_f, pigpio.INPUT)
        self.pi.set_mode(self.HC_SR04_trig_r, pigpio.OUTPUT)
        self.pi.set_mode(self.HC_SR04_echo_r, pigpio.INPUT)

        self.t_rise_f = 0
        self.t_fall_f = 0
        self.d_f = 0.0
        self.t_rise_r = 0
        self.t_fall_r = 0
        self.d_r = 0.0

        self.lenge_publisher_ = self.create_publisher(
            Sensor, "sensor", 10)
        self.number_timer_ = self.create_timer(
            1.0 / self.publish_frequency_, self.publish_lenge)
        self.get_logger().info("sensor has been started.")

    def cbf_f(self, gpio, level, tick):  # call back function for pulse detect _/~~\__
        #global t_rise, t_fall, d

        if (level == 1):  # right after the rising edge
            self.t_rise_f = tick
        else:            # right after the falling edge
            self.t_fall_f = tick
            if (self.t_fall_f >= self.t_rise_f):  # if wrapped 32bit value,
                timepassed_f = self.t_fall_f - self.t_rise_f
            else:
                timepassed_f = self.t_fall_f + (0xffffffff + 1 - self.t_rise_f)

            # meter to cm, microseconds to seconds, divide by 2
            self.d_f = 340 * 100 * timepassed_f / 1000000 / 2
            #print('"distance_cm": %.2f' % (d))

    def cbf_r(self, gpio, level, tick):
        if (level == 1):  # right after the rising edge
            self.t_rise_r = tick
        else:            # right after the falling edge
            self.t_fall_r = tick
            if (self.t_fall_r >= self.t_rise_r):  # if wrapped 32bit value,
                timepassed_r = self.t_fall_r - self.t_rise_r
            else:
                timepassed_r = self.t_fall_r + (0xffffffff + 1 - self.t_rise_r)

            # meter to cm, microseconds to seconds, divide by 2
            self.d_r = 340 * 100 * timepassed_r / 1000000 / 2
            #print('"distance_cm": %.2f' % (d))

    def publish_lenge(self):
        cb_f = self.pi.callback(self.HC_SR04_echo_f, pigpio.EITHER_EDGE, self.cbf_f)
        self.pi.gpio_trigger(self.HC_SR04_trig_f, 10, 1)  # Trig (10μs pulse)
        cb_r = self.pi.callback(self.HC_SR04_echo_r, pigpio.EITHER_EDGE, self.cbf_r)
        self.pi.gpio_trigger(self.HC_SR04_trig_r, 10, 1)  # Trig (10μs pulse)
        msg = Sensor()
        msg.front_sensor_data = self.d_f
        msg.rear_sensor_data = self.d_r
        self.lenge_publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
