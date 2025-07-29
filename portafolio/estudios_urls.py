from django.urls import path
from . import views

urlpatterns = [
    path('', views.EstudioListView.as_view(), name='estudios_list'),
    path('agregar/', views.EstudioCreateView.as_view(), name='agregar_estudio'),
    path('editar/<int:pk>/', views.EstudioUpdateView.as_view(), name='editar_estudio'),
    path('eliminar/<int:pk>/', views.EstudioDeleteView.as_view(), name='eliminar_estudio'),
]
