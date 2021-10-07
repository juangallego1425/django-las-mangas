from django.db import models


# Create your models here.
class Anuncio(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('date published')
    descripcion = models.TextField(max_length=500)
    telefono = models.CharField(max_length=13)
    imagen1 = models.ImageField(upload_to="gallery", blank=True, null=True)
    imagen2 = models.ImageField(upload_to="gallery", blank=True, null=True)
    imagen3 = models.ImageField(upload_to="gallery", blank=True, null=True)
    imagen4 = models.ImageField(upload_to="gallery", blank=True, null=True)
    imagen5 = models.ImageField(upload_to="gallery", blank=True, null=True)
    
