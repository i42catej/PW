from django.conf.urls import patterns, include, url
from eleccion import views
from .views import *

urlpatterns = patterns ('',

	#Ver y anadir circunscripcion con vistas basadas en clase
	url (r'^verCir', verCir.as_view(), name='Ver circunscripcion'),
	url (r'^addCir', login_required(addCir.as_view(),login_url='/login'), name='Anadir Ruta'),
	

	url (r'^detalleCir/(?P<id_circunscripcion>.*)', views.detalleCir, name='Detalle circunscripcion.'),
	
	#Eliminar y editar circunscripcion con vistas basadas en clase
	url('^eliminarCir/(?P<Circunscripcion_id>\w+)$', login_required(eliminarCir.as_view(),login_url='/login'), name='Eliminar cir.'),
	url('^editarCir/(?P<Circunscripcion_id>\w+)$', editarCir.as_view(), name='editar cir'),

	#A partir de aqui con funciones
	url (r'^addMesa', views.addMesa, name='Anadir mesa.'),
	url (r'^editarMesa/(?P<id_mesa>.*)', views.editarMesa, name='Editar mesa.'),
	url (r'^detalleMesa/(?P<id_mesa>.*)', views.detalleMesa, name='Detalle mesa.'),

	url (r'^addResultado', views.addResultado, name='Anadir resultado'),


	
)