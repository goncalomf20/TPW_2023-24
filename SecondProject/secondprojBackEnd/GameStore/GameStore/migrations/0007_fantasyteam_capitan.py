# Generated by Django 4.2.5 on 2023-12-17 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameStore', '0006_jogador_pontos'),
    ]

    operations = [
        migrations.AddField(
            model_name='fantasyteam',
            name='capitan',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
