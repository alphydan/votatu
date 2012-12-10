## django stuff ##
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone


## votatu models ##
from ley.models import Ley

class LeyList(ListView):
    model = Ley
    context_object_name = 'ley'
    template_name = 'home.html'

    # def get_context_data(self, **kwargs):
    #     context = super(LeyList, self).get_context_data(**kwargs)
    #     context['time_left'] = Ley.objects.all().dia_y_hora_voto - timezone.now() #          self.all() # .dia_y_hora_voto - d.now()

    #     return context
                

