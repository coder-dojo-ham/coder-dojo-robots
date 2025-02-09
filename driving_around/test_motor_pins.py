from machine import Pin
import time

motor_l_forward = Pin(8, Pin.OUT)
motor_l_back = Pin(9, Pin.OUT)
motor_r_forward = Pin(11, Pin.OUT)
motor_r_back = Pin(10, Pin.OUT)

try:
    print("Left")
    motor_l_forward.on()
    time.sleep(0.5)
    motor_l_forward.off()
    motor_l_back.on()
    time.sleep(0.5)
    motor_l_back.off()
    time.sleep(0.5)

    print("Right")
    motor_r_forward.on()
    time.sleep(0.5)
    motor_r_forward.off()
    motor_r_back.on()
    time.sleep(0.5)
    motor_r_back.off()
finally:
    motor_l_forward.off()
    motor_l_back.off()
    motor_r_forward.off()
    motor_l_back.off()
