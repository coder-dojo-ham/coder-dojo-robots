# motor test
from machine import Pin, PWM
import time

motor_l_forward = PWM(Pin(8), freq=2000)
motor_l_back = PWM(Pin(9), freq=2000)
motor_r_forward = PWM(Pin(11), freq=2000)
motor_r_back = PWM(Pin(10), freq=2000)

print("Left")
motor_l_forward.duty_u16(int(65535 * 0.5))
time.sleep(0.5)
motor_l_forward.duty_u16(0)
motor_l_back.duty_u16(int(65535 * 0.6))
time.sleep(0.5)
motor_l_back.duty_u16(0)
time.sleep(0.5)

print("Right")
motor_r_forward.duty_u16(int(65535 * 0.4))
time.sleep(0.5)
motor_r_forward.duty_u16(0)
motor_r_back.duty_u16(int(65535 * 0.3))
time.sleep(0.5)
motor_r_back.duty_u16(0)
