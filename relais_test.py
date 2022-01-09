#!/usr/bin/python3
from gpiozero import LED
from signal import pause
import time, sys
import logging

logging.basicConfig(filename='/home/pi/mylog2.log', filemode='w',level=logging.$


#led1 = LED(18)
led2 = LED(23)
led3 = LED(24)
led4 = LED(25)

#Rolladen li ab
led2.on()
print('relais 2 on')
time.sleep(18)
led2.off()
print('relais 2 off')
logging.info('Rollo li geschlossen')
time.sleep(2)
