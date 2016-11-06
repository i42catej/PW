from django.shortcuts import render, get_object_or_404
from videos import models, forms
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from django.core.context_processors import csrf

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def verVideo(request,id_video):

    video=get_object_or_404(models.Video, pk=id_video)
    comentarios=models.Comentario.objects.filter(video_comentario=video).order_by("fecha_comentario").reverse()

    formulario=forms.nuevoComentario(request.POST or None)

    if formulario.is_valid():
        usuario=get_object_or_404(models.User,pk=request.POST['id_usuario'])
        nuevoV=formulario.save(commit=False)
        nuevoV.video_comentario=video
        nuevoV.usuario_comentario=usuario
        nuevoV.save()

    return render(request,'verVideo.html',{'idvideo':id_video,'titulo':"Mostrar video",'video':video,'comentarios':comentarios,'formulario':formulario})

def mostrarResultados(request):

    r=models.Video.objects.all().filter(privacidad_video=False)

    if 'campo' in request.GET and request.GET['campo']:

        campo=request.GET['campo']

        for i in campo.split():
            r=r.filter(keywords_video__contains=i)

    else:
        campo=""

    return render(request,'mostrarResultados.html',{'titulo':"Muestra de Resultados", 'resultados':r})

def subirVideo(request):

    formulario=forms.nuevoVideo(request.POST,request.FILES or None)
    if 'id_usuario' in request.POST and request.POST['id_usuario']:
        usuario=get_object_or_404(models.User,pk=request.POST['id_usuario'])

        if formulario.is_valid():
            nuevoV=formulario.save(commit=False)
            nuevoV.usuario_video=usuario
            nuevoV.save()

            return render(request, 'subirVideo.html',{'formulario':formulario, 'booleano':True,'titulo':"Formulario valido"})
        else:
            return render(request, 'subirVideo.html',{'formulario':formulario, 'booleano':False,'titulo':"Formulario no valido"})


    return render(request, 'subirVideo.html',{'formulario':formulario,'titulo':"Subir Video"})


def mostrarPrincipal(request):

    r=models.Video.objects.all().filter(privacidad_video=False)

    return render(request,'mostrarResultados.html',{'titulo':"Pagina principal", 'resultados':r})


def usuario_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



def usuario_login(request):

    formulario=forms.usuarioLogin(request.POST or None)

    if formulario.is_valid():

        loger=authenticate(username=request.POST['usuario'], password=request.POST['contrasenia'])

        if loger:
            if loger.is_active:
                login(request,loger)
                return HttpResponseRedirect('/')

    return render(request,'login.html',{'formulario':formulario, 'titulo':"Formulario de login"})

def registro_usuario(request):

    if request.method == 'POST':
        usuario=UserCreationForm(request.POST)

        if usuario.is_valid():
            if request.POST['password1'] == request.POST['password2']:
                usuario.save()
                return HttpResponseRedirect('/')

    formulario={}
    formulario.update(csrf(request))
    formulario=UserCreationForm(request.POST or None)

    return render(request,'formulario_registro.html',{'formulario':formulario,'titulo':"Registro"})
