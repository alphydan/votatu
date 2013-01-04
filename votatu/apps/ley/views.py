## django stuff ##
from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone

## app secretballot ##
from secretballot.views import vote
from secretballot.models import Vote

## votatu models ##
from ley.models import Ley



class ListaDeLeyes(ListView):
    queryset = Ley.objects.filter(dia_y_hora_voto__gte=timezone.now()).order_by('dia_y_hora_voto')[:5]
    context_object_name = 'ley'
    template_name = 'home.html'


class ListaLeyesPasadas(ListView):
    queryset = Ley.objects.filter(dia_y_hora_voto__lte=timezone.now()).order_by('dia_y_hora_voto')
    context_object_name = 'ley'
    template_name = 'votos-previos.html'
    # http://www.congreso.es/portal/page/portal/Congreso/Congreso/Actualidad/Votaciones



class DetailLey(DetailView):
    model = Ley
    template_name = 'ley_detail.html'
    context_object_name = 'ley'





# def un_voto(request, slug):
#     ley = Ley.objects.from_request(request).get(pk=slug)
    # story has the following extra attributes
    # user_vote: -1, 0, or +1
    # total_upvotes: total number of +1 votes
    # total_downvotes: total number of -1 votes
    # vote_total: total_upvotes-total_downvotes
    # votes: related object manager to get specific votes (rarely needed)


def un_voto(request, object_id, votenr):

    unaley = get_object_or_404(Ley, pk=object_id)
    negative_votes = Vote.objects.filter(content_type = Ley, object_id = object_id, vote=-1).count()
    positive_votes = Vote.objects.filter(content_type = Ley, object_id = object_id, vote=1).count()
    resultado = positive_votes-negative_votes
    
    extra_context = dict()
    extra_context['ley'] = unaley
    extra_context['negative_votes'] = negative_votes
    extra_context['positive_votes'] = positive_votes
    extra_context['resultado'] = resultado
    extra_context['votenr'] = votenr

    return vote(request, content_type = 'ley.Ley', object_id = object_id, vote = votenr,
                extra_context = extra_context,
                template_name = 'vote_confirmation.html',)



# def vote(request, content_type, object_id, vote,
#      redirect_url=None, template_name=None, template_loader=loader,
#      extra_context=None, context_processors=None, mimetype=None):


