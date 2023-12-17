# Generated by Django 4.2.5 on 2023-12-17 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameStore', '0008_alter_jogador_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='tempo_fim_1p',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='tempo_fim_2p',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
