from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from videos import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'paginavideo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}), #FALTA POR HACER
    url(r'^mostrarresultados/$', views.mostrarResultados),
    url(r'^subirvideo/$',views.subirVideo),
    url(r'^ver/(?P<id_video>.*)/$',views.verVideo),
    url(r'^$',views.mostrarPrincipal),
    url(r'^logout/$',views.usuario_logout),
    url(r'^login/$',views.usuario_login),
    url(r'^registro/$',views.registro_usuario),
)
