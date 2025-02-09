import time
from machine import Pin
from hcsr04 import HCSR04
import motors


SPEED = 0.5
PROPORTION = 0.02
SET_POINT = 50.0

class Proportional:
    def __init__(self, proportion):
        self.kp = proportion

    def calculate(self, error):
        return self.kp * error

def limit(value, min_value=-1.0, max_value=1.0):
    return max(min(value, max_value), min_value)

def run():
    corrector = Proportional(PROPORTION)
    right_sensor = HCSR04(trigger_pin=0, echo_pin=1)
    left_sensor = HCSR04(trigger_pin=7, echo_pin=28)

    try:
        while True:
            # Error for each side, - will be higher as we get closer past the set point.
            left_error = max(0, SET_POINT - left_sensor.distance_cm())
            right_error = max(0, SET_POINT - right_sensor.distance_cm())
            # get the balance - positive result, too close to the left, negative is too close to the right
            balance_error = left_error - right_error
            # If we are balanced, then use the absolute left error, so we don't get stuck in corners
            if abs(balance_error) <= 5:
               balance_error = left_error
            # Use the balance to get an error value
            correction = corrector.calculate(balance_error)            
            print(
                "Left e:",
                left_error,
                "Right e:",
                right_error,
                "Balance e:",
                balance_error,
                "Correction:",
                correction,
                "Left m:", limit(SPEED + correction),
                "Right m:", limit(SPEED - correction),
            )
            motors.set_speed(motors.left, limit(SPEED + correction))
            motors.set_speed(motors.right, limit(SPEED - correction))
            time.sleep(0.05)
    finally:
            motors.stop_all()


if __name__ == "__main__":
    button_a = Pin(20, mode=Pin.IN, pull=Pin.PULL_UP)
    while button_a.value() != 0:
        time.sleep(0.05)
    run()


