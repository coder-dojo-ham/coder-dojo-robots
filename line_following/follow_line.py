from machine import Pin, PWM
import time
from motors import Motor

line_sensor = [
    Pin(10, Pin.IN),
    Pin(11, Pin.IN),
    Pin(12, Pin.IN),
    Pin(13, Pin.IN),
    Pin(14, Pin.IN)
]

SPEED = 0.4
PROPORTION = 0.1

motor_1 = Motor(1, 0)
motor_2 = Motor(2, 3)

def sensor_middle():
    outputs = []
    for n, sensor in enumerate(line_sensor):
        if sensor.value():
            outputs.append(n + 1)
    if outputs:
        return sum(outputs)/len(outputs)
    else:
        return 0

try:
    while True:
        line = sensor_middle()
        error = 3 - line
        correction = error * PROPORTION
        print(line, error, correction)
        motor_1.drive(SPEED + correction)
        motor_2.drive(SPEED - correction)
        time.sleep(0.04)
    
finally:
    motor_1.stop()
    motor_2.stop()
