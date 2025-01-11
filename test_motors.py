from machine import Pin
import time

ml1 = Pin(0, Pin.OUT)
ml2 = Pin(1, Pin.OUT)
mr1 = Pin(2, Pin.OUT)
mr2 = Pin(3, Pin.OUT)

try:
    ml1.value(1)
    time.sleep(0.5)
    ml1.value(0)
    ml2.value(1)

    time.sleep(0.5)
    ml2.value(0)
    mr1.value(1)
    time.sleep(0.5)
    mr1.value(0)
    mr2.value(1)
    time.sleep(0.5)
finally:
    ml1.value(0)
    ml2.value(0)
    mr1.value(0)
    mr2.value(0)
