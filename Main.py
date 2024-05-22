import time
import CapteurNiveauEau
import CapteurMOIST
import BaseDonne
import Pompe
# Utiliser "python3 manage.py runserver 7000" dans le terminal en étant dans le bon directory (aquaponieWeb2/siteAquaponie) pour lancer le serveur local
# et ouvrire l'adresse donnée
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
    print()
    BaseDonne.envoyerBD(valeurNiveauEau,valeurHumide)
    time.sleep(2)
