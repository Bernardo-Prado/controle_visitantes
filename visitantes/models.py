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

    data_de_nascimento = models.DateField(
        verbose_name="Data de nascimneto",
        auto_now_add=False,
        auto_now=False,
    )

    # O positive serve para armazenar valores positivos pequenos
    numero_casa = models.PositiveSmallIntegerField(
        verbose_name="Número da casa a ser visitada",
    )


# nome completo, cpf, data de nascimento, número da casa, placa do veiculo, horario de entrada-saida-autorização, nome de quem autorizou, nome do responsável pelo registro
