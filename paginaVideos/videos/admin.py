from django.contrib import admin
from videos import models

# Register your models here.

admin.site.register(models.Video)
admin.site.register(models.Comentario)
