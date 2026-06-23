from django.db import models


class CitaVeterinaria(models.Model):
    nombre_mascota = models.CharField(max_length=120, verbose_name='Nombre de la mascota')
    nombre_dueno = models.CharField(max_length=120, verbose_name='Nombre del dueño')
    telefono = models.CharField(max_length=30, verbose_name='Teléfono')
    email = models.EmailField(blank=True, verbose_name='Correo')
    direccion = models.CharField(max_length=255, blank=True, verbose_name='Dirección')
    tipo_mascota = models.CharField(max_length=50, verbose_name='Tipo de mascota')
    fecha = models.DateField(null=True, blank=True, verbose_name='Fecha de cita')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cita Veterinaria'
        verbose_name_plural = 'Citas Veterinarias'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.nombre_mascota} - {self.nombre_dueno}'
