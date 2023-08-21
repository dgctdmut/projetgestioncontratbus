from django.urls import path
from . import views

urlpatterns = [
    path('contrat',views.Contratidentif,name='contrat'),
    path('Patrimoine',views.Patrimoine,name='Patrimoine'),
    path('Patrimoine_second',views.Patrimoine_second,name='Patrimoine_second'),
    path('Effectif',views.Effectif,name='Effectif'),
    path('Service',views.Service,name='Service'),    
    path('Investissement/<int:contratid>/',views.Investissement_contractuels,name='Investissement'),    
    path('Partenaire',views.Autre_Partenaire,name='Partenaire'),
    path('Energy',views.Energy,name='Energy'),
    path('Commercial/<int:contratid>/',views.Commercial,name='Commercial'),
    path('Commercial_second',views.Commercial_second,name='Commercial_second'),
    path('Contratslist',views.Contratslist,name='contrat_list'),

    path('Perimetre/<int:contratid>/',views.Perimetre_step,name='Perimetre'),
]
