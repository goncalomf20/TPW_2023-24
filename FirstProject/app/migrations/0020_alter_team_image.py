# Generated by Django 4.2.5 on 2023-11-11 14:27

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_team_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='../app/static/assets/images'),
        ),
    ]
