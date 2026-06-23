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
]
