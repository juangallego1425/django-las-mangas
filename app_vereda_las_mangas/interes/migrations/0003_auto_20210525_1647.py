# Generated by Django 3.1.7 on 2021-05-25 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interes', '0002_interes_imagen1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interes',
            name='imagen1',
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('imagen_url', models.ImageField(blank=True, null=True, upload_to='gallery')),
                ('interes_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='interes.interes')),
            ],
        ),
    ]