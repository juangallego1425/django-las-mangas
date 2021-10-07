from .models import Via
from django.shortcuts import render
from .form import Comentario_via
from .models import Via, Comentario
from home.models import Home


def vias(request):
    vias = Via.objects.all
    home = Home.objects.all
    # se adjunta el home por el header y el footer
    home = Home.objects.all
    context = {'vias': vias, 'home': home}
    return render(request, 'vias/vias.html', context)


def comentario(request, via_id):
    home = Home.objects.all
    data = {
        'form': Comentario_via(),
         'home': home,
    }
    if request.method == 'POST':
        formulario = Comentario_via(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Enviado"
        else:
            data["form"] = formulario
    return render(request, "vias/comentario_via.html", data)


def listar(request):
    home = Home.objects.all
    vistacoment = Comentario.object.all()
    data = {
        'vistacoment': vistacoment,
        'home': home,
    }
    return render(request, "vias/comentario_via.html", data,)


""" 
def listar(request, comentario_id):
    home = Home.objects.all
    listar = get_object_or_404(Comentario, pk=comentario_id)
    return render(request, 'anuncios/detalle_anuncio.html', {'listar': listar, 'home': home})
    
"""
