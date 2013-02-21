# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from django.views.generic import ListView, TemplateView

from votosecreto.views import un_voto

urlpatterns = patterns('',
#    url(r'^$', TemplateView.as_view(template_name ="acerca-de.html")),
#    url(r'^(?P<object_id>[-\w]+)/(?P<votenr>\d)/$', un_voto, name='un-voto'),
    url(r'^(?P<slug_ley>[-\w]+)/$', un_voto, name='un-voto'),
)

