# Generated by Django 3.1.7 on 2021-05-23 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_home_imagen_paralax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='imagen_paralax',
        ),
    ]
