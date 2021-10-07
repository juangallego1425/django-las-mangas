import logging

from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Galeria
from home.models import Home

# Create your views here.

logger = logging.getLogger(__name__)

def galeria(request):
    galeria = Galeria.objects.all
    logger.error(galeria)
    home = Home.objects.all
    for galeri in Galeria.objects.all():
        imagenes = list(galeri.imagenes_set.all())
        print(imagenes[0].imagen_url);
    context = {'galeria': galeria, 'home': home}
    return render(request, 'galeria/galeria.html', context)


