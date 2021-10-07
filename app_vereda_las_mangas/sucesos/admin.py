from django.contrib import admin

# Register your models here.
from .models import Suceso

class SucesoAdmin(admin.ModelAdmin):
 list_display = ('titulo',)
 #list_select_related = ('titulo',)
 pass
admin.site.register(Suceso, SucesoAdmin)