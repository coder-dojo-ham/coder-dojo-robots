from machine import Pin, PWM

MAX_SPEED = 2 ** 16 - 1

motor_l_forward = PWM(Pin(8), freq=2000)
motor_l_back = PWM(Pin(9), freq=2000)
motor_r_forward = PWM(Pin(11), freq=2000)
motor_r_back = PWM(Pin(10), freq=2000)

left = motor_l_forward, motor_l_back
right = motor_r_forward, motor_r_back

def stop(motor):
    motor[0].duty_u16(0)
    motor[1].duty_u16(0)

def set_speed(motor, speed):
    if speed < 0:
        motor = motor[1], motor[0]
        speed = -speed
    motor[0].duty_u16(int(speed * MAX_SPEED))
    motor[1].duty_u16(0)

def stop_all():
    stop(left)
    stop(right)
