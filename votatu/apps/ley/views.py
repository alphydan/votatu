## django stuff ##
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone


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

