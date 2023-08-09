from django import forms
from .models import Contrat, Perimetre , Energie

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