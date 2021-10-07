from django.db import models

class Home(models.Model):
# Create your models here:
 imagen_header = models.ImageField(upload_to="gallery", blank=True, null=True)
 imagen_parallax1 = models.ImageField(upload_to="gallery", blank=True, null=True)
 imagen_parallax2 = models.ImageField(upload_to="gallery", blank=True, null=True)

class Imagenes(models.Model):
 actividad_id = models.ForeignKey('actividades.Actividad', on_delete=models.CASCADE, blank=True, null=True)
 interes_id = models.ForeignKey('interes.Interes', on_delete=models.CASCADE, blank=True, null=True)
 galeria_id = models.ForeignKey('galeria.Galeria', on_delete=models.CASCADE, blank=True, null=True)
 titulo = models.CharField(max_length=200)
 imagen_url = models.ImageField(upload_to="gallery", blank=True, null=True)
 list_display = ('titulo')

 
 
