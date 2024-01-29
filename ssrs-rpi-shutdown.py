#!/usr/bin/env python3

import os
import RPi.GPIO as GPIO
import time

shutdown_pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(shutdown_pin, GPIO.IN)

def shutdown(channel):
    print('Got shutdown signal')
    os.system("sudo shutdown -h now")

GPIO.add_event_detect(shutdown_pin, GPIO.RISING, callback=shutdown, bouncetime=100)

while True:
    time.sleep(1)
