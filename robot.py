from machine import Pin, PWM
PWM_MAX = 65025

class Motor:
    def __init__(self, pin1, pin2):
        self.pin1 = Pin(pin1, Pin.OUT)
        self.pin2 = Pin(pin2, Pin.OUT)
        self.m1 = PWM(self.pin1)
        self.m2 = PWM(self.pin2)
        
    def stop(self):
        self.m2.duty_u16(0)
        self.m1.duty_u16(0)
    
    def drive(self, speed):
        if speed > 0:
            self.m1.duty_u16(int(PWM_MAX * speed))
            self.m2.duty_u16(0)
        if speed < 0:
            self.m2.duty_u16(int(PWM_MAX * -speed))
            self.m1.duty_u16(0)

motors = [
    Motor(0, 1),
    Motor(2, 3)
]

def set_speed(motor, speed):
    motors[motor].drive(speed)

def stop():
    for motor in motors:
        motor.stop()
