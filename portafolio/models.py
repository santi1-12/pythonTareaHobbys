from django.db import models

# Create your models here.

class proyecto(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descripcion = models.TextField(verbose_name='Descripción')
    fecha = models.DateField()

    def __str__(self):  
        return self.titulo
 