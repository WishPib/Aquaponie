from django.db import models


# Create your models here.
class Mesures(models.Model):
    humidite = models.BooleanField()
    niveauDeau = models.BooleanField()


class Datafile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='datafile/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title