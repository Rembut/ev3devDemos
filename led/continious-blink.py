from ev3dev2.led import Leds
from time import sleep

l = Leds()
d = 5

while True:
    for c in range(0, d):
        l.set_color('LEFT', (c/d, 1-c/d))
        l.set_color('RIGHT', (1-c/d, c/d))
        sleep(0.05)
    for c in range(d, 0, -1):
        l.set_color('LEFT', (c/d, 1-c/d))
        l.set_color('RIGHT', (1-c/d, c/d))
        sleep(0.05)
