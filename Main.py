import time
import CapteurNiveauEau
import CapteurMOIST
import BaseDonne
import Pompe

time.sleep(1)
valeurNiveauEau = False
valeurHumide = False

def prendreMesures():
    global valeurNiveauEau
    valeurNiveauEau = CapteurNiveauEau.prendreMesure()
    global valeurHumide
    valeurHumide = CapteurMOIST.prendreMesure()
    affecterPompe(valeurHumide, valeurNiveauEau)

# Pomper l'eau si la terre n'est pas assez humide
def __affecterPompe(valeurHumide, valeurNiveauEau) :
    if valeurHumide == 1:
        Pompe.pomperEau(True, 100)
        sleep(50)
        Pompe.stop()
    
# Le programme roule en continu et peut être fermé avec ctrl + c dans la console
while True:
    prendreMesures()
    BaseDonne.envoyerBD(valeurNiveauEau,valeurHumide)
    time.sleep(2)
