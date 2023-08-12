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
    contrat_id = models.ForeignKey(Contrat , on_delete=models.CASCADE , blank=True, null=True )
    communesdesservies = models.IntegerField()
    populationdesservie = models.IntegerField()
    longueur_réseau = models.IntegerField()
    nombre_lignes = models.IntegerField()
    lignesurbaines = models.IntegerField()
    lignespériphériques = models.IntegerField()

class Commerciale(models.Model):
    contrat_id = models.ForeignKey(Contrat , on_delete=models.CASCADE , blank=True, null=True )
    nbvoyageurs=  models.IntegerField()
    nbplacesvides=  models.IntegerField()
    totalvoyageursannuels=  models.IntegerField()
    tauxremplissage= models.IntegerField()
    tauxtransportvide= models.IntegerField()
    ticketsvendussemestre=  models.IntegerField()
    tarifscolaire= models.IntegerField()
    tarifnormal= models.IntegerField()
    tarifconventions= models.IntegerField()

class Commercialseconde(models.Model):
    contrat_id = models.ForeignKey(Contrat , on_delete=models.CASCADE , blank=True, null=True )
    total_parcours_semestriel= models.IntegerField()
    moyenne_par_ligne= models.IntegerField()
    trajet_le_plus_long= models.IntegerField()
    trajet_le_plus_court= models.IntegerField()
    temps_max_trajet= models.DecimalField(max_digits=5 , decimal_places=2)
    temps_min_trajet= models.DecimalField(max_digits=5 , decimal_places=2)
    frequence_passage= models.IntegerField()
    vitesse_commerciale= models.IntegerField()
    ponctualite=models.DecimalField(max_digits=5 , decimal_places=2)
    horaire_debut= models.TimeField()
    horaire_fin= models.TimeField()
    heure_arret_service= models.IntegerField()
    pannes_bus= models.IntegerField()
    accidents_bus= models.IntegerField()
    delai_evacuation_panne= models.DecimalField(max_digits=5 , decimal_places=2)

class Energie(models.Model):
    contrat_id = models.ForeignKey(Contrat , on_delete=models.CASCADE , blank=True, null=True )
    consommation_moyenne = models.DecimalField(max_digits=5 , decimal_places=2)
    consommation_carurbant = models.DecimalField(max_digits=5 , decimal_places=2)
    consommation_electricite = models.DecimalField(max_digits=5 , decimal_places=2)
    emission_carbone = models.DecimalField(max_digits=5 , decimal_places=2)
    