from django.shortcuts import render , redirect 
from .models import Contrat , Perimetre , Energie
from .forms import ContratForm , PerimetreForm , EnergieForm

def Contratidentif(request):
    if request.method=="POST":
        form = ContratForm(request.POST)
        if form.is_valid():
            contrat = form.save()
            return redirect ('Perimetre' , contratid = contrat.contrat_id ) 
    else:
        form = ContratForm() 
    return render(request, 'pages\Contrat.html'   , {'form': form})

def Perimetre_step(request , contratid ):
    contrat = Contrat.objects.get(contrat_id = contratid)
    if request.method=="POST":
        form = PerimetreForm(request.POST)
        if form.is_valid():
            perimetre = form.save(commit=False)

            perimetre.contrat_id = contrat
            perimetre.save()
            return redirect ('Investissement', contratid = contrat.contrat_id )
    else:
        form = PerimetreForm()
       
    return render(request, 'pages\Perimetre.html' , {'form': form})

def Patrimoine(request):
    return render(request, 'pages\Patrimoine.html')

def Patrimoine_second(request):
    return render(request, 'pages\Patrimoine_second.html')

def Effectif(request):
    return render(request, 'pages\Effectif.html')

def Service(request):
    return render(request, 'pages\Service.html')

def Investissement(request):
    return render(request, 'pages\Investissement.html')

def Partenaire(request):
    return render(request, 'pages\Partenaire.html')

def Energy(request):
    if request.method=="POST":
        form = EnergieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('contrat') 
    else:
        form = EnergieForm()
    return render(request, 'pages\Efficacite_energitique.html' , {'form': form})

def Commercial(request):
    return render(request, 'pages\Commercial.html')

def Commercial_second(request):
    return render(request, 'pages\Commercial_second.html')

def Commercial_second(request):
    return render(request, 'pages\Commercial_second.html')

def Contratslist(request):
    return render(request, 'pages\Contratslist.html')

