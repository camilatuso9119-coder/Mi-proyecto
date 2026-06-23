from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'email', 'address', 'people', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class LoginForm(AuthenticationForm):
    """Formulario de login personalizado."""
    pass
