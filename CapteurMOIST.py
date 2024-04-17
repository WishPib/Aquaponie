import RPi.GPIO as GPIO
import time

channel = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

fonctionne = False

def arreter():
    global fonctionne
    fonctionne = False
    print("stop")

def activer():
    global fonctionne
    fonctionne = True
    print("start")

def prendreMesure():
    if (fonctionne):
        value = GPIO.input(channel)
        if value == 0:
            print("eau")
        else: 
            print("no eau")