import logging

from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Anuncio
from home.models import Home

# Create your views here.

logger = logging.getLogger(__name__)

def anuncios(request):
    ultimos_anuncios = Anuncio.objects.all
    #se adjunta el home por el header y el footer
    home = Home.objects.all
    context = {'ultimos_anuncios': ultimos_anuncios, 'home': home}
    return render(request, 'anuncios/index.html', context)

def detalle_anuncio(request, anuncio_id):
    home = Home.objects.all
    anuncio = get_object_or_404(Anuncio, pk=anuncio_id)
    return render(request, 'anuncios/detalle_anuncio.html', {'anuncio': anuncio, 'home': home})
    