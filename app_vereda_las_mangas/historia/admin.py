from django.contrib import admin

# Register your models here.
from .models import Hisoria

class HistoriaAdmin(admin.ModelAdmin):
 list_display = ('titulo',)
 #list_select_related = ('titulo',)
 pass
admin.site.register(Hisoria, HistoriaAdmin)