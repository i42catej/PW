from django.forms import ModelForm
from django import forms
from .models import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CircunscripcionForm (forms.ModelForm):
	class Meta:
		model = Circunscripcion

class MesaForm (forms.ModelForm):
	class Meta:
		model = Mesa

class PartidoForm (forms.ModelForm):
	class Meta:
		model = Partido

class ResultadoForm (forms.ModelForm):
	class Meta:
		model = Resultado

class AuthenticationForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
		widgets = {
		'password': forms.PasswordInput(),
		}