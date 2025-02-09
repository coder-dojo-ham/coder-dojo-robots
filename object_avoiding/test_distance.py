# test distance sensors
import time

from hcsr04 import HCSR04

right_sensor = HCSR04(trigger_pin=0, echo_pin=1)
left_sensor = HCSR04(trigger_pin=7, echo_pin=28)

while True:
    left_distance = right_sensor.distance_cm()
    right_distance = left_sensor.distance_cm()
    print(left_distance, right_distance)
    time.sleep(0.1)
