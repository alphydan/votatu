from django.conf.urls import patterns, include, url
from django.views.generic import ListView, TemplateView

# Votatu Views
from votatu.views import home
from ley.views import ListaDeLeyes

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
    url(r'^$', ListaDeLeyes.as_view(), name = 'home'),
    url(r'^$', ListaDeLeyes.as_view(), name = 'home'),

    url(r'^ley/', include('votatu.apps.ley.url')),
    url(r'^acerca-de/', TemplateView.as_view(template_name="acerca-de.html"), name = 'acerca-de'),
    # url(r'^ayuda/', TemplateView.as_view(template_name="ayudanos.html"), name = 'ayuda'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # API
    url(r'^api/', include(v1_api.urls)),
)
