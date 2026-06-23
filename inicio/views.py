from django.db.models import Count, Sum
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import CitaVeterinariaForm, LoginForm
from .models import CitaVeterinaria


# ─────────────────────────────────────────────
#  VISTAS PÚBLICAS  (usan templates/public/)
# ─────────────────────────────────────────────

def inicio(request):
    """Página principal pública — usa waggy (public/index.html)."""
    return render(request, 'public/index.html')


def book(request):
    """Formulario de cita veterinaria público."""
    success = False
    if request.method == 'POST':
        form = CitaVeterinariaForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = CitaVeterinariaForm()
    else:
        form = CitaVeterinariaForm()

    return render(request, 'public/book.html', {
        'form': form,
        'success': success,
    })


def login_view(request):
    """Login — página pública de acceso al área privada."""
    if request.user.is_authenticated:
        return redirect('dashboard')

    next_url = request.GET.get('next') or request.POST.get('next')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.username}!')
            if next_url and url_has_allowed_host_and_scheme(
                next_url, allowed_hosts={request.get_host()}
            ):
                return redirect(next_url)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()

    return render(request, 'public/login.html', {'form': form, 'next': next_url})


def logout_view(request):
    """Cerrar sesión."""
    logout(request)
    return redirect('inicio')


# ─────────────────────────────────────────────
#  VISTAS PRIVADAS  (usan templates/private/)
# ─────────────────────────────────────────────

@login_required
def dashboard(request):
    """Panel principal privado — usa guruable (private/dashboard.html)."""
    citas = CitaVeterinaria.objects.all()
    stats = CitaVeterinaria.objects.aggregate(
        citas_count=Count('id'),
    )
    return render(request, 'private/dashboard.html', {
        'citas': citas,
        'citas_count': stats['citas_count'],
    })
