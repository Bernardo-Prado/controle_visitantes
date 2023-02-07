from django.db import models

class Visitantes(models.Model):

    nome_completo = models.CharField(
        verbose_name="Nome Completo",
        max_length=194
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11
    )

# nome completo, cpf, data de nascimento, número da casa, placa do veiculo, horario de entrada-saida-autorização, nome de quem autorizou, nome do responsável pelo registro
