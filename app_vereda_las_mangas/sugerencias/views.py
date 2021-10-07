from django.shortcuts import render
from .forms import SugerenciaForm
from home.models import Home

def sugerencia(request):
    home = Home.objects.all

    data ={
        'form': SugerenciaForm(),
        'home': home,
    }
    if request.method == 'POST':
        formulario = SugerenciaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "Enviado"
        else:
            data["form"]= formulario
    return render (request, "sugerencias/sugerencias.html",data)