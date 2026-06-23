from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CitaVeterinaria, UsuarioPersonalizado


class CitaVeterinariaForm(forms.ModelForm):
    class Meta:
        model = CitaVeterinaria
        fields = ['nombre_mascota', 'nombre_dueno', 'telefono', 'email', 'direccion', 'tipo_mascota', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }


class UsuarioPersonalizadoForm(forms.ModelForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['nombre', 'rol']


class LoginForm(AuthenticationForm):
    """Formulario de login personalizado."""
    pass
