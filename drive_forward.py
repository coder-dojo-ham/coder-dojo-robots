import time
from motors import Motor

motor_1 = Motor(1, 0)
motor_2 = Motor(2, 3)

try:
    motor_1.drive(0.3)
    motor_2.drive(0.1)
    time.sleep(0.5)
finally:
    motor_1.stop()
    motor_2.stop()
