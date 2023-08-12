from django import forms
from .models import Contrat, Perimetre , Energie , Commerciale , Commercialseconde

class ContratForm(forms.ModelForm):
    class Meta:
        model = Contrat
        fields ="__all__"

class PerimetreForm(forms.ModelForm):
    class Meta:
        model = Perimetre
        fields ="__all__"

class EnergieForm(forms.ModelForm):
    class Meta:
        model = Energie
        fields ="__all__"

class CommercialeForm(forms.ModelForm):
    class Meta:
        model = Commerciale
        fields ="__all__"

class CommercialsecondeForm(forms.ModelForm):
    class Meta:
        model = Commercialseconde
        fields ="__all__"