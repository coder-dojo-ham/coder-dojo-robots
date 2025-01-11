import robot
import rcwl_1601
import time

left_sensor = rcwl_1601.RCWL1601(4, 5)
right_sensor = rcwl_1601.RCWL1601(6, 7)

speed = 0.5
proportional_constant = 1 / 30.0

try:
    while True:
        left_distance = left_sensor.distance_cm()
        right_distance = right_sensor.distance_cm()
        left_speed = min(1, right_distance * proportional_constant)
        right_speed = min(1, left_distance * proportional_constant)
        print("Left d:", left_distance, "Left s:", left_speed, "Right d:", right_distance, "Right s:", right_speed)
        robot.set_speed(0, right_speed)
        robot.set_speed(1, left_speed)
        time.sleep(0.05)
finally:
    robot.stop()
