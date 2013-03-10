# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from django.views.generic import ListView

from ley.views import ListaLeyesPrevias, LeyDetail, YaHaVotadoDetail, VotoEnviadoDetail


urlpatterns = patterns('',
                       url(r'^previas/$', ListaLeyesPrevias.as_view(), name = 'ley-previas'),
                       url(r'^(?P<slug>[-_\w]+)/$', LeyDetail.as_view(), name = 'ley-detail'),
                       url(r'^x/(?P<slug>[-_\w]+)/$', YaHaVotadoDetail.as_view(), name = 'ya-ha-votado'),
                       url(r'^v/(?P<slug>[-_\w]+)/$', VotoEnviadoDetail.as_view(), name = 'voto-enviado'),
                       )
