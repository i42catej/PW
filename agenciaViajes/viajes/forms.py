from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DestinoForm (forms.ModelForm):
	class Meta:
		model = Destino

class ViajeForm (forms.ModelForm):
	class Meta:
		model = Viaje

class RutaForm (forms.ModelForm):
    class Meta:
        model = Ruta
        
class AuthenticationForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
		widgets = {
		'password': forms.PasswordInput(),
		}
