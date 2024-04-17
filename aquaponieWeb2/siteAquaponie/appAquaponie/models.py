from django.db import models


# Create your models here.
class Mesures(models.Model):
    humidite = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    ph = models.DecimalField(max_digits=5, decimal_places=2)
    niveauDeau = models.DecimalField(max_digits=5, decimal_places=2)
    lumiere = models.IntegerField()


class Datafile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='datafile/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title