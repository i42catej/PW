from django.contrib import admin
#NUEVO A PARTIR DE AQUI
from eleccion.models import *

# Register your models here.
admin.site.register(Circunscripcion)
admin.site.register(Mesa)
admin.site.register(Partido)
admin.site.register(Resultado)