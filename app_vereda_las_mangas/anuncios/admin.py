from django.contrib import admin

from .models import Anuncio

class AnuncioAdmin(admin.ModelAdmin):
 list_display = ('titulo',)
 pass
admin.site.register(Anuncio, AnuncioAdmin)