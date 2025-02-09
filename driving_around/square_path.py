import time
import motors
from machine import Pin


def straight(speed, duration):
    motors.set_speed(motors.left, speed)
    motors.set_speed(motors.right, speed)
    time.sleep(duration)


def left(speed, duration):
    motors.set_speed(motors.left, 0)
    motors.set_speed(motors.right, speed)
    time.sleep(duration)


btn_20 = Pin(20, mode=Pin.IN, pull=Pin.PULL_UP)

while True:
    try:
        print("Waiting to go...")
        while btn_20.value() == 1:
            time.sleep(0.1)

        print("Go!")
        for n in range(4):
            straight(0.6, 1.0)
            left(0.6, 1.0)
        motors.stop_all()

    finally:
        motors.stop_all()
