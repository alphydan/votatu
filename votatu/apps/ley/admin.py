# -*- coding: utf-8 -*-
from django.contrib import admin
from ley.models import Ley


class LeyAdmin(admin.ModelAdmin):
    # filter_horizontal = ('country_of_distribution','wind_electrical', 'picture', 'certification' )
    list_display = ('__unicode__', 'dia_y_hora_voto', )
#     search_fields = ( 'name',)


admin.site.register(Ley, LeyAdmin)
