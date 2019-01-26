from ev3dev2.led import Leds
from time import sleep

l = Leds()

while True:
    for c in ['BLACK', 'RED', 'AMBER', 'GREEN', 'ORANGE', 'YELLOW']:
        for s in ['LEFT', 'RIGHT']:
            l.set_color(s, c)
        sleep(0.3)

