from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import ListView, TemplateView
# from django.views.generic.simple import redirect_to

# Votatu Views
from votatu.views import home
# from ley.views import ListaDeVotos #ListaDeLeyes
from votosecreto.views import ListaDeVotos #ListaDeLeyes

# TastyPie API
from tastypie.api import Api
from ley.api import LeyResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(LeyResource())

urlpatterns = patterns('',
    # Examples: 
    # url(r'^$', 'votatu.views.home', name='home'),

    ### LOGIN + SOCIAL AUTH ###
    url(r'^social/', include('social_auth.urls')),
    url(r'^perfil/$', TemplateView.as_view(template_name="registration/perfil.html"), name = 'perfil'),
    url(r'^perfil/', include('registration.backends.default.urls')),

    # url(r'^abrir-cuenta/', TemplateView.as_view(template_name="usuario/abrir_cuenta.html"), name = 'abrir-cuenta'),
    # url(r'^login/$', redirect_to, {

    ### CONTENIDO ESTATICO ###
    url(r'^acerca-de/', TemplateView.as_view(template_name="acerca-de.html"), name = 'acerca-de'),
    url(r'^ayuda/', TemplateView.as_view(template_name="ayudanos.html"), name = 'ayuda'),


    ### CONTENIDO DE APPS ###
    url(r'^$', ListaDeVotos.as_view(), name = 'home'),
    url(r'^ley/', include('votatu.apps.ley.url')),
    url(r'^vota/', include('votatu.apps.votosecreto.url')),
#    url(r'^congreso/', include('votatu.apps.congreso.url')),


    ### ADMIN  ###
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    ### API ###
    url(r'^api/', include(v1_api.urls)),
)

### this last line lets us see the 500 error at 127.0.0.1:8000/500
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),)

# para tener estilos correctos en el 500
handler500 = 'votatu.views.server_error'
