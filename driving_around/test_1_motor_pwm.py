import time
from machine import Pin, PWM
PWM_MAX = 65025

# using 2 pwm pins is simpler - due to the negative PWM gap.
pwm1 = PWM(Pin(1, Pin.OUT))
ml2 = Pin(0, Pin.OUT)

try:
    pwm1.duty_u16(int(PWM_MAX * (0.3)))
    ml2.value(0)
    time.sleep(0.5)
finally:
    pwm1.duty_u16(0)
    ml2.value(0)
