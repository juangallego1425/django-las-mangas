from django.db import models


# Create your models here.
class Hisoria(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=500)
