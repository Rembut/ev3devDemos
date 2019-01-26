from ev3dev2.button import Button
from time import sleep

btn = Button()

while True:
    print(btn.buttons_pressed)
    sleep(0.5)

