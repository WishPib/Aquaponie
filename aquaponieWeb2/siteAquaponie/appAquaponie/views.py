from django.shortcuts import render
#from models import mesure


def index(request):
    #dataTemperature = mesure.temperature
    #dataHumidite = mesure.humidite
    #dataPh = mesure.ph
    #dataLumiere = mesure.lumiere
    #dataNiveauDeau = mesure.niveauDeau
    return render(request, 'appAquaponie/index.html', {})
