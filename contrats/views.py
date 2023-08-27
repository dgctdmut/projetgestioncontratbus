from django.shortcuts import render , redirect 
from .models import Contrat , Perimetre , Energie , Partenaire , Investissement
from .forms import ContratForm , PerimetreForm , EnergieForm ,  CommercialeForm , CommercialsecondeForm , InvestissementForm , PartenaireForm 


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
            return redirect ('Investissement' , contratid = contrat.contrat_id )
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

def Investissement_contractuels(request, contratid ):
    contrat = Contrat.objects.get(contrat_id = contratid)
    if request.method=="POST":
        form = InvestissementForm(request.POST)
        if form.is_valid():
            investissement = form.save(commit=False)
            investissement.contrat_id = contrat
            investissement.save()
            return redirect ('Commercial' , contratid = contrat.contrat_id )
    else:
        form = InvestissementForm()
    return render(request, 'pages\Investissement.html', {'form': form})

def Autre_Partenaire(request):
    if request.method=="POST":
        form = PartenaireForm(request.POST)
        if form.is_valid():
           partenaire = form.save()
           return redirect ('Perimetre' , partenaireid = partenaire.partenaire_id ) 
    else:
        form = PartenaireForm() 
    return render(request, 'pages\Partenaire.html', {'form': form})

def Energy(request):
    contrat = Contrat.objects.get(contrat_id = contratid)
    if request.method=="POST":
        form = EnergieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('contrat') 
    else:
        form = EnergieForm()
    return render(request, 'pages\Efficacite_energitique.html' , {'form': form})

def Commercial(request , contratid):
    contrat = Contrat.objects.get(contrat_id = contratid)
    if request.method=="POST":
        form = CommercialeForm(request.POST)
        if form.is_valid():
            commercial = form.save(commit=False)
            commercial.contrat_id = contrat
            commercial.save()
            return redirect ('Commercial_second') 
    else:
        form = CommercialeForm()
    return render(request, 'pages\Commercial.html' , {'form': form})

def Commercial_second(request):
    if request.method=="POST":
        form = CommercialsecondeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Energy') 
    else:
        form = CommercialsecondeForm()
    return render(request, 'pages\Commercial_second.html', {'form': form})


def Contratslist(request):
    return render(request, 'pages\Contratslist.html')



def login_view(request):
    return render(request, 'pages\login.html')
