from machine import Pin
import time

enc1 = Pin(8, Pin.IN)
enc2 = Pin(22, Pin.IN)


class Encoder:
    def __init__(self, pin_number):
        self.pin = Pin(pin_number, Pin.IN)
        # self.last = self.pin.value()
        self.count = 0
        self.pin.irq(self.incr, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)

    def incr(self, _):
        self.count += 1


encl = Encoder(8)
encr = Encoder(22)

while True:
    print(encl.count, encr.count)
    time.sleep(0.1)
