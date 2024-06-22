import pigpio
import threading
from time import sleep              	#sleepを使う

def enc_callback_R(gpio,level, tick):
    global count_R
    count_R += 1
    #print('R= ' + str(count_R)) 		#画面出力
    
def enc_callback_L(gpio,level, tick):
    global count_L
    count_L += 1
    #print('L= ' + str(count_L)) 		#画面出力

pi = pigpio.pi()
# encoder settings
ENC_R = 10
ENC_L = 2
count_R = 0
count_L = 0
pi.set_mode(ENC_R, pigpio.INPUT)
pi.set_pull_up_down(ENC_R, pigpio.PUD_UP)
pi.set_mode(ENC_L, pigpio.INPUT)
pi.set_pull_up_down(ENC_L, pigpio.PUD_UP)
cbR = pi.callback(ENC_R, pigpio.EITHER_EDGE, enc_callback_R)
cbL = pi.callback(ENC_L, pigpio.EITHER_EDGE, enc_callback_L)

MOT_R_1 = 18                       	    #GPIO18をMOT_R_1と命名
MOT_R_2 = 17                       	    #GPIO17をMOT_R_2と命名
MOT_L_1 = 23                       	    #GPIO23をMOT_L_1と命名
MOT_L_2 = 22                       	    #GPIO22をMOT_L_2と命名

pi.set_mode(MOT_R_1, pigpio.OUTPUT) 	#MOT_R_1を出力指定
pi.set_mode(MOT_R_2, pigpio.OUTPUT) 	#MOT_R_2を出力指定
pi.set_mode(MOT_L_1, pigpio.OUTPUT) 	#MOT_L_1を出力指定
pi.set_mode(MOT_L_2, pigpio.OUTPUT) 	#MOT_L_2を出力指定
pi.set_PWM_frequency(MOT_R_1, 60)   	#MOT_R_1に60HzでPWM出力
pi.set_PWM_frequency(MOT_R_2, 60)   	#MOT_R_2に60HzでPWM出力
pi.set_PWM_frequency(MOT_L_1, 60)   	#MOT_L_1に60HzでPWM出力
pi.set_PWM_frequency(MOT_L_2, 60)   	#MOT_L_2に60HzでPWM出力
pi.set_PWM_range(MOT_R_1, 100)      	#デューティのレンジ設定
pi.set_PWM_range(MOT_R_2, 100)
pi.set_PWM_range(MOT_L_1, 100)
pi.set_PWM_range(MOT_L_2, 100)

pi.set_PWM_dutycycle(MOT_R_1, 29)   	#MOT_R_1:20/100
pi.set_PWM_dutycycle(MOT_R_2, 0)    	#MOT_R_2:0/100
pi.set_PWM_dutycycle(MOT_L_1, 30)   	#MOT_L_1:20/100
pi.set_PWM_dutycycle(MOT_L_2, 0)    	#MOT_L_2:0/100

try:
    while True:
        pass
except KeyboardInterrupt:
    pi.set_PWM_dutycycle(MOT_R_1, 0)
    pi.set_PWM_dutycycle(MOT_R_2, 0)
    pi.set_PWM_dutycycle(MOT_L_1, 0)
    pi.set_PWM_dutycycle(MOT_L_2, 0)
    pi.stop()