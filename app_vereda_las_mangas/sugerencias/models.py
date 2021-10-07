from django.db import models


# Create your models here.
class Sugerencia(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(max_length=500, blank=True, null=True)
    
    def __str__(self):
            return self.titulo