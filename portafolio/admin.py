from django.contrib import admin
from .models import proyecto, Habilidad, Experiencia, Estudio, Hobby

admin.site.register(proyecto)
admin.site.register(Habilidad)
admin.site.register(Experiencia)
admin.site.register(Estudio)
admin.site.register(Hobby)