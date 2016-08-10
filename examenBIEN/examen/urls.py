from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from eleccion import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'examen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'), #NUEVO
    url(r'^admin/', include(admin.site.urls)),

    url(r'^eleccion/', include ('eleccion.urls', namespace = 'eleccion')),

    url (r'^login', views.userLogin, name='Login'),
    url (r'^logout', views.userLogout, name='Logout'),
)
