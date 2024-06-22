import pigpio
pi = pigpio.pi()

#PWMパラメータ
pwm_pin1 = 12 #PWM出力ピンを指定

duty1 = 70 #デューティー比を%で指定

freq = 60 #PWM周波数をHzで指定

#パラメータ変換
cnv_dutycycle1 = int((duty1 * 1000000 / 100))


#PWMを出力
pi.hardware_PWM(pwm_pin1, freq, cnv_dutycycle1)
