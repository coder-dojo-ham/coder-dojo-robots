from machine import ADC, Pin
import time
import motors


SENSOR_MID = 2 ** 15
# Normalise to -1.0 to 1.0
SENSOR_SCALE = 1 / SENSOR_MID
SPEED = 0.3
# How much to correct motors by
PROPORTION = 0.2

class Proportional:
    def __init__(self, proportion):
        self.kp = proportion

    def calculate(self, error):
        return self.kp * error

def read_sensor(line_in):
    raw = line_in.read_u16()
    mid = raw - SENSOR_MID
    scaled = mid * SENSOR_SCALE
    return scaled


def run():
    line_in = ADC(Pin(27, Pin.IN))
    corrector = Proportional(PROPORTION)
    try:
        while True:
            # We can directly call it an error, if it's not 0, it's not in the middle.
            error = read_sensor(line_in)
            correction = corrector.calculate(error)
            print(error, correction, SPEED + correction, SPEED - correction)
            motors.set_speed(motors.left, SPEED + correction)
            motors.set_speed(motors.right, SPEED - correction)
            time.sleep(0.1)
    finally:
        motors.stop_all()

if __name__ == "__main__":
    run()
