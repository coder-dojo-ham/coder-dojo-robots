from machine import Pin
import time

line_1 = Pin(10, Pin.IN)
line_2 = Pin(11, Pin.IN)
line_3 = Pin(12, Pin.IN)
line_4 = Pin(13, Pin.IN)
line_5 = Pin(14, Pin.IN)

while True:
    print(line_1.value(), line_2.value(), line_3.value(), line_4.value(), line_5.value())
    time.sleep(0.1)
