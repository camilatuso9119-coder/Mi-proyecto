from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'people', 'date', 'created_at')
    list_filter = ('date',)
    search_fields = ('name', 'email', 'phone')
