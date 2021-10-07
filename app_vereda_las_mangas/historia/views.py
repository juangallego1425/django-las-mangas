import logging

from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import  Hisoria
from home.models import Home

# Create your views here.

logger = logging.getLogger(__name__)

def historia(request):
    ultima_historia = Hisoria.objects.all
    logger.error("ultima Historia")
    home = Home.objects.all
    context = {'ultima_historia': ultima_historia, 'home': home}
    return render(request, 'historia/historia.html', context)
