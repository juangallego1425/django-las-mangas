# Generated by Django 3.1.7 on 2021-03-30 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0004_auto_20210329_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='imagen1',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagen4',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagen5',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]
