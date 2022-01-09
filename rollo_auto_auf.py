#!/usr/bin/python3
from gpiozero import LED
from signal import pause
import time, sys
import logging

logging.basicConfig(filename='/home/pi/mylog2.log', filemode='w',level=logging.$

led1 = LED(18)
#led2 = LED(23)
led3 = LED(24)
#led4 = LED(25)

#Rolladen li auf
led1.on()
time.sleep(18)
led1.off()
logging.info('Rollo li offen')
time.sleep(2)

#Rolladen re auf
led3.on()
time.sleep(18)
led3.off()
logging.info('Rollo re offen')

sys.exit()
