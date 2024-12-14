Entrega Final individual Por el estudiante

Julian Salas

Como podran ver, la tercera pre entrega se utilizo como base de la entrega final , las diferencias que que les hice unas modificaciones y es que al momento de agregar el crud lo hice con clases basdas en vistas para que sea mas organizado , se agrego el modelo avatar y para el momento de agregar el avatar lo puse en editar_avatr para que sea mas dinamico y poder agregar el avatar ahi mismo

Otra diferencia es que hice que en la barra de navegacion de mi proyecto solo deje los modelos necesarios y al momento de hacer click en cada modelo poder visualizar el Crud de clases basadas en vistas , el avatar 
y el boton desplegable con todas sus opciones que son : iniciar sesion y crear cuenta en caso de no haberse registrado y iniciado sesion y en caso de haber iniciado sesion el boton desplegable cambiara a editar perfil y cerrar sesion . Nota : Cabe recalcar que si no estar registrado no podras acceder a ninguna seccion de la app , te mandara a iniciar sesion y en caso de no tener un usuario tendras que registrarte

Tambien les agregue seguridad para que como ya mencione cualquiera no pueda navegar por la pagina ("solo no tendra seguridad las secciones inicio("en este caso aparece como CodificAr Dev Demo que seria el boton para ir al inicio") ,registrarse y iniciar sesion"), sino que se tenga que registrar y iniciar sesion para poder navegar por la web , en caso de no tener un usuario tendras que pulsar el boton desplegable que dice cuenta y pulsar registrarse , y despues de registrarse ya tendras un usuario para poder iniciar sesion,

Como podran ver en este proyecto existen 2 Aplicaciones o app , las cuales son AppCoder que es donde puse el codigo general de las secciones 
Buscar Universidades.
Docentes.
Alumnos.
Universidades.
Envios.
Y la otra app es User , que es donde manejo todo lo relacionado con el User como iniciar secion , cerrar sesion , editar perfil y registrarsey lo del avatar que lo agregue en el apartado de editar perfil en la parte inferior, etc.


Como funciona la Web? : 
Primero que nada tendras que correr el comando "python manage.py runserver" para correr el servidor con solo ir a tu navegador y poner ("http://localhost:8000//") te mandara a la seccion de inicio , como ya mencione no podras navegar por la web sin iniciar sesion , asi que dirigete al apartado del boton desplegable cuenta y se te abrira una seccion que contendra iniciar sesion y registrarte , si aun no tienes un usuario tendras 
que registrarte primero y ya despues tendras que iniciar sesion , y ya podras navegar por la pagina normalmente.Como ya iniciaste sesion ya podras agregar un avatar , para eso dirigete al boton desplegable que antes de iniciar sesion se llamaba cuenta ahora tendra el nombre de tu usuario y si le das click las secciones abran cambiado con editar perfil y cerrar sesion , dirigete a editar perfil rellena el formulario y agrega tu avatar , si no estoy mal tiene que ser .gif eso si no lo se, pero por preferencia y por que asi fue como lo vi en la clase que sea .gif.

Buscar universidad:
por parte de la seccion de buscar universidad que se encuentra en la parte superor , como su nombre se dice es para buscar universidad ademas abajo te mostrara las universidades y sus paises si deseas buscar busca por el nombre de la universidad , no importa si lo escribes en minusculas o mayusculas te mostrara la universidad quee mas se asemeje a el nombre de la universidad que diste en el buscador 
http://localhost:8000/buscar_universidades/ por si acaso esta es la url

Docentes:
Por parte de la seccion de Docentes que tambien lo veras en el navegador en la parte superior: Esta seccion te mostrara los docentes que has creado con cada uno de sus apartados :
Nombre,	Apellido,	Correo Electronico y Profesion, y tambien te permitira crear(te enviara al formulario de agregar Docentes) , editar(te enviara al formulario de editar Docentes) , eliminar(te enviara al formulario de eliminar Docentes) y detallar(te enviara al formulario de detallar Docentes) los docentes, si le das click en alguno de los botones ya anteriormente mencionados crear , editar , eliminar y detallar ,te mostrara el formulario que te permitira realizar alguna de esas acciones mencionadas
http://localhost:8000/lista_docente/

