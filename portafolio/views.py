from django.shortcuts import render
from .models import proyecto, Habilidad
from .forms import proyectoForm
from .forms import HabilidadForm
from django.shortcuts import render, redirect, get_object_or_404

def mostrar_proyectos(request):
    proyectos = proyecto.objects.all()
    habilidades = Habilidad.objects.all()
    return render(request, 'portafolio/proyectos.html', {
        'proyectos': proyectos,
        'habilidades': habilidades
    })
# Agregar proyecto
def agregar_proyecto(request):
    if request.method == 'POST':
        form = proyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mostrar_proyectos')
    else:
        form = proyectoForm()
    return render(request, 'portafolio/agregar_proyecto.html', {'form': form})

# Editar proyecto
def editar_proyecto(request, proyecto_id):
    proyecto_instancia = get_object_or_404(proyecto, pk=proyecto_id)
    if request.method == 'POST':
        form = proyectoForm(request.POST, request.FILES, instance=proyecto_instancia)
        if form.is_valid():
            form.save()
            return redirect('mostrar_proyectos')
    else:
        form = proyectoForm(instance=proyecto_instancia)
    return render(request, 'portafolio/editar_proyecto.html', {'form': form})

# Eliminar proyecto
def eliminar_proyecto(request, proyecto_id):
    proyecto_instancia = get_object_or_404(proyecto, pk=proyecto_id)
    if request.method == 'POST':
        proyecto_instancia.delete()
        return redirect('mostrar_proyectos')
    return render(request, 'portafolio/confirmar_eliminar.html', {'proyecto': proyecto_instancia})




# Agregar Habilidad
def agregar_habilidad(request):
    if request.method == 'POST':
        form = HabilidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_proyectos')
    else:
        form = HabilidadForm()
    return render(request, 'portafolio/form_habilidad.html', {'form': form, 'titulo': 'Agregar Habilidad'})

# Editar Habilidad
def editar_habilidad(request, habilidad_id):
    habilidad = get_object_or_404(Habilidad, pk=habilidad_id)
    if request.method == 'POST':
        form = HabilidadForm(request.POST, instance=habilidad)
        if form.is_valid():
            form.save()
            return redirect('mostrar_proyectos')
    else:
        form = HabilidadForm(instance=habilidad)
    return render(request, 'portafolio/form_habilidad.html', {'form': form, 'titulo': 'Editar Habilidad'})

# Eliminar Habilidad
def eliminar_habilidad(request, habilidad_id):
    habilidad = get_object_or_404(Habilidad, pk=habilidad_id)
    if request.method == 'POST':
        habilidad.delete()
        return redirect('mostrar_proyectos')
    return render(request, 'portafolio/eliminar_habilidad.html', {'proyecto': habilidad, 'tipo': 'habilidad'})
