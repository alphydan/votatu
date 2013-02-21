# -*- coding: utf-8 -*-
from django.contrib import admin
from votosecreto.models import Token, Voto

class VotoAdmin(admin.ModelAdmin):
    # filter_horizontal = ('token',)
    list_display = ('__unicode__', 'voto_ley_slug', )
    


admin.site.register(Voto , VotoAdmin)
admin.site.register(Token)
