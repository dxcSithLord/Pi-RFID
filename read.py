#!/usr/bin/env python

'''
This script will wait untill you put your RFID tag on the RFID RC522 reader.
Then it will then output the data it reads off the tag.
Code originally from https://pimylifeup.com/raspberry-pi-rfid-rc522/
using libraries from https://github.com/pimylifeup/MFRC522-python
'''

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
print("Waiting to read token - place token near reader\n")
try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()

