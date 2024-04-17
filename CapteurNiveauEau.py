import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

entre = 27

activer = False

GPIO.setup(entre, GPIO.IN)

def stop():
    activer = False
    print("stop")

def commencer():
    print("start")
    activer = True
    while activer:
        etat = GPIO.input(entre)
        if (etat == 1):
            print("CapteurNiveauEau On, assez d'eau")
        else:
            print("CapteurNiveauEau Off, pas assez d'eau")
        time.sleep(3)

