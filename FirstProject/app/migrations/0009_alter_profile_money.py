# Generated by Django 4.2.5 on 2023-10-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_profile_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='money',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]