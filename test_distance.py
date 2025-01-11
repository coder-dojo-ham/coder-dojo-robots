# test distance sensors
from machine import Pin
import time

from hcsr04 import HCSR04

left_distance_sensor = HCSR04(4, 5)
right_distance_sensor = HCSR04(6, 7)

while True:
    left_distance = left_distance_sensor.distance_mm()
    right_distance = right_distance_sensor.distance_mm()
    print(left_distance, right_distance)
    time.sleep(0.1)
