from machine import ADC, Pin
import time
import motors

line_in = ADC(Pin(27, Pin.IN))
btn_20 = Pin(20, mode=Pin.IN, pull=Pin.PULL_UP)

class PID:
    def __init__(self, kp=0.1, ki=0, kd=0, d_filter_gain=0.1):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.d_filter_gain = d_filter_gain
        self.integral = 0
        self.error_prev = 0
    
    def calculate(self, error, dt):
        self.integral += error * dt
        difference = (error - self.error_prev) * self.d_filter_gain
        return self.kp * error + self.ki * self.integral + self.kd * difference


print("Waiting to go...")
#while btn_20.value() == 1:
    #time.sleep(0.1)

speed = 0.3
line_pid = PID(0.2)
current_time = time.ticks_ms()
scale_factor = 1/32768
try:
    while True:
        last_time = current_time
        line_error = (line_in.read_u16() - 32768) * scale_factor
        current_time = time.ticks_ms()
        dt = time.ticks_diff(current_time,last_time)
        output = line_pid.calculate(line_error, dt)
        print(line_error, output, speed + output, speed - output)
        motors.set_speed(motors.left, speed + output)
        motors.set_speed(motors.right, speed - output)
        time.sleep(0.1)
finally:
    motors.stop_all()
