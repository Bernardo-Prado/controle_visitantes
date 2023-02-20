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
        error_messages = {
            "nome_completo": {
                "required": "O nome completo do visitante é obrigatório para o registro"
            },
            "cpf": {
                "required": "O cpf do visitante é obrigatório para o registro"
            },
            "data_de_nascimento": {
                "required": "A data de nascimento do visitante é obrigatório para o registro",
                "invalid": "Por favor, informe um formato válido para a data de nascimento (DD/MM/AAAA)"
            },
            "numero_casa": {
                "required": "Por favor, informe o número da casa a ser visitada"
            }
        }
