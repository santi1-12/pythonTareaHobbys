from django.shortcuts import render
from .models import proyecto, Habilidad, Experiencia, Estudio, Hobby
from .forms import HabilidadForm, ExperienciaForm, EstudioForm, HobbyForm,proyectoForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


def index(request):
    # puedes pasar contexto si quieres
    return render(request, 'portafolio/index.html')

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


# Experiencia
class ExperienciaListView(ListView):
    model = Experiencia
    template_name = 'portafolio/experiencia_list.html'
    context_object_name = 'experiencias'

class ExperienciaCreateView(CreateView):
    model = Experiencia
    fields = ['empresa', 'puesto', 'descripcion']
    template_name = 'portafolio/form_generic.html'
    success_url = reverse_lazy('experiencia_list')

class ExperienciaUpdateView(UpdateView):
    model = Experiencia
    fields = ['empresa', 'puesto', 'descripcion'] 
    template_name = 'portafolio/form_generic.html'
    success_url = reverse_lazy('experiencia_list')

class ExperienciaDeleteView(DeleteView):
    model = Experiencia
    template_name = 'portafolio/confirm_delete.html'
    success_url = reverse_lazy('experiencia_list')

# Estudios
class EstudioListView(ListView):
    model = Estudio
    template_name = 'portafolio/estudios_list.html'
    context_object_name = 'estudios'

class EstudioCreateView(CreateView):
    model = Estudio
    fields = ['institucion', 'titulo', 'fecha_inicio', 'fecha_fin']
    template_name = 'portafolio/form_generic.html'
    success_url = reverse_lazy('estudios_list')

class EstudioUpdateView(UpdateView):
    model = Estudio
    fields = ['institucion', 'titulo', 'fecha_inicio', 'fecha_fin']
    template_name = 'portafolio/form_generic.html'
    success_url = reverse_lazy('estudios_list')

class EstudioDeleteView(DeleteView):
    model = Estudio
    template_name = 'portafolio/confirm_delete.html'
    success_url = reverse_lazy('estudios_list')

# Hobbies
class HobbyListView(ListView):
    model = Hobby
    template_name = 'portafolio/hobbies_list.html'
    context_object_name = 'hobbies'

class HobbyCreateView(CreateView):
    model = Hobby
    fields = ['nombre', 'descripcion']
    template_name = 'portafolio/form_generic.html'
    success_url = reverse_lazy('hobbies_list')

class HobbyUpdateView(UpdateView):
    model = Hobby
    fields = ['nombre', 'descripcion']
    template_name = 'portafolio/form_generic.html'
    success_url = reverse_lazy('hobbies_list')

class HobbyDeleteView(DeleteView):
    model = Hobby
    template_name = 'portafolio/confirm_delete.html'
    success_url = reverse_lazy('hobbies_list')

