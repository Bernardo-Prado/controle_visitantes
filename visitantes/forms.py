from django import forms
from visitantes.models import Visitante

# Mapeia os campos automaticamente da classe Model
# Define quais campos vão ser exibidos 
class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", 
            "cpf", 
            "data_de_nascimento", 
            "numero_casa", 
            "placa_veiculo"
        ]
