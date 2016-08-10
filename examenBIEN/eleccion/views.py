# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView


# Create your views here.
def userLogin(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            user = request.POST['username']
            passwd = request.POST['password']
            access = authenticate(username=user, password=passwd)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return redirect('/')
    else:
        formulario = AuthenticationForm()
    context = {'formulario': formulario}
    return render(request,'login.html', context)

@login_required(login_url='/login')
def userLogout(request):
    logout(request)
    return redirect('/')


class verCir(View):
    template_name = 'verCir.html'
    def get(self, request, *args, **kwargs):
       cir= Circunscripcion.objects.all()
       context={'cir':cir,'titulo':"Circunscripciones"}
       return render(request, self.template_name, context)


class addCir(View):

	    form_class = CircunscripcionForm
	    template_name = 'formulario.html'

	    def get(self, request, *args, **kwargs):
	    	if request.user.is_staff:
	    		formulario = self.form_class()
	    		context={'formulario': formulario,'titulo':"Añadir Circunscripcion"}
	    		return render(request, self.template_name, context)
	    	else:
	    		return HttpResponseRedirect('/login')

	    def post(self, request, *args, **kwargs):
	    	if request.user.is_staff:
	    		formulario = self.form_class(request.POST, request.FILES)
	    		if formulario.is_valid():
	    			formulario.save()
	    			return HttpResponseRedirect('/eleccion/verCir')

	    		context={'formulario': formulario,'titulo':"Añadir Circunscripcion "}
	    		return render(request, self.template_name,context)
	    	else:
				return HttpResponseRedirect('/login')



@login_required(login_url="/login")
def addMesa(request):
	if request.user.is_staff:
		mesa = Mesa()
		formulario = MesaForm(request.POST or None, instance = mesa)
		context = {'formulario':formulario,'titulo':"Añadir mesa"}

		if request.method == 'POST':
			if formulario.is_valid():
				formulario.save()
				return HttpResponseRedirect('/eleccion/verCir')

		return render_to_response('formulario.html',context,context_instance = RequestContext(request))
	else:
		return render_to_response('permisos.html')

	



def detalleCir(request,id_circunscripcion):
	cir= get_object_or_404(Circunscripcion, pk = id_circunscripcion)

	mesa=Mesa.objects.all().filter(circunscripcion=cir)
	

	context={'cir':cir,'mesa':mesa,'titulo':"Mesas de circunscripcion"}
	return render(request,'detalleCir.html',context)

def detalleMesa(request,id_mesa):
	mesa= get_object_or_404(Mesa, pk = id_mesa)
	context={'mesa':mesa,'titulo':"Mesas de circunscripcion"}
	
	return render(request,'detalleMesa.html',context)

@login_required(login_url='/login')
def editarMesa(request, id_mesa ):
	mesa = get_object_or_404(Mesa, pk = id_mesa)
	formulario = MesaForm(request.POST or None, instance = mesa)

	if request.method == 'POST':
		if formulario.is_valid():
			formulario.save()
           	return HttpResponseRedirect('/eleccion/verCir')
	else:
		context = { 'formulario': formulario,'titulo':"Editar mesa"}
	return render_to_response('formulario.html', context,  context_instance=RequestContext(request))


@login_required(login_url="/login")
def addResultado(request):
	resultado = Resultado()
	formulario = ResultadoForm(request.POST or None, instance = resultado)
	context = {'formulario':formulario,'titulo':"Añadir resultado"}

	if request.method == 'POST':
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')

	return render_to_response('formulario.html',context,context_instance = RequestContext(request))


class editarCir(View):

	template_name ='formulario.html'


	def get(self, request, *args, **kwargs):
	    if request.user.is_staff:
	    	id = self.kwargs['Circunscripcion_id']
        	cir = get_object_or_404(Circunscripcion, pk = id)
	    	formulario = CircunscripcionForm(request.POST or None, instance = cir)
	    	context={'formulario': formulario,'titulo':"editar Circunscripcion"}
	    	return render(request, self.template_name, context)
	    else:
	    	return HttpResponseRedirect('/login')

	def post(self, request, *args, **kwargs):
		if request.user.is_staff:
			id = self.kwargs['Circunscripcion_id']
			cir = get_object_or_404(Circunscripcion, pk = id)
			formulario = CircunscripcionForm(request.POST or None, instance = cir)

			if formulario.is_valid():
				formulario.save()
				return HttpResponseRedirect('/eleccion/verCir')

			context={'formulario': formulario,'titulo':"Añadir Circunscripcion "}
			return render(request, self.template_name,context)

		else:
			return HttpResponseRedirect('/login')


class eliminarCir(View):
	
	def get(self, request, *args, **kwargs):
		id = self.kwargs['Circunscripcion_id']
		cir = get_object_or_404(Circunscripcion, pk = id)
		cir.delete()

		return HttpResponseRedirect('/eleccion/verCir')
