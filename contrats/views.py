from django.shortcuts import render


def contrat(request):
    return render(request, 'pages\contrat.html')

def Patrimoine(request):
    return render(request, 'pages\Patrimoine.html')

def Effectif(request):
    return render(request, 'pages\Effectif.html')

def Service(request):
    return render(request, 'pages\Service.html')

def Investissement(request):
    return render(request, 'pages\Investissement.html')

def Partenaire(request):
    return render(request, 'pages\Partenaire.html')

def Energy(request):
    return render(request, 'pages\Efficacite_energitique.html')

def Commercial(request):
    return render(request, 'pages\Commercial.html')

def Commercial_second(request):
    return render(request, 'pages\Commercial_second.html')

def Commercial_second(request):
    return render(request, 'pages\Commercial_second.html')

def Contratslist(request):
    return render(request, 'pages\Contratslist.html')

