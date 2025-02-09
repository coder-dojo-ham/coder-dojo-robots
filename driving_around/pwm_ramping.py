# motor test
from machine import Pin, PWM
import time

motor_l_forward = PWM(Pin(8), freq=2000)
motor_l_back = PWM(Pin(9), freq=2000)
motor_r_forward = PWM(Pin(11), freq=2000)
motor_r_back = PWM(Pin(10), freq=2000)

print("PWM ramp")
for n in range(0, 11):
    duty = int(65535 * n / 10)
    motor_l_forward.duty_u16(duty)
    motor_r_forward.duty_u16(duty)
    time.sleep(0.5)
motor_l_forward.duty_u16(0)
motor_r_forward.duty_u16(0)
