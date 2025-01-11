from machine import Pin
from neopixel import NeoPixel
import time

leds = NeoPixel(Pin(18, Pin.OUT),2)
leds[0] = (255, 0, 255)
leds[1] = (0, 255, 0)
leds.write()

time.sleep(2)
leds[0] = (0, 0, 0)
leds[1] = (0, 0, 0)
leds.write()

try:
    for n in range(50):
        leds[0] = (255, 0, 0)
        leds[1] = (0, 0, 255)
        leds.write()
        time.sleep(0.5)
        leds[1] = (255, 0, 0)
        leds[0] = (0, 0, 255)
        leds.write()
        time.sleep(0.5)
finally:
    leds[0] = (0, 0, 0)
    leds[1] = (0, 0, 0)
    leds.write()
