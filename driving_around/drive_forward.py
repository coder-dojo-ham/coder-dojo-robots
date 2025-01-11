import motors
import time

try:
    motors.set_speed(motors.left, 0.7)
    motors.set_speed(motors.right, 0.7)
    time.sleep(0.4)
finally:
    motors.stop_all()