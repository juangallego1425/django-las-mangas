from django.contrib import admin

# Register your models here.
from .models import Sugerencia

class SugerenciaAdmin(admin.ModelAdmin):
 list_display = ('titulo',)
 #list_select_related = ('titulo',)
 pass
admin.site.register(Sugerencia, SugerenciaAdmin)