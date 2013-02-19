# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

# apps
import secretballot # for voting

# Create your models here.


class Ley(models.Model):
    '''iniciativa legistlativa en el congreso'''

    tipo_ley =  models.CharField(_(u'Tipo de ley'), 
            max_length = 200,
            help_text = _(u'Tipo de ley: Proyecto de Ley, Proposición de Ley, Real Decreto, etc ...'))

    titulo =  models.CharField(_(u'Título de la ley'), 
            max_length = 400,
            help_text = _(u'¿Cuál es el título de la ley sometida a voto?'))

    numero =  models.CharField(_(u'Número de ley'), 
            max_length = 20,
            help_text = _(u'Número de ley en formato: 121/000029'))

    slug = models.SlugField(_(u'Slug'),
            blank = True, null=True,
            help_text = _(u'Si no se añade manualmente se convertirá el número 121/000029 en slug 121-000029'),)

    dia_y_hora_voto = models.DateTimeField(_(u'Día y hora del voto'), blank = True, null = True,
            help_text = _(u'Día y Hora en que concluye el voto en el Parlamento'),)

    descripcion = models.TextField(_(u'Descripción de la ley'), 
            blank = True, null = True, 
            help_text = _(u'Primeros parrafos de la ley en questión'))
            # allow paragraph formatting and use "safe"

    texto_completo_html = models.URLField(_('URL del texto completo (HTML)'),
            help_text =_('Pagina web del parlamento que contiene el texto completo en formato HTML.'),
            blank=True, null = True,
            max_length = 500,)

    texto_completo_pdf = models.URLField(_('URL del texto completo (PDF)'),
            help_text =_('Pagina web del parlamento que contiene el texto completo en formato PDF.'),
            blank=True, null = True,
            max_length = 500,)
    
    autor = models.CharField(_(u'Autor o Autores de la ley'),
            max_length = 300,
            blank = True, null = True,
            help_text = _(u'Autores de la ley (Gobierno, Un nombre, Un colectivo)'))

    votos_si =  models.SmallIntegerField(_(u'Diputados a favor'), 
                        null = True, blank = True,)
    votos_no =  models.SmallIntegerField(_(u'Diputados en contra'), 
                        null = True, blank = True,)
    votos_abs =  models.SmallIntegerField(_(u'Número de abstenciones'), 
                        null = True, blank = True,)
    votos_aus =  models.SmallIntegerField(_(u'Número de diputados ausentes'), 
                        null = True, blank = True,)


    def __unicode__(self):
        return 'Ley %s - %s ' % (self.numero, self.titulo)

    def save(self, *args, **kwargs):
        if not self.slug:
            if self.numero:
                self.slug = "%s" % slugify(self.numero)
            elif not self.numero and self.titulo:
                self.slug = "%s" % slugify(self.titulo)
            else:
                self.slug =self.id
        return super(Ley, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Leyes'












secretballot.enable_voting_on(Ley)
