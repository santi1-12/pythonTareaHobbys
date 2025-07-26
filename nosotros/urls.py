from django.urls  import path
from . import views

urlpatterns = [
    path('', views.nosotros, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/', views.servicios, name='servicios'),
    path('video/', views.video, name='video'),
    path('proyectos/', views.proyectos, name='proyectos'),
]
