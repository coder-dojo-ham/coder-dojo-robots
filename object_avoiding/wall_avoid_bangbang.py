# Install https://github.com/rsc1975/micropython-hcsr04/blob/master/hcsr04.py
# into a lib folder.

import time
from hcsr04 import HCSR04
import motors

right_sensor = HCSR04(trigger_pin=0, echo_pin=1)
left_sensor = HCSR04(trigger_pin=7, echo_pin=28)

SPEED = 0.5
TURN_SPEED = 0.3
THRESHOLD = 30

def run():
    try:
        while True:
            # Sense
            left_distance = left_sensor.distance_cm()
            right_distance = right_sensor.distance_cm()
            print("Left:", left_distance, "cm", "Right:", right_distance, "cm")
            # Think
            left_speed = SPEED
            right_speed = SPEED
            if left_distance < THRESHOLD:
                right_speed = -TURN_SPEED
            elif right_distance < THRESHOLD:
                left_speed = -TURN_SPEED
            # act
            motors.set_speed(motors.left, left_speed)
            motors.set_speed(motors.right, right_speed)
            time.sleep(0.01)
    finally:
        motors.stop_all()


if __name__ == "__main__":
    run()
