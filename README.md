 ##### Julian Salas #########

# Entrega Final - Proyecto Django

## Video visita al sitio

https://drive.google.com/file/d/17_HhctwlQJtv9h2I3stdBXZBCO9L9ro6/view?usp=sharing

## Descripción

Este es el proyecto final para la cursada de Python de CoderHouse, desarrollado por Julian Salas. El proyecto consiste en una aplicación web para la gestión de perfiles de universidades, docentes, alumnos y envíos. Permite agregar, editar y visualizar información relevante de cada perfil.

## Usuario con permisos:
user: julian
pass: julian123

## Requisitos

- Python 3.8 o superior
- Django 4.1 o superior
- Dependencias listadas en `requirements.txt`

## Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

1. **Clonar el repositorio:**

    ```pwsh
    git clone https://github.com/JulianSalas2/Entrega-Final-JulianSalas.git
    ```

2. **Navegar al directorio del proyecto:**

    ```pwsh
    cd .\Entrega-Final-JulianSalas\
    cd .\Tercera-pre-entrega-JulianSalas\

    Esto es debido a que la tercera pre entrega se utilizo como base para la entrega final
    ```

3. **Crear un entorno virtual e instalar las dependencias:**

    ```pwsh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

4. **Configurar la base de datos:**

    ```pwsh
    python manage.py migrate
    ```

5. **Crear un superusuario para el panel de administración (opcional):**

    ```pwsh
    python manage.py createsuperuser
    ```

6. **Iniciar el servidor de desarrollo:**

    ```pwsh
    python manage.py runserver
    ```

## Uso

1. **Acceder a la aplicación:**

    Abre tu navegador web y dirígete a [(http://127.0.0.1:8000//)).

2. **Navegar por la aplicación:**

    - **Página de inicio:** Visualiza la primera view del sitio.
    - **Formulario de registro:** Permite añadir nuevos perfiles.
    - **Panel de administración:** Accede al panel para gestionar perfiles y configuraciones (accesible en [(http://127.0.0.1:8000/admin/)).
    - **Páginas Buscar Universidades, Docentes, Almnos, Universidades , Envios:** Visualiza los detalles de cada uno de las categorias.

## Contribución

1. **Hacer un fork del repositorio.**
2. **Crear una nueva rama para tus cambios:**

    ```pwsh
    git checkout -b nombre-de-la-rama
    ```

3. **Realizar tus cambios y hacer commits:**

    ```pwsh
    git add .
    git commit -m "Descripción de los cambios"
    ```

4. **Pushear los cambios a tu fork:**

    ```pwsh
    git push origin nombre-de-la-rama
