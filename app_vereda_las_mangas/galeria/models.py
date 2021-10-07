from django.db import models

# Create your models here.
class Galeria(models.Model):
   titulo = models.CharField(max_length=200)

   def __str__(self):
      return self.titulo
