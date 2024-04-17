from django.db import models


# Create your models here.
class Mesures(models.Model):
    humidite = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    ph = models.DecimalField(max_digits=5, decimal_places=2)
    niveauDeau = models.DecimalField(max_digits=5, decimal_places=2)
    lumiere = models.IntegerField()

   #humidite = 10
   #temperature = 20
   #ph = 30
   #niveauDeau = 40
   #lumiere = 50
