import time
import robot

try:
    while True:
        robot.set_speed(1, 1)
        time.sleep(0.5)
        robot.stop()
        robot.set_speed(0, 1)
        time.sleep(0.5)
        robot.stop()
finally:
    robot.stop()
 