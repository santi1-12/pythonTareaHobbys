from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.mostrar_proyectos, name='mostrar_proyectos'),
#     path('agregar/', views.agregar_proyecto, name='agregar_proyecto'),
#     path('editar/<int:proyecto_id>/', views.editar_proyecto, name='editar_proyecto'),
#     path('eliminar/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),
# ]

urlpatterns = [
    # Página de inicio
    path('', views.index, name='index'),

    # Proyectos
    path('proyectos/', views.mostrar_proyectos, name='mostrar_proyectos'),
    path('proyectos/agregar/', views.agregar_proyecto, name='agregar_proyecto'),
    path('proyectos/editar/<int:proyecto_id>/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/eliminar/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),

    # Habilidades
    path('habilidades/agregar/', views.agregar_habilidad, name='agregar_habilidad'),
    path('habilidades/editar/<int:habilidad_id>/', views.editar_habilidad, name='editar_habilidad'),
    path('habilidades/eliminar/<int:habilidad_id>/', views.eliminar_habilidad, name='eliminar_habilidad'),

    # Experiencia
    path('experiencia/', views.ExperienciaListView.as_view(), name='experiencia_list'),
    path('experiencia/agregar/', views.ExperienciaCreateView.as_view(), name='agregar_experiencia'),
    path('experiencia/editar/<int:pk>/', views.ExperienciaUpdateView.as_view(), name='editar_experiencia'),
    path('experiencia/eliminar/<int:pk>/', views.ExperienciaDeleteView.as_view(), name='eliminar_experiencia'),

    # Estudios
    path('estudios/', views.EstudioListView.as_view(), name='estudios_list'),
    path('estudios/agregar/', views.EstudioCreateView.as_view(), name='agregar_estudio'),
    path('estudios/editar/<int:pk>/', views.EstudioUpdateView.as_view(), name='editar_estudio'),
    path('estudios/eliminar/<int:pk>/', views.EstudioDeleteView.as_view(), name='eliminar_estudio'),

    # Hobbies
    path('hobbies/', views.HobbyListView.as_view(), name='hobbies_list'),
    path('hobbies/agregar/', views.HobbyCreateView.as_view(), name='agregar_hobby'),
    path('hobbies/editar/<int:pk>/', views.HobbyUpdateView.as_view(), name='editar_hobby'),
    path('hobbies/eliminar/<int:pk>/', views.HobbyDeleteView.as_view(), name='eliminar_hobby'),
]