Alumnos:
Por parte de la seccion de Alumnos que tambien lo veras en el navegador en la parte superior: Esta seccion te mostrara los alumnos que has creado con cada uno de sus apartados :
Nombre,	Apellido,	Correo Electronico y ID-Estudiante, y tambien te permitira crear(te enviara al formulario de agregar Alumnos) , editar(te enviara al formulario de editar Alumnos) , eliminar(te enviara al formulario de eliminar Alumnos) y detallar(te enviara al formulario de detallar Alumnos) los alumnos, si le das click en alguno de los botones ya anteriormente mencionados crear , editar , eliminar y detallar ,te mostrara el formulario que te permitira realizar alguna de esas acciones mencionadas
http://localhost:8000/lista_alumno/
    
Universidades:
Por parte de la seccion de Universidades que tambien lo veras en el navegador en la parte superior: Esta seccion te mostrara las universidades que has creado con cada uno de sus apartados :
Nombre y pais, y tambien te permitira crear(te enviara al formulario de agregar Universidades) , editar(te enviara al formulario de editar Universidades) , eliminar(te enviara al formulario de eliminar Universidades) y detallar(te enviara al formulario de detallar Universidades) las universidades, si le das click en alguno de los botones ya anteriormente mencionados crear , editar , eliminar y detallar ,te mostrara el formulario que te permitira realizar alguna de esas acciones mencionadas
http://localhost:8000/lista_universidad/

Envios:
Por parte de la seccion de Envios que tambien lo veras en el navegador en la parte superior: Esta seccion te mostrara los Envios que has creado con cada uno de sus apartados :
Nombre ,Descripcion,Fecha De Entrega y Entrega, y tambien te permitira crear(te enviara al formulario de agregar envios) , editar(te enviara al formulario de editar envios) , eliminar(te enviara al formulario de eliminar envios) y detallar(te enviara al formulario de detallar envios) los Envios, si le das click en alguno de los botones ya anteriormente mencionados crear , editar , eliminar y detallar ,te mostrara el formulario que te permitira realizar alguna de esas acciones mencionadas
http://localhost:8000/lista_envio/

Cerrar sesion:
Por parte de cerrar sesion , si le das click al boton desplegable con el nombre de tu usuario (Nota: Tienes que haber iniciado sesion) te apareceran dos opciones editar perfil y cerrar sesion, dale click a cerrar sesion y te cerrara la sesion y te saldra un mensaje de que has cerrado sesion haciendo que no tengas permiso de navegar por las secciones anteriormente mencionadas.Y al darle click te pedira que inicies sesion.
http://localhost:8000/User/cerrar_sesion/

Editar perfil:
Por parte de Editar perfil , si le das click al boton desplegable con el nombre de tu usuario (Nota: Tienes que haber iniciado sesion) te apareceran dos opciones editar perfil y cerrar sesion, dale click a Editar perfil y te mandara a una pagina con un formulario que deberas rellenar.En este apartado tambien estara la opcion de agregar un avatar (seleccionar un archivo) al darle click te enviara a tus archivos , agrega tu avatar ahi , tiene que ser .gif y le das a guardar cambios. despues de eso te aparecera la imagen.gif que agregaste en la parte superior al lado del boton desplegable 
http://localhost:8000/User/editar_usuario/

Eliminar avatar:
Por parte de Eliminar avatar. Esta seccion te aparecera adentro de editar perfil en la parte inferior  ,cabe recalcar que para poder eliminar tu avatar tienes que tener un avatar.Al eliminar el avatar te enviara al inicio y ya no te aparecera la imagen que antes aparecia 