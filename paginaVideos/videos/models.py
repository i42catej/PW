from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
	titulo_video = models.CharField(max_length = 100, verbose_name = 'Titulo ', help_text = "Titulo ")
	descripcion_video = models.TextField(help_text = 'Descripcion ', verbose_name = 'Descripcion ')
	keywords_video = models.TextField(verbose_name = "Palabras de referencia", help_text = "Palabras de referencia")
	usuario_video = models.ForeignKey(User, verbose_name = 'Usuario ')
	archivo_video = models.FileField(upload_to = 'videos', help_text = "Seleccione un archivo", verbose_name = "Seleccione un archivo")
	fecha_video = models.DateTimeField(auto_now = True)
	privacidad_video = models.BooleanField(verbose_name = "Privado", default = False, help_text = "Privado")

	def __unicode__(self):
		return self.titulo_video + "Usuario: " + self.usuario_video.username

class Comentario(models.Model):
	video_comentario = models.ForeignKey(Video)
	texto_comentario = models.TextField(help_text = 'Comentario', verbose_name = "Comentario")
	usuario_comentario = models.ForeignKey(User, verbose_name = 'Autor')
	fecha_comentario = models.DateTimeField(auto_now=True, verbose_name= 'Fecha del Comentario')

	def __unicode__(self):
		return self.texto_comentario + "Usuario: " + self.usuario_comentario.username
