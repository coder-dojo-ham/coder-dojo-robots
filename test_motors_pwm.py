import time
from motors import Motor

motor_1 = Motor(1, 0)

try:
    motor_1.drive(0.3)
    time.sleep(0.5)
finally:
    motor_1.stop()
