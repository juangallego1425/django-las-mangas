import logging

from django.shortcuts import render, HttpResponse

from .models import Home

logger = logging.getLogger(__name__)

def home(request):
    home = Home.objects.all
    logger.error("ultimos home")
    #logger.error(ultimo_home.imagen_header.url)
    context = {'home': home}
    return render(request, 'home/home.html', context)