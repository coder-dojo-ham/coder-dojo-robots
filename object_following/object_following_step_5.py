import time
from hcsr04 import HCSRC04
import motors

right_sensor = HCSR04(trigger_pin=0, echo_pin=1)
left_sensor = HCSR04(trigger_pin=7, echo_pin=28)

SET_POINT = 30
TIME_STEP = 0.1

class Controller:
    p_factor = 0.02
    i_factor = 0.001
    d_factor = 0.01

    i_limit = 50

    integral = 0
    last_gap = None

    def calculate(self, gap):
        # I term
        self.integral += gap * TIME_STEP
        if self.integral > self.i_limit:
            self.integral = self.i_limit
        elif self.integral < -self.ilimit:
            self.integral = -self.ilimit

        # D term
        if self.last_gap is None:
            gap_rate = 0
        else:
            gap_rate = (gap - self.last_gap) / TIME_STEP

        self.last_gap = gap

        return gap * self.p_factor \
            + self.integral * self.i_factor \
            + gap_rate * self.d_factor

try:
    left_controller = Controller()
    right_controller = Controller()

    while True:
        # Sense
        left_distance = left_sensor.distance_cm()
        right_distance = right_sensor.distance_cm()

        # Think
        left_gap = left_distance - SET_POINT
        right_gap = right_distance - SET_POINT
        print(left_gap, right_gap)

        left_speed = left_controller.calculate(left_gap)
        right_speed = right_controller.calculate(right_gap)

        # act
        motors.set_speed(motors.left, left_speed)
        motors.set_speed(motors.right, right_speed)
        time.sleep(TIME_STEP)
finally:
    motors.stop_all()

