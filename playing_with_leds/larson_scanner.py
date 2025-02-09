from machine import Pin
import time


def larson_leds():
    current_direction = 1
    current_position = 1
    position_led_range = list(range(0, 8)) + [16, 17, 26, 27, 28]
    position_leds = [Pin(led, Pin.OUT) for led in position_led_range]
    highest_position = len(position_leds) - 1
    while True:
        if not 0 < current_position < highest_position:
            current_direction = -current_direction
        position_leds[current_position].value(0)
        current_position += current_direction
        position_leds[current_position].value(1)
        yield


if __name__ == "__main__":
    larson = larson_leds()
    while True:
        next(larson)
        time.sleep(0.1)
