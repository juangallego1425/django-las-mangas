from django.contrib import admin

# Register your models here.
from .models import Galeria

class GaleriaAdmin(admin.ModelAdmin):
 list_display = ('titulo',)
 pass
admin.site.register(Galeria, GaleriaAdmin)