from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_proyectos, name='mostrar_proyectos'),
    path('agregar/', views.agregar_proyecto, name='agregar_proyecto'),
    path('editar/<int:proyecto_id>/', views.editar_proyecto, name='editar_proyecto'),
    path('eliminar/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),

    path('habilidad/agregar/', views.agregar_habilidad, name='agregar_habilidad'),
    path('habilidad/editar/<int:habilidad_id>/', views.editar_habilidad, name='editar_habilidad'),
    path('habilidad/eliminar/<int:habilidad_id>/', views.eliminar_habilidad, name='eliminar_habilidad'),
]
