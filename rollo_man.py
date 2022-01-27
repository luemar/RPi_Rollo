#!/usr/bin/python3
from gpiozero import Button, LED
from signal import pause
import time
import logging

logging.basicConfig(filename='/home/pi/mylog1.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
 13                      level=logging.INFO)


btn1 = Button(17, hold_time = 1)
btn2 = Button(22, hold_time = 1)
btn3 = Button(27)
btn4 = Button(5)
btn5 = Button(6, hold_time = 1)
btn6 = Button(19, hold_time = 1)
btn7 = Button(13)
btn8 = Button(26)

led1 = LED(18)
led2 = LED(23)
led3 = LED(24)
led4 = LED(25)

Button.was_held = False

def held_li_up(btn1):
    print("button li up held")
    Button.was_held = True
    led1.on()
    time.sleep(18)
    led1.off()

def released_li_up(btn1):
    if not btn1.was_held:
        Button.was_held = False

btn1.when_held = held_li_up
btn1.when_released = released_li_up

def held_li_down(btn2):
    print("button li down held")
    Button.was_held = True
    led2.on()
    time.sleep(18)
    led2.off()

def released_li_down(btn2):
    if not btn1.was_held:
        Button.was_held = False

btn2.when_held = held_li_down
btn2.when_released = released_li_down

def held_re_up(btn5):
    print("button re up held")
    Button.was_held = True
    led3.on()
    time.sleep(18)
    led3.off()

def released_re_up(btn5):
    if not btn5.was_held:
        Button.was_held = False

btn5.when_held = held_re_up
btn5.when_released = released_re_up

def held_re_down(btn6):
    print("button re down held")
    Button.was_held = True
    led4.on()
    time.sleep(18)
    led4.off()
def released_re_down(btn6):
    if not btn6.was_held:
        Button.was_held = False

btn6.when_held = held_re_down
btn6.when_released = released_re_down

def on_up_li():
    print("button li up pressed")
    led1.on()

def off_up_li():
    print("button li up released")
    led1.off()

def on_down_li():
    print("button li down pressed")
    led2.on()

def off_down_li():
    print("button li down released")
    led2.off()

btn3.when_pressed = on_up_li
btn3.when_released = off_up_li
btn4.when_pressed = on_down_li
btn4.when_released = off_down_li

def on_up_re():
    print("button re up pressed")
    led3.on()

def off_up_re():
    print("button re up released")
    led3.off()

def on_down_re():
    print("button re down pressed")
    led4.on()

def off_down_re():
    print("button re down released")
    led4.off()

btn7.when_pressed = on_up_re
btn7.when_released = off_up_re
btn8.when_pressed = on_down_re
btn8.when_released = off_down_re

print("Init abgeschlossen")
pause()
