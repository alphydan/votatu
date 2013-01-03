from django.conf.urls import patterns, url, include
from django.views.generic import ListView

from ley.models import Ley
from secretballot.views import vote
from ley.views import ListaLeyesPasadas, DetailLey, un_voto

urlpatterns = patterns('',
                       url(r'^$', ListaLeyesPasadas.as_view(), name = 'votos-previos'),
                       url(r'^ley/(?P<slug>[-_\w]+)/$', DetailLey.as_view(), name = 'ley-detail'),
                       url(r'^voto/(?P<object_id>[-\w]+)/(?P<votenr>[-\w]+)/$', un_voto, name = 'un-voto'),
                       )
