from django.shortcuts import render
from .models import proyecto, Habilidad

def mostrar_proyectos(request):
    proyectos = proyecto.objects.all()
    habilidades = Habilidad.objects.all()
    return render(request, 'portafolio/proyectos.html', {
        'proyectos': proyectos,
        'habilidades': habilidades
    })
