# Generated by Django 4.2.5 on 2023-12-17 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameStore', '0007_fantasyteam_capitan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
    ]
