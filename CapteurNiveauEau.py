import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

entre = 27

fonctionne = False

GPIO.setup(entre, GPIO.IN)

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
        etat = GPIO.input(entre)
        if (etat == 1):
            print("CapteurNiveauEau On, assez d'eau")
        else:
            print("CapteurNiveauEau Off, pas assez d'eau")
    else:
        print("Nest pas allumer")