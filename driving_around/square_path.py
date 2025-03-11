import time
import motors

def straight(speed, duration):
    motors.set_speed(motors.left, speed)
    motors.set_speed(motors.right, speed)
    time.sleep(duration)


def left(speed, duration):
    motors.set_speed(motors.left, 0)
    motors.set_speed(motors.right, speed)
    time.sleep(duration)

try:
    for n in range(4):
        straight(0.6, 1.0)
        left(0.6, 1.0)
finally:
    motors.stop_all()
