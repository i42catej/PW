# PW
# Grado en Ingeniero en Informática - Programación Web
### Enero 2016
#### Normas de Realización
En la cuenta del examen hay un fichero comprimido con el esqueleto para comenzar el examen. Descomprime el fichero examen.tgz usando **‘‘tar xpzf examen.tgz’’** y a continuación borra **examen.tgz.**

El navegador se puede usar para comprobar la corrección de los ejercicios a medida que se realizan. También se puede usar para acceder al manual de Django o a cualquier otra página donde se pueda obtener información siempre y cuando no se realicen consultas en ningún foro. Las cuentas de examen son monitorizadas de forma automática durante todo el tiempo de realización del examen.

Cada alumno podrá contar con 5 hojas de tamaño A4 en las que podrá incluir la información que quiera. Podrán estar escritas por ambas caras. **No se podrán compartir con otros alumnos durante el examen bajo ninguna circunstancia.**

### Ejercicios
El proyecto consiste en la web de gestión de un proceso electoral. Dentro de este proyecto se ha de completar la aplicación eleccion que gestionará el recuento de votos del proceso electoral. Para la gestión se han de tener en cuenta las siguientes entidades:

1. Mesa electoral. Indica el recuento de votos de una mesa concreta donde hay varios partidos que concurren a las elecciones. Cada mesa pertenece a una única circunscripción y tiene un nombre.
2. Circunscripción electoral. Consiste en un conjunto de mesas. Cada circunscripción tiene asociado un número de escaños que reparte entre los partidos que se presentan y tiene un nombre.
3. Partido político. Concurre a la elecciones, obtiene un número determinado de votos en cada mesa. Cada partido se denomina por un nombre que ha de ser único.
4. Resultado. Es el resultado de un determinado partido en una mesa electoral. Cada mesa electoral tiene un resultado para cada partido. No es necesario que todos los partidos tengan resultados en todas las mesas de una circunscripción electoral.

Los atributos que se indican arriba son los mínimos necesarios. Se podrán añadir los atributos que se deseen para la realización de los ejercicios.
A la web podrá acceder un usuario no registrado que podrá consultar toda la información disponible pero no podrá añadir nueva información ni modificar la ya existente. Deben existir usuarios registrados con dos niveles de privilegios. El usuario supervisor podrá añadir circunscripciones y mesas electorales y el usuario gestor podrá añadir la información de los resultados de una mesa electoral, pero no anñadir nuevas mesas o circunscripciones.
Para la corrección deberá incluir dos usuarios. El usuario supervisor se denominará **supervisor9** y el usuario gestor será **gestor9**. En ambos casos la clave será el mismo nombre del usuario.

El esqueleto facilitado contiene una propuesta de clases y relaciones para resolver el ejercicio. No se indican atributos que deberán ser añadidos al realizar el ejercicio. Las relaciones propuestas así como las clases podrán ser modificadas por el alumno si considera otras más eficientes, siempre que se respete el enunciado del problema.

A partir de esta descripción del problema a resolver implementa las siguientes funcionalidades:

1. (2) Usando la clase User de Django implementa la autenticación de un usuario. No es necesario implementar las funciones de gestión de usuarios, para ello se puede usar el interfaz de administrador de Django. Se han de distinguir los dos tipos de usuarios descritos anteriormente. Para ello se pueden usar directamente los atributos de la clase User de Django.
2. (3) Implementa las vistas, formularios y plantillas necesarios para poder ver una lista de circunscripciones electorales, añadir una circunscripción, editar una circunscripción y borrar una circunscripción ya existente. Las operaciones de añadir, editar y borrar solo las podrá llevar a cabo un usuario supervisor. La visualización de la lista podrá verla cualquier usuario incluso si no se ha auntenticado. Este ejercicio se habrá de realizar usando vistas basadas en clases.
3. (3) Implementa las vistas, formularios y plantillas necesarios para poder ver una lista de las mesas de una cierta circunscripción electoral y ver los detalles de una mesa concreta. Implemente las vistas para añadir una mesa a una circunscripción y editar una mesa ya existente. Las operaciones de añadir y editar solo las podrá llevar a cabo un usuario supervisor. La visualización de la lista y los detalles los podrá ver cualquier usuario incluso si no se ha auntenticado. Este ejercicio se habrá de realizar usando vistas como funciones.
4. (2) Implementa las vistas, formularios y plantillas necesarias para que un usuario gestor pueda introducir los resultados de una mesa electoral. Implementa las vistas necesarias para conocer la asignación de los escaños a una circunscripción por un sistema mayoritario donde el partido más votado recibe todos los escaños menos uno y el segundo partido más votado recibe un escaño. Este ejercicio se podrá implementar con vistas como funciones o basadas en clases a elección del alumno y con la misma puntuación en ambos casos.

NOTAS IMPORTANTES:

• Implemente los ejercicios siguiendo las instrucciones específicas de forma exacta. No implementes ninguna opción no solicitada en el enunciado, ni modifique las opciones pedidas. Lo que no se indique de forma específica se podrá implementar de cualquier forma razonable.

• Cada apartado del ejercicio debe funcionar para poder ser considerado puntuable.

• Entre paréntesis se indica la nota de cada ejercicio.


Tiempo de realización: 5 horas.


