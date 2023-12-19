# Generated by Django 4.2.5 on 2023-12-17 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GameStore', '0003_alter_liga_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='FirstName',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='LastName',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='equipa',
            name='grupos',
            field=models.ManyToManyField(blank=True, to='GameStore.grupo'),
        ),
        migrations.AlterField(
            model_name='equipa',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='liga',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='GameStore.liga'),
        ),
        migrations.AlterField(
            model_name='liga',
            name='equipas',
            field=models.ManyToManyField(blank=True, to='GameStore.equipa'),
        ),
        migrations.AlterField(
            model_name='liga',
            name='fase',
            field=models.CharField(max_length=20),
        ),
    ]