import robot
import rcwl_1601
import time

left_sensor = rcwl_1601.RCWL1601(4, 5)
right_sensor = rcwl_1601.RCWL1601(6, 7)


speed = 0.5
turn_distance_cm = 5

try:
    while True:
        if left_sensor.distance_cm() < turn_distance_cm:
            robot.set_speed(0, speed)
            robot.set_speed(1, -speed)
        elif right_sensor.distance_cm() < turn_distance_cm:
            robot.set_speed(0, -speed)
            robot.set_speed(1, speed)
        else:
            robot.set_speed(0, speed)
            robot.set_speed(1, speed)
        time.sleep(0.01)
except:
    robot.stop()
