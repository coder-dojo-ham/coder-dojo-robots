from machine import Pin
import time

motor_forward = Pin(10, Pin.OUT)
motor_back = Pin(11, Pin.OUT)

try:
    motor_forward.on()
    time.sleep(0.5)
    motor_forward.off()
    motor_back.on()
    time.sleep(0.5)
finally:
    motor_forward.off()
    motor_back.off()
