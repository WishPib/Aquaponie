from django.db import models


# Create your models here.
class mesure(models.Model):
    humidite = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    ph = models.DecimalField(max_digits=5, decimal_places=2)
    niveauDeau = models.DecimalField(max_digits=5, decimal_places=2)
    lumiere = models.IntegerField()

    def __str__(self):
        return {self.pk}
