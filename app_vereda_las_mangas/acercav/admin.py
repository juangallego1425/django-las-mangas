from django.contrib import admin

# Register your models here.
from .models import Acerca

class AcercaAdmin(admin.ModelAdmin):
 list_display = ('titulo',)
 #list_select_related = ('titulo',)
 pass
admin.site.register(Acerca, AcercaAdmin)