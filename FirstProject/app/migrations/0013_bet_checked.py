# Generated by Django 4.2.5 on 2023-10-27 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_game_game_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='checked',
            field=models.IntegerField(default=0),
        ),
    ]
