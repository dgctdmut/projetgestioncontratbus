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

class Partenaire(models.Model):
    partenaire_id = models.AutoField(primary_key=True )
    partenaire_nom = models.CharField(max_length=100)
    def __str__(self) :
        return self.partenaire_nom

class Investissement(models.Model):
    contrat_id = models.ForeignKey(Contrat , on_delete=models.CASCADE , blank=True, null=True )
    partenaire_id = models.ForeignKey(Partenaire , on_delete=models.CASCADE )
    montant_investissement = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_bus = models.IntegerField()
    nombre_abris = models.IntegerField()
    nombre_arrets = models.IntegerField()
    nombre_aires_stationnement = models.IntegerField()
    
class Type_MR (models.Model): 
    id_categoie = models.AutoField(primary_key=True) 
    nom_categoie = models.CharField(max_length=100)

class Type_MF (models.Model):
    id_patrimoine = models.AutoField(primary_key=True) 
    contrat_id = models.CharField(max_length=100)

class Patrimoine (models.Model):
    id_patrimoine = models.AutoField(primary_key=True)
    contrat_id = models.ForeignKey(Contrat, on_delete=models.CASCADE, blank=True,null=True) 
    id_Fixe = models.ForeignKey(Type_MF, on_delete=models.CASCADE, blank=True, null=True) 
    id_MR = models.ForeignKey(Type_MR, on_delete=models.CASCADE, blank=True, null=True) 

class Materiel_roulant (models.Model):
    nombre = models.DecimalField(max_digits=5 , decimal_places=2)
    age = models.DecimalField(max_digits=5 , decimal_places=2)
    km_parcourus = models.DecimalField(max_digits=5, decimal_places=2)
    id_MR = models.ForeignKey(Type_MR, on_delete=models.CASCADE, blank=True, null=True)

class Materiel_roulant (models.Model):
    nombre = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.DecimalField(max_digits=5, decimal_places=2)
    capacite = models.CharField()
    etet_satisfaction = models.CharField()
    id_Fixe = models.ForeignKey(Type_MF, on_delete=models.CASCADE, blank=True, null=True) 

class Effectif_Rh (models.Model):
    contrat_id = models.ForeignKey(Contrat, on_delete=models.CASCADE, blank=True, null=True) 
    Conducteurs = models.IntegerField()
    


    