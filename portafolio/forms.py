from django import forms
from .models import proyecto, Habilidad

class proyectoForm(forms.ModelForm):
    class Meta:
        model=proyecto
        fields= ["titulo", "descripcion", "fecha"]



class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = ["nombre","nivel"]
