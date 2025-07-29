from django.db import models

# Create your models here.

class proyecto(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descripcion = models.TextField(verbose_name='Descripción')
    fecha = models.DateField()

    def __str__(self):  
        return self.titulo
 


class Habilidad(models.Model):
    NIVELES = [
         ('Básico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20, choices=NIVELES)

    def __str__(self):
        return f"{self.nombre} ({self.nivel})"



class Experiencia(models.Model):
    empresa = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"

class Estudio(models.Model):
    institucion = models.CharField(max_length=100)
    titulo = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"

class Hobby(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
