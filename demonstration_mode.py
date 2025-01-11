# Start up - show lights running.
# When A is pressed - line follow until reset
# When B is pressed - distance avoid until reset
# Must upload:
# motors.py, rcwl_1601.py, follow_line.py, wall_avoid_proportional.py and this file.
# Rename this file to main.py.
from machine import Pin
import time

button_a = Pin(20)
button_b = Pin(21)

def larson_leds():
    current_direction = 1
    current_position = 0
    position_led_range = list(range(0, 8)) + [16, 17, 26, 27, 28]
    position_leds = [Pin(l, Pin.OUT) for l in position_led_range]
    highest_position = len(position_leds) - 1
    while True:
        if not 0 < current_position < highest_position:
            current_direction = -current_direction
        position_leds[current_position].value(0)
        current_position += current_direction        
        position_leds[current_position].value(1)
        yield
        
while True:
    if button_a.value() == 1:
        import line_following.follow_line as follow_line
    elif button_b.value() == 1:
        import object_avoiding.wall_avoid_proportional as wall_avoid_proportional
    time.sleep(0.01)
