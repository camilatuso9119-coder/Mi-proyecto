from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=120, verbose_name='Nombre')
    phone = models.CharField(max_length=30, verbose_name='Teléfono')
    email = models.EmailField(blank=True, verbose_name='Correo')
    address = models.CharField(max_length=255, blank=True, verbose_name='Dirección')
    people = models.PositiveSmallIntegerField(default=1, verbose_name='Personas')
    date = models.DateField(null=True, blank=True, verbose_name='Fecha')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.people} persona(s)'
