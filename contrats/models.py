from django.db import models

# Create your models here.
class Contrat(models.Model):
    contrat_id = models.AutoField(primary_key=True)
    titreducontrat = models.CharField(max_length=100)
    déléguant = models.CharField(max_length=100)
    délégataire = models.CharField(max_length=100)
    semestre_debut = models.DateField()
    semestre_fin = models.DateField()
    datevisa = models.DateField()
    durée = models.IntegerField()
    datededémarrage = models.DateField()

class Perimetre(models.Model):
    contrat_id = models.ForeignKey(Contrat , on_delete=models.CASCADE)
    communesdesservies = models.IntegerField()
    populationdesservie = models.IntegerField()
    longueur_réseau = models.IntegerField()
    nombre_lignes = models.IntegerField()
    lignesurbaines = models.IntegerField()
    lignespériphériques = models.IntegerField()

class Energie(models.Model):
    contrat_id = models.ForeignKey(Contrat , on_delete=models.CASCADE)
    consommation_moyenne = models.DecimalField(max_digits=5 , decimal_places=2)
    consommation_carurbant = models.DecimalField(max_digits=5 , decimal_places=2)
    consommation_electricite = models.DecimalField(max_digits=5 , decimal_places=2)
    emission_carbone = models.DecimalField(max_digits=5 , decimal_places=2)


