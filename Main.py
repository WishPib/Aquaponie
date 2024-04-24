import time
import CapteurNiveauEau
import CapteurMOIST
import Pompe

time.sleep(1)

def prendreMesures():
    CapteurNiveauEau.prendreMesure()
    CapteurMOIST.prendreMesure()

while True:
    prendreMesures()
    print()
    time.sleep(2)
