from django.urls import path
from . import views

urlpatterns = [
    path('', views.HobbyListView.as_view(), name='hobbies_list'),
    path('agregar/', views.HobbyCreateView.as_view(), name='agregar_hobby'),
    path('editar/<int:pk>/', views.HobbyUpdateView.as_view(), name='editar_hobby'),
    path('eliminar/<int:pk>/', views.HobbyDeleteView.as_view(), name='eliminar_hobby'),
]
