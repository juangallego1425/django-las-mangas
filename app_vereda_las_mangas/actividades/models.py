from django.db import models


# Create your models here.
class Actividad(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=500)
    contacto = models.TextField(max_length=20)
    descripcion = models.TextField(max_length=500)
    destacado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    
