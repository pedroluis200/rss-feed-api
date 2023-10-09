# Proyecto RSS FEED API

![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-blue.svg)
![Estado de Construcción](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.7%2B-green.svg)
![Django](https://img.shields.io/badge/Django-3.0%2B-green.svg)


Este proyecto es un **agregador de feeds RSS** desarrollado con Django REST Framework. Permite a los usuarios agregar sitios web RSS y ver los feeds recientes de esos sitios en un solo lugar. El objetivo principal de esta aplicación es simplificar la lectura de noticias y blogs al proporcionar un único punto de acceso para múltiples fuentes de noticias.

## Características principales

- **Agregar Feeds RSS**: Los usuarios pueden agregar fácilmente enlaces de sitios web RSS para agregarlos a su lista de fuentes de noticias.
- **Visualización de Feeds**: Los feeds RSS de los sitios agregados se presentan en una interfaz de usuario limpia y fácil de leer.
- **Actualizaciones Automáticas**: Los feeds se actualizan automáticamente en intervalos regulares para garantizar que los usuarios vean las últimas noticias.
- **Filtrado de Contenido**: Los usuarios pueden filtrar los feeds por palabras clave, categorías o cualquier otro criterio relevante.
- **API REST**: La aplicación proporciona una API REST para acceder a los feeds y la funcionalidad del sistema desde otras aplicaciones o servicios.

## Requisitos del Sistema

- Python 3.7 o superior
- Django 3.0 o superior
- Django REST Framework 3.11 o superior

## Pasos para Ejecutar el Proyecto

1. **Clonar el Repositorio**:
   
   git clone https://github.com/pedroluis200/rss-feed-api
   
3. **Configurar el Entorno Virtual**:

   python3 -m venv venv
   source venv/bin/activate # En Windows: venv\Scripts\activate

3. **Instalar Dependencias**:

   pip install -r requirements.txt

4. **Configurar la Base de Datos**:

   python manage.py migrate

5. **Crear un Superusuario** (opcional, pero útil para administrar el sitio):

   python manage.py createsuperuser

6. **Ejecutar el Servidor de Desarrollo**:

   python manage.py runserver

7. Accede a la interfaz de administrador en `http://localhost:8000/admin` (usando las credenciales del superusuario) para agregar feeds RSS y administrar el sistema.

## Endpoints de la API

- **Agregar Feed RSS**: `POST /api/add_rss_feed/`
- Parámetro: `website_url` (URL del sitio web RSS)
- **Obtener Todos los Feeds**: `GET /api/feeds/`
- **Obtener Detalles de un Feed Específico**: `GET /api/feeds/<feed_id>/`

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un *fork* del repositorio.
2. Crea una rama para tu característica o corrección: `git checkout -b nombre-de-la-rama`.
3. Realiza los cambios y haz *commit*: `git commit -m "Descripción del cambio"`.
4. Sube los cambios a tu *fork*: `git push origin nombre-de-la-rama`.
5. Abre un *pull request* en GitHub.
