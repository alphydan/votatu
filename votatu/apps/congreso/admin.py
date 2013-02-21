# -*- coding: utf-8 -*-
from django.contrib import admin
from congreso.models import Diputado, VotoDiputado, Partido, Comision, SubComision


class DiputadoAdmin(admin.ModelAdmin):
     filter_horizontal = ('comision','subcomision')


#     list_display = ('__unicode__', 'model_nr', 'rotor_diameter', )
#     search_fields = ( 'name',)


admin.site.register(Diputado, DiputadoAdmin)
admin.site.register(VotoDiputado)
admin.site.register(Partido)
admin.site.register(Comision)
admin.site.register(SubComision)
