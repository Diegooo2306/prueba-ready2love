# Proyecto Django: Login para Matchers

Este proyecto crea un login personalizado usando el sistema de autenticación de Django y PostgreSQL.

## Requisitos
- Python 3.10+
- PostgreSQL

## Pasos para correr el proyecto

1. Crear y activar el entorno virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias
```bash
pip install -r requirements.txt
```

3. Crear base de datos y usuario en PostgreSQL (ejemplo)
```bash
psql -U postgres
```
```sql
CREATE DATABASE prueba_db;
CREATE USER prueba_user WITH PASSWORD tu_password_segura;
GRANT ALL PRIVILEGES ON DATABASE prueba_db TO prueba_user;
\q
```

4. Configurar variables de entorno

Opción A: usar `.env`
```bash
cp .env.example .env
```
Edita `.env` con tus credenciales reales.

Opción B: exportar variables
```bash
export POSTGRES_DB=prueba_db
export POSTGRES_USER=prueba_user
export POSTGRES_PASSWORD=tu_password_segura
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
```

5. Ejecutar migraciones
```bash
python manage.py migrate
```

6. Crear superusuario
```bash
python manage.py createsuperuser
```

7. Ejecutar el servidor
```bash
python manage.py runserver
```

8. Probar en el navegador
- `http://127.0.0.1:8000/login/`
- `http://127.0.0.1:8000/dashboard/` (requiere login)

## Notas
- Si faltan variables de entorno de PostgreSQL, Django fallará con un mensaje claro en consola.
- La vista de login usa `authenticate()` + `login()` y está protegida con CSRF.
