from django.contrib import admin

# Register your models here.
from .models import Actividad

class ActividadAdmin(admin.ModelAdmin):
 list_display = ('titulo',)
 pass
admin.site.register(Actividad, ActividadAdmin) 