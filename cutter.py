import pigpio                           #pigpio （RaspiのGPIOを使うためのライブラリ）を使う
from time import sleep                  #sleepを使う

MOT_R_1 = 19                            #GPIO18をMOT_R_1と命名

pi = pigpio.pi()
pi.set_mode(MOT_R_1, pigpio.OUTPUT)     #MOT_R_1を出力指定

pi.hardware_PWM(MOT_R_1, 60, 80000)
#音が鳴る（鳴らないと動かない。基準値を決めるための校正？）
sleep(0.5)

#pi.hardware_PWM(MOT_R_1, 60, 78000)
#sleep(0.5)
duty_array = [78000, 77000, 76000, 75000, 74000, 73000, 72000, 71000]
for i in range(len(duty_array)):
    pi.hardware_PWM(MOT_R_1, 60, duty_array[i])
    sleep(0.2)

sleep(3) #5秒待つ

pi.set_mode(MOT_R_1, pigpio.INPUT)
pi.stop()
