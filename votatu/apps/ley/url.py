from django.conf.urls import patterns, url, include
from django.views.generic import ListView

from ley.views import ListaLeyesPasadas

urlpatterns = patterns('',
                       url(r'^$', ListaLeyesPasadas.as_view(), name = 'votos-previos'),
                       )
