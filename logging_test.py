#!/usr/bin/python3

from time import sleep
import logging

logging.basicConfig(filename='/home/pi/mylog1.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
 13                      level=logging.INFO)

n = 0
while n < 7:
    print('printing')
    logging.info('printing again')
    sleep(3)
    n+= 1
