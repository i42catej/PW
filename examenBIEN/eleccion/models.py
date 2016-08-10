from django.db import models
#NUEVOOO TODO LO DE DEBAJO
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Circunscripcion(models.Model):
	escanos = models.IntegerField()
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
        	return self.nombre

class Mesa(models.Model):
	nombre = models.CharField(max_length=100)
	circunscripcion = models.ForeignKey(Circunscripcion)

	def __unicode__(self):
        	return self.nombre


class Partido(models.Model):
	nombre = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
        	return self.nombre


class Resultado(models.Model):
	numeroVotos = models.IntegerField()
	mesa = models.ForeignKey(Mesa)
	partido = models.ForeignKey(Partido)
	

	def __unicode__(self):
        	return unicode(self.numeroVotos)