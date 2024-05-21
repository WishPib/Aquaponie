import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# Le channel peut être différent, dépend de la configuration sur le raspberry pi.
entre = 27

GPIO.setup(entre, GPIO.IN)

def prendreMesure():
    etat = GPIO.input(entre)
    if (etat == 1):
        print("CapteurNiveauEau On, assez d'eau")
    else:
        print("CapteurNiveauEau Off, pas assez d'eau")
    return etat    
