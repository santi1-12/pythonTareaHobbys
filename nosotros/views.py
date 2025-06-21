from django.shortcuts import render

def nosotros(request):
    return render(request, 'nosotros/index.html')  

def servicios(request):
    return render(request, 'nosotros/servicios.html')

def contacto(request):
    return render(request, 'nosotros/contacto.html')

def galeriavideos(request):
    return render(request, 'nosotros/galeriavideos.html')