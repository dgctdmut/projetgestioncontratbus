from django.db import models

# Create your models here.
class contrat(models.Model):
    Contrat = models.CharField(max_length=100)
    Déléguant = models.CharField(max_length=100)
    Délégataire = models.CharField(max_length=100)
    SemestreDe = models.DateField()
    Semestreà = models.DateField()
    Datevisa = models.DateField()
    Durée = models.IntegerField()
    Datededémarrage = models.DateField()

