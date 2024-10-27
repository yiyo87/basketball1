from django.contrib import admin
from equipos.models import Equipo

# Register your models here.
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombreEquipo', 'ciudad', 'conferencia','estadio','anioFundacion')
admin.site.register(Equipo,EquipoAdmin)