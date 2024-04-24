import time
import CapteurNiveauEau
import CapteurMOIST
import BaseDonne

time.sleep(1)
valeurNiveauEau = False
valeurHumide = False
BaseDonne.resetBD()

def prendreMesures():
    global valeurNiveauEau
    valeurNiveauEau = CapteurNiveauEau.prendreMesure()
    global valeurHumide
    valeurHumide = CapteurMOIST.prendreMesure()

while True:
    prendreMesures()
    BaseDonne.envoyerBD(valeurNiveauEau,valeurHumide)
    print()
    time.sleep(2)
