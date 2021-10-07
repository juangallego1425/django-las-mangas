from django.contrib import admin

# Register your models here.
from .models import Home, Imagenes

admin.site.register(Home)
class ImagenesAdmin(admin.ModelAdmin):
 list_display = ('titulo',)
 list_filter = ('titulo',)
 list_select_related  = ('actividad_id',)
 pass
admin.site.register(Imagenes, ImagenesAdmin)