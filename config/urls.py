from django.contrib import admin
from django.urls import path, include

# Título del panel de administración en español
admin.site.site_header = 'Administración'
admin.site.site_title = 'Panel de control'
admin.site.index_title = 'Bienvenido al panel de administración'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
]
