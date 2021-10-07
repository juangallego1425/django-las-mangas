import logging

from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import  Suceso
from home.models import Home

# Create your views here.

logger = logging.getLogger(__name__)

def sucesos(request):
    ultimo_suceso = Suceso.objects.all
    logger.error("ultimo suceso")
    home = Home.objects.all
    context = {'ultimo_suceso': ultimo_suceso, 'home': home}
    return render(request, 'sucesos/sucesos.html', context)
