from django.urls import include, path

urlpatterns = [
    path('', include('portafolio.home_urls')),
    path('proyectos/', include('portafolio.proyectos_urls')),
    path('experiencia/', include('portafolio.experiencia_urls')),
    path('estudios/', include('portafolio.estudios_urls')),
    path('hobbies/', include('portafolio.hobbies_urls')),
]
