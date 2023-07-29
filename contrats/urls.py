from django.urls import path
from . import views

urlpatterns = [
    path('contrat',views.contrat,name='contrat'),
    path('Patrimoine',views.Patrimoine,name='Patrimoine'),
    path('Effectif',views.Effectif,name='Effectif'),
    path('Service',views.Service,name='Service'),    
    path('Investissement',views.Investissement,name='Investissement'),    
    path('Partenaire',views.Partenaire,name='Partenaire'),
    path('Energy',views.Energy,name='Energy'),
    path('Commercial',views.Commercial,name='Commercial'),
    path('Commercial_second',views.Commercial_second,name='Commercial_second'),

]