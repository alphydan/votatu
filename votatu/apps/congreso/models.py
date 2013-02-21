from django.db import models
from django.utils.translation import ugettext_lazy as _

# votatu
from ley.models import Ley


class Partido(models.Model):
    nombre = models.CharField(max_length=110)

    def __unicode__(self):
        return self.nombre

class Comision(models.Model):
    nombre = models.CharField(max_length=110)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Comisiones'


class SubComision(models.Model):
    nombre = models.CharField(max_length=110)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Subcomisiones'



class Diputado(models.Model):
    '''miembro "electo" del congreso'''
    nombre = models.CharField(_('Nombre'), max_length=50)
    apellidos = models.CharField(_('Apellidos'), max_length=50)
    asiento = models.SmallIntegerField(_('Asiento'),
                    blank = True, null = True,) #hay 350 asientos en total
    partido = models.ForeignKey(Partido,
                    blank = True, null = True,)
    comision = models.ManyToManyField(Comision,
                    blank = True, null = True,)
    subcomision = models.ManyToManyField(SubComision,
                    blank = True, null = True,)

    def __unicode__(self):
        return 'Diputad@: %s - %s ' % (self.nombre, self.apellidos)

    class Meta:
        verbose_name_plural = 'Diputad@s'


class VotoDiputado(models.Model):
    '''voto que cada Diputado ha hecho'''
    ley = models.ForeignKey(Ley,
            verbose_name=_('Ley Votada'),
            related_name='%(class)s_slug',)
    diputado = models.ForeignKey(Diputado)
    SELECCION = ((0, _('abstencion')),
                 (-99, _('ausente')),
                 (1, _('si')),
                 (-1, _('no')),
                 )
    seleccion = models.SmallIntegerField(choices=SELECCION,
                    blank = True, null = True,)
    
