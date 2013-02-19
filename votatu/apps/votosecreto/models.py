from django.db import models
from django.utils.translation import ugettext_lazy as _

# votatu
from ley.models import Ley



class Token(models.Model):
    token_string = models.CharField(max_length=50,
                    blank = True, null = True,)
    # 489a9ef6fdb6da2f7c0fa8271d964463
    # will be a 32 char long md5(s).hexdigest()
    # of useragent and ip, or of username

    def __unicode__(self):
        return self.token_string


class Voto(models.Model):
    ley = models.ForeignKey(Ley)
    votos_si = models.IntegerField(_('internautas a favor'),
        blank = True, null = True,)
    votos_no = models.IntegerField(_('internautas en contra'),
        blank = True, null = True,)
    votos_abstencion = models.IntegerField(_('internautas que se abstienen'),
        blank = True, null = True,)


    
    
