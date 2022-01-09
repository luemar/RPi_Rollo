#!/usr/bin/python3
import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN)

def response(pin):
    print("button pressed")


GPIO.add_event_detect(37, GPIO.FALLING)
GPIO.add_event_callback(37, response)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
