# Generated by Django 3.1.7 on 2021-05-30 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_home_imagen_paralax'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='imagen_parallax1',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='home',
            name='imagen_parallax2',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]
