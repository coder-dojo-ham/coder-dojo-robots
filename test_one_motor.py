from machine import Pin
import time

ml1 = Pin(0, Pin.OUT)
ml2 = Pin(1, Pin.OUT)

try:
    ml1.value(0)
    ml2.value(1)
    time.sleep(0.5)
finally:
    ml1.value(0)
    ml2.value(0)
