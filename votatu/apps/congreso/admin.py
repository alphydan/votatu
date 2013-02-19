# -*- coding: utf-8 -*-
from django.contrib import admin
from congreso.models import Diputado, VotoDiputado, Partido


# class LeyAdmin(admin.ModelAdmin):
#     filter_horizontal = ('country_of_distribution','wind_electrical', 'picture', 'certification' )
#     list_display = ('__unicode__', 'model_nr', 'rotor_diameter', )
#     search_fields = ( 'name',)


admin.site.register(Diputado)
admin.site.register(VotoDiputado)
admin.site.register(Partido)
