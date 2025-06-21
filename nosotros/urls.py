from django.urls  import path
from . import views

urlpatterns = [
    path('', views.nosotros, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/', views.servicios, name='servicios'),
    path('galeriavideos/', views.galeriavideos, name='galeriavideos')
]
