from django import forms
from videos import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets

class nuevoVideo(forms.ModelForm):
    class Meta:
        model= models.Video
        fields= ('titulo_video','descripcion_video','archivo_video','keywords_video','privacidad_video')


class nuevoComentario(forms.ModelForm):
    class Meta:
        model= models.Comentario
        fields= ('texto_comentario',)


class usuarioLogin(forms.Form):
    usuario=forms.CharField(help_text="Usuario",required=True)
    contrasenia=forms.CharField(widget=forms.PasswordInput(),help_text="Contrasenia",required=True)

    def __init__(self,*args,**kwargs):
        super(usuarioLogin,self).__init__(*args,**kwargs)

        self.fields['usuario'].widget.attrs.update({'required':True,'class':'form-control'})

        self.fields['contrasenia'].widget.attrs.update({'required':True,'class':'form-control'})
