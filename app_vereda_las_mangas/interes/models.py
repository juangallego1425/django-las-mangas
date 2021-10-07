from django.db import models

# Create your models here.
class Interes(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=500)


    def __str__(self):
        return self.titulo

