from django.contrib import admin

from .models import Via, Comentario

class ViasAdmin(admin.ModelAdmin):
 list_display = ('titulo',)
 pass
admin.site.register(Via, ViasAdmin)
admin.site.register(Comentario, ViasAdmin)