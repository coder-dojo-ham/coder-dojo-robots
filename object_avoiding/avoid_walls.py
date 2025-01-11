# Install https://github.com/rsc1975/micropython-hcsr04/blob/master/hcsr04.py into a lib folder.

from machine import Pin, PWM
import time
from hcsr04 import HCSR04
import motors

right_sensor = HCSR04(trigger_pin=0, echo_pin=1)
left_sensor = HCSR04(trigger_pin=7, echo_pin=28)

speed = 0.5
turn_speed = 0.3
threshold = 30

try:
    while True:
        # Sense
        left_distance = left_sensor.distance_cm()
        right_distance = right_sensor.distance_cm()
        print('Left:', left_distance, 'cm', 'Right:', right_distance, 'cm')
        # Think
        left_speed = speed
        right_speed = speed
        if left_distance < threshold:
            right_speed = -turn_speed
        elif right_distance < threshold:
            left_speed = -turn_speed
        # act
        motors.set_speed(motors.left, left_speed)
        motors.set_speed(motors.right, right_speed)
        time.sleep(0.01)
finally:
    motors.stop_all()
