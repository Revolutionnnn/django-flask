<h1>API de Estudiantes</h1>
Este es un proyecto de una API para administrar información de estudiantes, desarrollada con Django Rest Framework y PostgresSQL como base de datos.

El frontend fue creado con Bootstrap 5 y Flask, permitiendo realizar operaciones CRUD de manera sencilla. Además, se utiliza JWT Token para proteger las rutas y asegurar la seguridad de la información.

<h2>Instalación</h2>
Para instalar y ejecutar la aplicación en su máquina local, siga los siguientes pasos:

Clonar el repositorio: git clone https://github.com/Revolutionnnn/django-flask.

Crear y activar un entorno virtual para la aplicación: python3 -m venv venv y source venv/bin/activate.

Instalar las dependencias del proyecto: pip install -r requirements.txt.

Crear la base de datos en PostgresSQL y actualizar la configuración en settings.py.

Realizar las migraciones: python manage.py migrate.

Crear un superusuario para acceder al panel de administración de Django: python manage.py createsuperuser.

Ejecutar el servidor de desarrollo: python manage.py runserver.


<h2>Endpoints</h2>
GET /api/estudiantes/: Devuelve una lista de todos los estudiantes registrados.

POST /api/estudiantes/: Crea un nuevo estudiante.

GET /api/estudiantes/<id>/: Devuelve la información de un estudiante específico.
  
PUT /api/estudiantes/<id>/: Actualiza la información de un estudiante.
  
DELETE /api/estudiantes/<id>/: Elimina un estudiante.
 
<h2>Autenticación y Seguridad</h2>
La API utiliza JWT Token para proteger las rutas y asegurar la seguridad de la información. Para acceder a los endpoints protegidos, es necesario enviar un token válido en el encabezado de la solicitud.

<h2>Contribuir</h2>
Si desea contribuir al proyecto, puede hacer un fork del repositorio, realizar los cambios y enviar un pull request. Se agradecen todas las contribuciones.

![home](https://github.com/Revolutionnnn/django-flask/blob/main/imagenes/Home.png)
![Formulario](https://github.com/Revolutionnnn/django-flask/blob/main/imagenes/Formulario.png)
![Informacion de estudiantes](https://github.com/Revolutionnnn/django-flask/blob/main/imagenes/Personas.png)
![Actualizar usuario](https://github.com/Revolutionnnn/django-flask/blob/main/imagenes/Actualizar.png)


  
PD: Las secret key y los datos de autenticacion fueron eliminados para que cualquier persona pueda crear los suyos propios
