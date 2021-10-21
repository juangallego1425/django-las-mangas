from django.db import models

# Create your models here.

class Via(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion= models.CharField(max_length=200)
    imagen_via = models.ImageField(upload_to="gallery", blank=True, null=True)

    
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    via_id = models.ForeignKey('vias.Via', on_delete=models.CASCADE, blank=False, null=False)
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField('date published')
    descripcion= models.CharField(max_length=200)