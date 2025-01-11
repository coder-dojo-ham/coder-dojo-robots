from machine import ADC, Pin
import time

line_in = ADC(Pin(27, Pin.IN))

while True:
    line = line_in.read_u16()
    print(line)
    time.sleep(0.1)
