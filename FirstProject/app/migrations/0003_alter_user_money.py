# Generated by Django 4.2.5 on 2023-10-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.IntegerField(),
        ),
    ]