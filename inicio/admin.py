from django.contrib import admin
from .models import CitaVeterinaria


@admin.register(CitaVeterinaria)
class CitaVeterinariaAdmin(admin.ModelAdmin):
    list_display = ('nombre_mascota', 'nombre_dueno', 'telefono', 'email', 'tipo_mascota', 'fecha', 'created_at')
    list_filter = ('fecha',)
    search_fields = ('nombre_mascota', 'nombre_dueno', 'email', 'telefono')
