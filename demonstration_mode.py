# Start up - show lights running.
# When 20 is pressed - line follow until reset
# When 21 is pressed - distance avoid until reset
# Must upload:
# motors.py, rcwl_1601.py, follow_line.py,
# wall_avoid_proportional.py and this file.
# Rename this file to main.py.
from machine import Pin
from larson_scanner import larson_leds
import p_line_follower, wall_avoid_proportional
import time

button_20 = Pin(20, mode=Pin.IN, pull=Pin.PULL_UP)
button_21 = Pin(21, mode=Pin.IN, pull=Pin.PULL_UP)
larson = larson_leds()


def debounce_in(button_pin):
    # Low is pushed
    if button_pin.value == 0:
        cur_value = 0
        active = 0
        while active < 20:
            if pin.value() != cur_value:
                active +=1
            
    
while True:
    next(larson)
    if button_20.value() == 0:
        p_line_follower.run()        
    elif button_21.value() == 0:
        wall_avoid_proportional.run()
    time.sleep(0.05)
