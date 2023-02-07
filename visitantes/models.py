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

    # Pode ser nulo ou em branco, caso o visitante não tenha veiculo
    placa_veiculo = models.CharField(
        verbose_name="Placa de veículo",
        max_length=7,
        blank=True,
        null=True,
    )

    horario_chegada = models.DateTimeField(
        verbose_name="Horário de chegada na portaria",
        auto_now_add=True,
    )

    horario_saida = models.DateTimeField(
        verbose_name="Horário de saída do condomínio",
        auto_now=False,
        blank=True,
        null=True,
    )

    horario_autorizacao = models.DateTimeField(
        verbose_name="Horário de autorização de entrada",
        auto_now=False,
        blank=True,
        null=True,
    )

    morador_responsavel = models.CharField(
        verbose_name="Nome do morador responsável por autorizar a entrada do visitante",
        max_length=194,
        blank=True,
    )

    registrado_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsável pelo registro",
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = "Visitante",
        verbose_name_plural = "Visitantes",
        db_table = "visitante"

    def __str__(self):
        return self.nome_completo
# nome completo, cpf, data de nascimento, número da casa, placa do veiculo, horario de entrada-saida-autorização, nome de quem autorizou, nome do responsável pelo registro
