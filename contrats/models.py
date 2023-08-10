from django.db import models

# Create your models here.
class Contrat(models.Model):
    ContractID = models.AutoField(primary_key=True)
    ContractTitre = models.CharField(max_length=255)
    Delegant = models.CharField(max_length=255)
    Delegataire= models.CharField(max_length=255)
    Datevisa= models.DateField()
    DateDebut = models.DateField()
    DateFin = models.DateField()
