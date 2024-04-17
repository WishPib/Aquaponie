import time
import CapteurNiveauEau
import CapteurMOIST
import Pompe

CapteurNiveauEau.activer()
CapteurMOIST.activer()
time.sleep(2)



#CapteurNiveauEau.arreter()

def prendreMesures():
    CapteurNiveauEau.prendreMesure()
    CapteurMOIST.prendreMesure()

while True:
    prendreMesures()
    print()
    time.sleep(2)
