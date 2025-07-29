from django import forms
from .models import proyecto, Habilidad, Experiencia, Estudio, Hobby

class proyectoForm(forms.ModelForm):
    class Meta:
        model=proyecto
        fields= ["titulo", "descripcion", "fecha"]



class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = ["nombre","nivel"]


class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['empresa', 'puesto', 'descripcion', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class EstudioForm(forms.ModelForm):
    class Meta:
        model = Estudio
        fields = ['institucion', 'titulo', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }