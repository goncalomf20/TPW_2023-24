# Generated by Django 4.2.5 on 2023-10-27 17:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_paymentmethod'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]