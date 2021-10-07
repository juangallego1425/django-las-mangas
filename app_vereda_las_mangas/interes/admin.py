from django.contrib import admin

# Register your models here.
from .models import Interes

class InteresAdmin(admin.ModelAdmin):
 list_display = ('titulo',)
 pass
admin.site.register(Interes, InteresAdmin)