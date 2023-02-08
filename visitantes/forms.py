from django import forms
from visitantes.models import Visitante

# Mapeia os campos automaticamente da classe Model
class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = "__all__"
