import RPi.GPIO as GPIO
import time
# Le channel peut être différent
channel = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def prendreMesure():
    value = GPIO.input(channel)
    if value == 0:
        print("eau")
    else: 
        print("no eau")
    return value
