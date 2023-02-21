# Generated by Django 3.0 on 2023-02-21 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visitante',
            options={'verbose_name': 'Visitante', 'verbose_name_plural': 'Visitantes'},
        ),
        migrations.AddField(
            model_name='visitante',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO', 'Aguardando autorização'), ('FINALIZADO', 'Visita finalizada'), ('EM_VISITA', 'Em visita')], default='AGUARDANDO', max_length=10, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='visitante',
            name='data_de_nascimento',
            field=models.DateField(verbose_name='Data de nascimento'),
        ),
    ]