from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExperienciaListView.as_view(), name='experiencia_list'),
    path('agregar/', views.ExperienciaCreateView.as_view(), name='agregar_experiencia'),
    path('editar/<int:pk>/', views.ExperienciaUpdateView.as_view(), name='editar_experiencia'),
    path('eliminar/<int:pk>/', views.ExperienciaDeleteView.as_view(), name='eliminar_experiencia'),
]
