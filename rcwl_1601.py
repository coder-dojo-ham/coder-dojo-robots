from machine import Pin, time_pulse_us
from time import sleep_us

class RCWL1601:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = Pin(trigger_pin, Pin.OUT)
        self.echo_pin = Pin(echo_pin, Pin.IN)
        self.trigger_pin.value(0)
        
    us_to_cm = 0.0343 / 2

    def distance_cm(self):
        self.trigger_pin.value(0) # Stabilize the sensor
        sleep_us(20)
        # Send a pulse
        self.trigger_pin.value(1)
        sleep_us(10)
        self.trigger_pin.value(0)
        sleep_us(20)
        # Measure the time it takes to get a pulse back
        return_time =  time_pulse_us(self.echo_pin, 1, 3000)
        # Now we have the time, we can calculate the distance
        return return_time * self.us_to_cm
