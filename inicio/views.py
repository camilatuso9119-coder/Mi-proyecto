from django.db.models import Count
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import CitaVeterinariaForm, LoginForm, UsuarioPersonalizadoForm
from .models import CitaVeterinaria, UsuarioPersonalizado


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
    """Panel principal privado."""
    citas = CitaVeterinaria.objects.all()
    citas_count = citas.aggregate(total=Count('id'))['total']
    duenos_count = (
        citas.exclude(nombre_dueno='')
        .values('nombre_dueno')
        .distinct()
        .count()
    )

    return render(request, 'private/dashboard.html', {
        'citas': citas,
        'citas_count': citas_count,
        'duenos_count': duenos_count,
    })


@login_required
def lista_usuarios(request):
    """Lista de usuarios personalizados."""
    usuarios = UsuarioPersonalizado.objects.all()
    return render(request, 'private/usuarios/lista.html', {'usuarios': usuarios})


@login_required
def crear_usuario(request):
    """Crear nuevo usuario personalizado."""
    if request.method == 'POST':
        form = UsuarioPersonalizadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('lista_usuarios')
    else:
        form = UsuarioPersonalizadoForm()
    return render(request, 'private/usuarios/crear.html', {'form': form})


@login_required
def editar_usuario(request, usuario_id):
    """Editar usuario personalizado."""
    usuario = UsuarioPersonalizado.objects.get(id=usuario_id)
    if request.method == 'POST':
        form = UsuarioPersonalizadoForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('lista_usuarios')
    else:
        form = UsuarioPersonalizadoForm(instance=usuario)
    return render(request, 'private/usuarios/editar.html', {'form': form, 'usuario': usuario})


@login_required
def eliminar_usuario(request, usuario_id):
    """Eliminar usuario personalizado."""
    usuario = UsuarioPersonalizado.objects.get(id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente.')
        return redirect('lista_usuarios')
    return render(request, 'private/usuarios/eliminar.html', {'usuario': usuario})
