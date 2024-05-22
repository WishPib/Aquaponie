import RPi.GPIO as GPIO
import time
# Le channel peut être différent
channel = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def prendreMesure():
    value = GPIO.input(channel)
    if value == 0:
        print("eau détecté")
    else: 
        print("pas d'eau")
    return value
