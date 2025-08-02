# views.py
from django.shortcuts import render

def pasatiempos_agregar(request):
    # tu lógica aquí
    return render(request, 'hobbies/agregar.html')
