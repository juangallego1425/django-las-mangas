# Generated by Django 3.1.7 on 2021-05-29 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0004_actividad_contacto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='imagen1',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='imagen2',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='imagen3',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='imagen4',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='imagen5',
        ),
    ]
