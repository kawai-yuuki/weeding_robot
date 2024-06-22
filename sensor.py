import pigpio
import time

HC_SR04_trig = 5
HC_SR04_echo = 6

pi = pigpio.pi()
pi.set_mode(HC_SR04_trig, pigpio.OUTPUT)
pi.set_mode(HC_SR04_echo, pigpio.INPUT)

t_rise = 0
t_fall = 0
d = 0


def cbf(gpio, level, tick):  # call back function for pulse detect _/~~\__
    global t_rise, t_fall, d

    if (level == 1):  # right after the rising edge
        t_rise = tick
    else:            # right after the falling edge
        t_fall = tick
        if (t_fall >= t_rise):  # if wrapped 32bit value,
            timepassed = t_fall - t_rise
        else:
            timepassed = t_fall + (0xffffffff + 1 - t_rise)

        # meter to cm, microseconds to seconds, divide by 2
        d = 340 * 100 * timepassed / 1000000 / 2
        #print('"distance_cm": %.2f' % (d))

def print_d(d):
    print('"distance_cm": %.2f' % (d))
    time.sleep(0.2)

 
if __name__ == '__main__':
    try:
        while True:
            cb = pi.callback(HC_SR04_echo, pigpio.EITHER_EDGE, cbf)
            pi.gpio_trigger(HC_SR04_trig, 10, 1)  # Trig (10μs pulse)
            print_d(d)
            time.sleep(0.2)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        pi.stop()
