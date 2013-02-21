# -*- coding: utf-8 -*-
# python stuff
try:
    from hashlib import md5
except ImportError:
    from md5 import md5

## django stuff ##
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# from django.contrib.auth.models import User

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone

## votatu models ##
from votosecreto.models import Voto
from ley.models import Ley


def un_voto(request, slug_ley):
    try:
        seleccion = request.POST['seleccion'] #1:a favor, -1:en contra
        # identificar el voto por la "slug" de la ley
        voto_votado = get_object_or_404(Voto, ley__slug = slug_ley)
    except (KeyError, Voto.DoesNotExist): # si se abre /vota/<slug> sin hacer POST.
        # redireccion a la URL de la ley
        return HttpResponseRedirect(reverse('ley-detail', args=(slug_ley,)))

    token_voto = generate_token(request) # hash que identifica al votante

    # si existe el token hash(usuario+email ó IP+user-agent) actual para esta ley:
    if Voto.objects.filter(ley__slug = slug_ley).filter( token__token_string__exact = token_voto):
        return HttpResponseRedirect(reverse('ya-ha-votado', args=(slug_ley,)))
    else:
        # crear y guardar un nuevo token asociado a ese voto
        voto_votado.token.create(
        token_string = generate_token(request),
        )
        if int(seleccion) > 0:
            voto_votado.votos_si += 1
        if int(seleccion) < 0:
            voto_votado.votos_no += 1
        voto_votado.save()
        return HttpResponseRedirect(reverse('voto-enviado', args=(slug_ley,)))
        print 'el token %s no ha votado aun' % token_voto


def generate_token(request):
    # si el usuario está logeado, crear un token con nombre e email.
    if request.user.is_authenticated():
        s = ''.join((request.user.username, request.user.email))
    else:
    # si el usuario no está logeado, mirar su ip y user-agent y crear token.
        s = ''.join((request.META['REMOTE_ADDR'], request.META['HTTP_USER_AGENT']))
    return md5(s).hexdigest()


class ListaDeVotos(ListView):
    queryset = Voto.objects.filter(ley__dia_y_hora_voto__gte=timezone.now()).order_by('ley__dia_y_hora_voto')[:3]
    context_object_name = 'voto'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeVotos, self).get_context_data(**kwargs)
        context['ley'] = Ley.objects.filter(dia_y_hora_voto__gte=timezone.now()).order_by('dia_y_hora_voto')[3:6]
        return context







    
