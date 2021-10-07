import logging

from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import  Acerca
from home.models import Home

# Create your views here.

logger = logging.getLogger(__name__)

def acercav(request):
    ultimo_acerca = Acerca.objects.all
    logger.error("ultimo acerca")
    #logger.error(ultimo_home.imagen_header.url)
    home = Home.objects.all
    context = {'ultimo_acerca': ultimo_acerca, 'home': home}
    return render(request, 'acercav/acercav.html', context)
