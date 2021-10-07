import logging

from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Interes
from home.models import Home

# Create your views here.

logger = logging.getLogger(__name__)

def interes(request):
    interes = Interes.objects.all
    logger.error(interes)
    home = Home.objects.all
    for intere in Interes.objects.all():
        imagenes = list(intere.imagenes_set.all())
        print(imagenes[0].imagen_url);
    context = {'interes': interes, 'home': home}
    return render(request, 'interes/interes.html', context)
