Entrega Final Individual por el Estudiante: Julian Salas
Este es el proyecto final para el curso de Python de Coderhouse, en el cual he implementado una web de gestión de universidades, docentes, alumnos y envíos, junto con un sistema de autenticación de usuarios. A continuación, te explico las principales características y funcionalidades del proyecto.

Características Implementadas
Sistema de Autenticación y Seguridad:

Se requiere que los usuarios estén registrados e iniciados sesión para acceder a la mayoría de las secciones de la web. La única excepción son las páginas de inicio, registro e inicio de sesión.
He implementado una barra de navegación dinámica, que cambia según si el usuario está autenticado o no. Para los usuarios no registrados, aparecerán las opciones "Iniciar sesión" y "Crear cuenta", y una vez iniciada la sesión, se cambiará a "Editar perfil" y "Cerrar sesión".
En caso de no estar registrado, el sistema redirige al usuario a la página de inicio de sesión o registro.
Aplicaciones Separadas:

El proyecto se divide en dos aplicaciones principales:
AppCoder: Maneja todo el código relacionado con las secciones de "Buscar Universidades", "Docentes", "Alumnos", "Universidades" y "Envios".
User: Gestiona todo lo relacionado con el usuario, incluyendo inicio de sesión, registro, edición de perfil, y gestión de avatar.
Funcionalidades de la Web:

Registrar y autenticación de usuarios: Los usuarios pueden registrarse y acceder a la página utilizando su nombre de usuario y contraseña.
Gestión de avatar: Los usuarios pueden agregar y editar su avatar en la sección de "Editar perfil".
Barra de navegación dinámica: Dependiendo de si el usuario está autenticado, la barra de navegación muestra opciones diferentes.
CRUD para Universidades, Docentes, Alumnos y Envios: Cada una de estas secciones permite crear, editar, eliminar y visualizar registros. Los formularios correspondientes para estas operaciones están accesibles desde la barra de navegación.
Seguridad en la navegación: Se protege el acceso a las secciones principales de la web para usuarios no autenticados, como la creación de universidades, docentes, alumnos y envíos.
Cómo Funciona la Web
Iniciar el Servidor:

Para correr el servidor localmente, utiliza el comando:
python manage.py runserver
Luego, accede a http://localhost:8000 desde tu navegador. La página de inicio aparecerá.
Navegación en la Web:

Si no estás registrado, haz clic en el botón desplegable que dice "Cuenta" y selecciona "Registrar cuenta". Después de completar el registro, podrás iniciar sesión.
Si ya has iniciado sesión, la barra de navegación cambiará a mostrar tu nombre de usuario, con opciones para "Editar perfil" y "Cerrar sesión".
Al editar tu perfil, puedes agregar un avatar (preferiblemente un archivo .gif).
Secciones del Proyecto:

Buscar Universidad: Permite buscar universidades por nombre. Se muestra una lista de universidades y sus países. URL: http://localhost:8000/buscar_universidades/
Docentes: Muestra los docentes registrados con su nombre, apellido, correo electrónico y profesión. Permite crear, editar, eliminar y detallar docentes. URL: http://localhost:8000/lista_docente/
Alumnos: Muestra a los alumnos registrados con su nombre, apellido, correo electrónico e ID de estudiante. Permite realizar las mismas acciones CRUD. URL: http://localhost:8000/lista_alumno/
Universidades: Muestra las universidades creadas con su nombre y país, permitiendo también realizar las acciones CRUD. URL: http://localhost:8000/lista_universidad/
Envios: Muestra los envíos registrados con su nombre, descripción, fecha de entrega y estado de entrega, permitiendo agregar, editar, eliminar y detallar envíos. URL: http://localhost:8000/lista_envio/
Cerrar Sesión y Editar Perfil:

Al hacer clic en tu nombre de usuario en la barra de navegación, se mostrarán las opciones de "Editar perfil" y "Cerrar sesión". En "Editar perfil", podrás actualizar tus datos y añadir o cambiar tu avatar.
Si seleccionas "Cerrar sesión", serás desconectado y redirigido a la página de inicio, donde necesitarás iniciar sesión nuevamente para continuar navegando.
Eliminar Avatar:

Si deseas eliminar tu avatar, esta opción se encuentra dentro de la sección "Editar perfil" en la parte inferior. Solo podrás eliminar el avatar si tienes uno previamente asignado.
Notas Importantes:
Es esencial estar registrado e iniciar sesión para poder navegar por las secciones protegidas de la web.
Los avatares deben ser archivos .gif para garantizar que se carguen correctamente.
La página de inicio, junto con las páginas de registro e inicio de sesión, están accesibles para todos los usuarios, sin necesidad de autenticación previa.
Este proyecto ha sido diseñado para ofrecer una estructura clara y segura para la gestión de universidades, docentes, alumnos y envíos, mientras que garantiza que solo los usuarios autenticados puedan acceder a las funcionalidades protegidas.