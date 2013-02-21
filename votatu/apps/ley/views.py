## django stuff ##
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.template import RequestContext
from django.utils import timezone

## votatu models ##
from ley.models import Ley
from votosecreto.models import Voto


class ListaDeLeyes(ListView):
    queryset = Ley.objects.filter(dia_y_hora_voto__gte=timezone.now()).order_by('dia_y_hora_voto')[:5]
    context_object_name = 'ley'
    template_name = 'home.html'


class ListaLeyesPasadas(ListView):
    queryset = Ley.objects.filter(dia_y_hora_voto__lte=timezone.now()).order_by('dia_y_hora_voto')
    context_object_name = 'ley'
    template_name = 'ley/votos-previos.html'
    # http://www.congreso.es/portal/page/portal/Congreso/Congreso/Actualidad/Votaciones

class LeyDetail(DetailView):
    model = Ley
    template_name = 'ley/ley_detail.html'
    context_object_name = 'ley'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LeyDetail, self).get_context_data(**kwargs)
        ley_slug = kwargs['object'].slug
        context['voto'] = get_object_or_404(Voto, ley__slug = ley_slug)
        return context

class YaHaVotadoDetail(DetailView):
    model = Ley
    template_name = 'ley/ley_detail.html'
    context_object_name = 'ley'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(YaHaVotadoDetail, self).get_context_data(**kwargs)
        ley_slug = kwargs['object'].slug
        context['ya_ha_votado'] = 1
        context['voto'] = get_object_or_404(Voto, ley__slug = ley_slug)
        return context

class VotoEnviadoDetail(DetailView):
    model = Ley
    template_name = 'ley/ley_detail.html'
    context_object_name = 'ley'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(VotoEnviadoDetail, self).get_context_data(**kwargs)
        ley_slug = kwargs['object'].slug
        context['enviado'] = 1
        context['voto'] = get_object_or_404(Voto, ley__slug = ley_slug)
        return context





# def vote(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the poll voting form.
#         return render_to_response('polls/detail.html', {
#             'poll': p,
#             'error_message': "You didn't select a choice.",
#         }, context_instance=RequestContext(request))
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))






