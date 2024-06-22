import pigpio
import time

MOT_R_1 = 23
MOT_R_2 = 22
MOT_L_1 = 18
MOT_L_2 = 17

pi = pigpio.pi()

pi.set_mode(MOT_R_1, pigpio.OUTPUT)
pi.set_mode(MOT_R_2, pigpio.OUTPUT)
pi.set_mode(MOT_L_1, pigpio.OUTPUT)
pi.set_mode(MOT_L_2, pigpio.OUTPUT)
pi.set_PWM_frequency(MOT_R_1, 1000)
pi.set_PWM_frequency(MOT_R_2, 1000)
pi.set_PWM_frequency(MOT_L_1, 1000)
pi.set_PWM_frequency(MOT_L_2, 1000)
pi.set_PWM_range(MOT_R_1, 100)
pi.set_PWM_range(MOT_R_2, 100)
pi.set_PWM_range(MOT_L_1, 100)
pi.set_PWM_range(MOT_L_2, 100)


pi.set_PWM_dutycycle(MOT_R_1, 20)
pi.set_PWM_dutycycle(MOT_R_2, 0)

time.sleep(3)

pi.set_PWM_dutycycle(MOT_R_1, 0)
pi.set_PWM_dutycycle(MOT_R_2, 0)

time.sleep(3)

pi.set_PWM_dutycycle(MOT_L_1, 20)
pi.set_PWM_dutycycle(MOT_L_2, 0)

time.sleep(3)

pi.set_PWM_dutycycle(MOT_L_1, 0)
pi.set_PWM_dutycycle(MOT_L_2, 0)

time.sleep(3)

pi.set_PWM_dutycycle(MOT_R_1, 0)
pi.set_PWM_dutycycle(MOT_R_2, 20)

time.sleep(3)

pi.set_PWM_dutycycle(MOT_R_1, 0)
pi.set_PWM_dutycycle(MOT_R_2, 0)

time.sleep(3)

pi.set_PWM_dutycycle(MOT_L_1, 0)
pi.set_PWM_dutycycle(MOT_L_2, 20)

time.sleep(3)

pi.set_PWM_dutycycle(MOT_L_1, 0)
pi.set_PWM_dutycycle(MOT_L_2, 0)

pi.stop()