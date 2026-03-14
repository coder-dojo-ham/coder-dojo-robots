import time
from hcsr04 import HCSRC04
import motors

right_sensor = HCSR04(trigger_pin=0, echo_pin=1)
left_sensor = HCSR04(trigger_pin=7, echo_pin=28)

THRESHOLD = 30
SPEED = 0.7

try:
    motors.set_speed(motors.left, SPEED)
    motors.set_speed(motors.right, SPEED)

    while True:

        # Sense
        left_distance = left_sensor.distance_cm()
        right_distance = right_sensor.distance_cm()

        # Think
        if left_distance < THRESHOLD or \
            right_distance < THRESHOLD:
            # act
            break
        time.sleep(0.1)
finally:
    motors.stop_all()

