# Mi Proyecto Django

## Estructura del proyecto

```
mi_proyecto/
│
├── manage.py
│
├── config/                        ← Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── inicio/                        ← App principal
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    ├── migrations/
    │
    ├── templates/
    │   ├── public/                ← Plantillas WAGGY (vista pública)
    │   │   ├── index.html         → /
    │   │   ├── book.html          → /book/
    │   │   └── login.html         → /login/
    │   │
    │   └── private/               ← Plantillas GURUABLE (vista privada)
    │       └── dashboard.html     → /dashboard/  (requiere login)
    │
    └── static/
        ├── public/                ← Archivos estáticos de WAGGY
        │   ├── css/
        │   │   ├── style.css
        │   │   └── normalize.css
        │   ├── js/
        │   │   └── script.js
        │   ├── images/
        │   │   └── (imágenes waggy)
        │   └── vendor/
        │       └── bootstrap-5.1.3/
        │
        └── private/               ← Archivos estáticos de GURUABLE
            ├── css/
            │   ├── bootstrap/
            │   ├── animate.css/
            │   └── style.css
            ├── js/
            ├── images/
            └── icon/
                ├── icofont/
                └── themify-icons/
```

## Cómo copiar los archivos estáticos

### Estáticos PÚBLICOS (waggy → static/public/)
Desde el ZIP `waggy-1.0.0/`, copia:
- `css/` y `style.css`       → `inicio/static/public/css/`
- `js/`                       → `inicio/static/public/js/`
- `images/`                   → `inicio/static/public/images/`
- `assets/vendor/`            → `inicio/static/public/vendor/`

### Estáticos PRIVADOS (guruable → static/private/)
Desde el ZIP `guruable-1.0.0/`, copia:
- `assets/css/`               → `inicio/static/private/css/`
- `assets/js/`                → `inicio/static/private/js/`
- `assets/images/`            → `inicio/static/private/images/`
- `assets/icon/`              → `inicio/static/private/icon/`

## Instalación y ejecución

```bash
# 1. Crear entorno virtual
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/Mac

# 2. Instalar dependencias
pip install django psycopg2-binary

# 3. Crear base de datos en PostgreSQL
#    (o cambia a sqlite3 en settings.py si prefieres)

# 4. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# 5. Crear superusuario para el panel privado
python manage.py createsuperuser

# 6. Ejecutar el servidor
python manage.py runserver
```

## URLs disponibles

| URL            | Vista           | Zona     |
|----------------|-----------------|----------|
| `/`            | Inicio (waggy)  | Pública  |
| `/book/`       | Reservas        | Pública  |
| `/login/`      | Login           | Pública  |
| `/logout/`     | Logout          | -        |
| `/dashboard/`  | Panel (guruable)| Privada  |
| `/admin/`      | Admin Django    | Privada  |
