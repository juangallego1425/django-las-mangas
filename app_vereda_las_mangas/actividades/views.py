import logging

from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Actividad
from home.models import Home

# Create your views here.

logger = logging.getLogger(__name__)

def actividades(request):
    actividades = Actividad.objects.all
    logger.error(actividades)
    home = Home.objects.all
    for actividad in Actividad.objects.all():
        imagenes = list(actividad.imagenes_set.all())
        print(imagenes[0].imagen_url);
    context = {'actividades': actividades, 'home': home}
    return render(request, 'actividades/actividades.html', context)
