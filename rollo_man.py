#!/usr/bin/python3
from gpiozero import Button, LED, DigitalInputDevice
from signal import pause
import time
import logging
import schedule
import threading

logging.basicConfig(filename='/home/pi/mylog1.log', filemode='w',\
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',\
                    level=logging.INFO)
logging.info('rollo_man.py gestarted')

Taste_li_autoauf = Button(17, hold_time = 1)
Taste_li_autoab = Button(22, hold_time = 1)
Taste_li_manauf = Button(27)
Taste_li_manab = Button(5)
Taste_re_autoauf = Button(6, hold_time = 1)
Taste_re_autoab = Button(19, hold_time = 1)
Taste_re_manauf = Button(13)
Taste_re_manab = Button(26)

led1 = LED(25)
led2 = LED(23)
led3 = LED(24)
led4 = LED(18)

switch=DigitalInputDevice(12, pull_up=False)

Button.was_held = False

def held_li_up(Taste_li_autoauf):
    print("Taste li auf gehalten")
    Button.was_held = True
    led1.on()
    time.sleep(18)
    led1.off()

def released_li_up(Taste_li_autoauf):
    if not Taste_li_autoauf.was_held:
        Button.was_held = False

def held_li_down(Taste_li_autoab):
    #print("Taste li ab gehalten")
    Button.was_held = True
    led2.on()
    time.sleep(18)
    led2.off()

def released_li_down(Taste_li_autoab):
    if not Taste_li_autoab.was_held:
        Button.was_held = False

def held_re_up(Taste_re_autoauf):
    #print("Taste re auf gehalten")
    Button.was_held = True
    led3.on()
    time.sleep(18)
    led3.off()

def released_re_up(Taste_re_autoauf):
    if not Taste_re_autoauf.was_held:
        Button.was_held = False

def held_re_down(Taste_re_autoab):
    #print("Taste re ab gehalten")
    Button.was_held = True
    led4.on()
    time.sleep(18)
    led4.off()

def released_re_down(Taste_re_autoab):
    if not Taste_re_autoab.was_held:
        Button.was_held = False
def on_up_li():
    print("Taste li auf gedrueckt")
    led1.on()

def off_up_li():
    print("Taste li auf losgelassen")
    led1.off()

def on_down_li():
    print("Taste li ab gedrueckt")
    led2.on()

def off_down_li():
    print("Taste li ab losgelassen")
    led2.off()

def on_up_re():
    print("Taste re auf gedrueckt")
    led3.on()

def off_up_re():
    print("Taste re auf losgelassen")
    led3.off()

def on_down_re():
    print("Taste re ab gedrueckt")
    led4.on()

def off_down_re():
    print("Taste re ab losgelassen")
    led4.off()
    
def zeitschalt_runterfahren_an():
    led2.on()
    time.sleep(18.2)
    led2.off()
    logging.info('Rollo li geschlossen')
    time.sleep(2)

    led3.on()
    time.sleep(17.5)
    led3.off()
    logging.info('Rollo re geschlossen')

def zeitschalt_hochfahren_an():
    led1.on()
    time.sleep(18.2)
    led1.off()
    logging.info('Rollo li offen')
    time.sleep(2)

    led4.on()
    time.sleep(17.5)
    led4.off()
    logging.info('Rollo re offen')

def schedule_thread():
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    gpio_pin_12=switch.value
    if gpio_pin_12 == 1:
        schedule.every().day.at("HH:MM").do(zeitschalt_hochfahren_an)
    schedule.every().day.at("HH:MM").do(zeitschalt_runterfahren_an)
    
    logging.info('Rollo heruntergefahren')

    threading.Thread(target=schedule_thread).start()

    Taste_li_autoauf.when_held = held_li_up
    Taste_li_autoauf.when_released = released_li_up
    Taste_li_autoab.when_held = held_li_down
    Taste_li_autoab.when_released = released_li_down

    Taste_re_autoauf.when_held = held_re_up
    Taste_re_autoauf.when_released = released_re_up
    Taste_re_autoab.when_held = held_re_down
    Taste_re_autoab.when_released = released_re_down

    Taste_li_manauf.when_pressed = on_up_li
    Taste_li_manauf.when_released = off_up_li
    Taste_li_manab.when_pressed = on_down_li
    Taste_li_manab.when_released = off_down_li

    Taste_re_manauf.when_pressed = on_up_re
    Taste_re_manauf.when_released = off_up_re
    Taste_re_manab.when_pressed = on_down_re
    Taste_re_manab.when_released = off_down_re

    print("Init abgeschlossen")
    pause()

if __name__ == "__main__":
    main()

