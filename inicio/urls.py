from django.urls import path
from . import views

urlpatterns = [
    # ── Públicas ──────────────────────────────
    path('', views.inicio, name='inicio'),
    path('book/', views.book, name='book'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ── Privadas (requieren login) ─────────────
    path('dashboard/', views.dashboard, name='dashboard'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/nuevo/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:usuario_id>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:usuario_id>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),
]
