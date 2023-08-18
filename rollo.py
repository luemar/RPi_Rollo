#!/usr/bin/python3
from gpiozero import Button, DigitalOutputDevice, LED
from time import sleep
import logging
import schedule
from functools import partial

logging.basicConfig(filename='/home/pi/mylog1.log', filemode='w',\
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',\
                    level=logging.INFO)
logging.info('rollo.py gestarted')

SWITCH_PIN = 12

def automatisch_fahren_re(motor):
    motor.on()
    sleep(18.2)
    motor.off()
    print('rollo re automatisch gefahren')
    logging.info('rollo re automatisch gefahren')

def automatisch_fahren_li(motor):
    motor.on()
    sleep(17.5)
    motor.off()
    print('rollo li automatisch gefahren')
    logging.info('rollo li automatisch gefahren')

def zeitgeschaltet_hochfahren(motor_1, motor_2, switch):
    print('Hochfahren Funktion aufgerufen')
    logging.info('Hochfahren Funktion aufgerufen')
    if switch.is_pressed:
       print('Switch pressed')
       logging.info('Switch pressed')
       motor_1.on()
       sleep(18.2)
       motor_1.off()
       motor_2.on()
       sleep(17.5)
       motor_2.off()
       print('rollos zeitgeschaltet hochgefahren')
       logging.info('rollos zeitgeschaltet hochgefahren')
    else:
        print('switch aus')

def zeitgeschaltet_runterfahren(motor_1, motor_2):
    motor_1.on()
    sleep(18.2)
    motor_1.off()
    motor_2.on()
    sleep(17.5)
    motor_2.off()
    print('rollos zeitgeschaltet runtergefahren')
    logging.info('rollos zeitgeschaltet runtergefahren')

def main():
    links_manuell_auf = Button(26)
    links_manuell_zu = Button(13)
    motor_li_ab = DigitalOutputDevice(24)
    motor_li_auf = DigitalOutputDevice(18)

    rechts_manuell_auf = Button(27)
    rechts_manuell_zu = Button(5)
    motor_re_auf = DigitalOutputDevice(25)
    motor_re_ab = DigitalOutputDevice(23)

    links_auto_auf = Button(19, hold_time = 1)
    links_auto_zu = Button(6, hold_time = 1)
    rechts_auto_auf = Button(17, hold_time = 1)
    rechts_auto_zu = Button(22, hold_time = 1)

    switch = Button(SWITCH_PIN, pull_up=False)

    print('main gestarted')
    logging.info('main gestarted')

    links_manuell_auf.when_pressed = motor_li_auf.on
    links_manuell_auf.when_released = motor_li_auf.off
    links_manuell_zu.when_pressed = motor_li_ab.on
    links_manuell_zu.when_released = motor_li_ab.off
    rechts_manuell_auf.when_pressed = motor_re_auf.on
    rechts_manuell_auf.when_released = motor_re_auf.off
    rechts_manuell_zu.when_pressed = motor_re_ab.on
    rechts_manuell_zu.when_released = motor_re_ab.off

    links_auto_auf.when_held = partial(automatisch_fahren_li, motor_li_auf)
    links_auto_zu.when_held = partial(automatisch_fahren_li, motor_li_ab)
    rechts_auto_auf.when_held = partial(automatisch_fahren_re, motor_re_auf)
    rechts_auto_zu.when_held = partial(automatisch_fahren_re, motor_re_ab)

    #hochfahren
    schedule.every().day.at("HH:MM").do(zeitgeschaltet_hochfahren, motor_li_auf, motor_re_auf, switch)
    #runterfahren
    schedule.every().day.at("HH:MM").do(zeitgeschaltet_runterfahren, motor_li_ab, motor_re_ab)

    while True:
        schedule.run_pending()
        sleep(1)

    print('init abgeschlossen')

if __name__ == "__main__":
    main()
