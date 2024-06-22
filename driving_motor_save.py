#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import Sensor
import pigpio
import time

class DrivingMotorNode(Node):
    def __init__(self):
        super().__init__("driving_motor")

        self.pi = pigpio.pi()

        self.ENC_R = 25
        self.ENC_L = 4
        self.count_R = 0
        self.count_L = 0
        self.pi.set_mode(self.ENC_R, pigpio.INPUT)
        self.pi.set_pull_up_down(self.ENC_R, pigpio.PUD_UP)
        self.pi.set_mode(self.ENC_L, pigpio.INPUT)
        self.pi.set_pull_up_down(self.ENC_L, pigpio.PUD_UP)
        self.cbR = self.pi.callback(self.ENC_R, pigpio.EITHER_EDGE, self.enc_callback_R)
        self.cbL = self.pi.callback(self.ENC_L, pigpio.EITHER_EDGE, self.enc_callback_L)

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

        self.DURATION = 0.1		#制御周期（秒）
        self.prev_count_R = 0	#前回カウント
        self.prev_count_L = 0
        self.err_prev_R = 0		#前回誤差
        self.err_prev_L = 0
        self.err_I_R = 0		    #誤差の積分
        self.err_I_L = 0
        self.Kp = 20			    #比例ゲイン20
        self.Ki = 50		    #積分ゲイン100
        self.Kd = 0.1		    #微分ゲイン0.1
        self.target_speed_R = 0.1	#目標速度
        self.target_speed_L = 0.1
        
        self.front_range = 0.0
        self.rear_range = 0.0
        self.range_error = 0.0
        self.subscribe_rear_sensor_ = self.create_subscription(
            Sensor, "sensor", self.calculate_robot_angle, 10)
        
        self.get_logger().info("Driving motor has been started.")

        self.pi.set_PWM_dutycycle(self.MOT_R_1, 20)
        self.pi.set_PWM_dutycycle(self.MOT_R_2, 0)
        self.pi.set_PWM_dutycycle(self.MOT_L_1, 19)
        self.pi.set_PWM_dutycycle(self.MOT_L_2, 0)
        #time.sleep(1.0)

        #self.control_loop_timer_ = self.create_timer(self.DURATION, self.drive)

        #time.sleep(20)
        #self.control_loop_timer_.cancel()
        #self.pi.set_PWM_dutycycle(self.MOT_R_1, 0)
        #self.pi.set_PWM_dutycycle(self.MOT_R_2, 0)
        #self.pi.set_PWM_dutycycle(self.MOT_L_1, 0)
        #self.pi.set_PWM_dutycycle(self.MOT_L_2, 0)

    
    def enc_callback_R(self,gpio,level, tick):
        self.count_R
        self.count_R += 1
    
    def enc_callback_L(self,gpio,level, tick):
        self.count_L
        self.count_L += 1

    def drive(self):	#0.1秒ごとに実行
        self.count_R
        self.count_L
        self.prev_count_R
        self.prev_count_L
        self.err_I_R
        self.err_I_L
        self.err_prev_R
        self.err_prev_L
        
        speed_R = (self.count_R - self.prev_count_R)/40/self.DURATION
        err_P = self.target_speed_R - speed_R
        self.err_I_R += err_P * self.DURATION
        err_D = (err_P - self.err_prev_R)/self.DURATION
        duty_R = self.Kp * err_P + self.Ki * self.err_I_R + self.Kd * err_D
        if duty_R > 0:
            if duty_R > 30.0:
                duty_R = 30.0
            self.pi.set_PWM_dutycycle(self.MOT_R_1, duty_R)
            self.pi.set_PWM_dutycycle(self.MOT_R_2, 0)
        else:
            pass
        self.prev_count_R = self.count_R
        self.err_prev_R = err_P
        
        speed_L = (self.count_L - self.prev_count_L)/40/self.DURATION
        err_P = self.target_speed_L - speed_L
        self.err_I_L += err_P * self.DURATION
        err_D = (err_P - self.err_prev_L)/self.DURATION
        duty_L = self.Kp * err_P + self.Ki * self.err_I_L + self.Kd * err_D
        if duty_L > 0:
            if duty_L > 30.0:
                duty_L = 30.0
            self.pi.set_PWM_dutycycle(self.MOT_L_1, duty_L)
            self.pi.set_PWM_dutycycle(self.MOT_L_2, 0)
        else:
            pass
        self.prev_count_L = self.count_L
        self.err_prev_L = err_P



    
    def calculate_robot_angle(self, msg):
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
