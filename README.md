# Bienvenido a nuestro GitHub

## Grupo

* Jesús García-Peñuela Molina-Prados (Frontend)

* Ángela Gijón Flores (Testing)

* Jesús Sánchez Cambronero Campos (Backend)

## Extra

Con respecto al Sprint 3, hemos tenido que rediseñar el enfoque de nuestra empresa por problemas con las APIS. Al hacer web scraping y obtener la información de las páginas de Renfe e Interbus, nos hemos dado cuenta de que cualquier cambio que hicieran en la página web respectiva, hacía que nuestra Base de Datos se quedará inutilizable. 
Por ello, hemos buscado una alternativa sobre nuestra aplicación web de viajes, cambiado las APIs e implementado otra alternativa efectiva, que es mostrar posibles viajes mediante la información de Ryanair. 
Este cambio nos ha afectado tanto en diseño como en código. Por lo que nuestra aplicación sigue la misma temática, pero con variación en cuanto al tipo de información mostrada. 
Las nuevas APIs seleccionadas, dejando a un lado web scraping, han sido Ryanair y la otra por problemas de códigos de acceso y de contradicción con la temática de nuestra idea, queda pendiente de implementar para el Sprint 4.
A parte de esto, al usar la API de Ryanair deja un máximo de peticiones por cuenta, por lo que el token solo se puede usar 20 veces en un mismo día. Queda pendiente de buscar una solución para el siguiente Sprint. 


## Documento de usuario

Nuestra empresa está implementada de tal forma que el usuario sea capaz de visualizarla como una aplicación web. 
En cuanto al diseño del código, hemos implementado una carpeta denominada “templates” que contiene el código HTML que carga la página web para ser visualizada. Ese mismo código contiene su respectivo diseño para tener una apariencia más cómoda y visual para el usuario. 
El código para utilizar la API de Ryanair y su respectiva base de datos no es perceptible ni usable por parte del usuario. 
Por otro lado, el código denominado “index.py” si que es necesario para que el usuario tenga acceso a la hora de carga la página web, ya que es su función. 
Por lo que, para poder usar la aplicación, se tienen que seguir los siguientes pasos: 
1.	Descargarse el código “index.py” que da acceso a la página web
2.	A la hora de la organización de los códigos, la forma de utilizarlo es tener todos los archivos dentro de una misma carpeta: index.py y la carpeta templates con el código del HTML denominado home.html
3.	Una vez hecho esto, desde la propia terminal de Windows se puede ejecutar. Para conseguirlo, se tiene que situar en la zona del ordenador donde tenga la carpeta anterior. Y abrir la carpeta para tener la ruta de los archivos. 
4.	Cuando se esté en este punto, hay que ejecutar el código HTML mediante el archivo index.py, poniendo la siguiente sentencia de código: python index.py
[En el caso de que no se pueda ejecutar podría ser por no tener Flask implementado, en ese caso como paso previo tendría que introducirse en la terminal: pip install Flask]
5.	Una vez que la ejecución esté lista, se abre el navegador del respectivo ordenador personal y se pone la siguiente dirección de acceso: https://localhost:5000 o bien https://127.0.0.1:5000 (el puerto 5000 al haber utilizado “Flask”).
6.	En este punto la página web tiene que visualizarse. 
7.	Cuando el usuario ya esté dentro de la aplicación web, tendrá diferentes casillas para rellenar: destino, origen y fecha; y un botón para Buscar que te da los diferentes vuelos con la siguiente información: origen, destino, número de vuelo, tarifa regular, moneda, asientos disponibles, fecha de salida y de llegada y la duración del vuelo. 
8.	Una vez que pinches dentro de la respectiva casilla de destino y origen, habrá un desplegable con los diferentes lugares de los que se puede viajar, como se muestra en las siguientes capturas: 
 
9.	Cuando ya se haya seleccionado el origen y el destino, habrá que seleccionar la fecha del vuelo, en donde se despliega un calendario para que sea más rápido seleccionarla y cómodo para el usuario, como aparece en la siguiente captura: 
 
10.	En este punto ya está toda la información seleccionada, el siguiente paso es darle al botón de Buscar que aparece en la esquina inferior derecha, con la siguiente apariencia: 
 
11.	Cuando la búsqueda se ha realizado, ya sale la información mencionada en el punto 7 sobre el vuelo. En el siguiente ejemplo visual que hemos probado se opta por Origen: Málaga, Destino: Barcelona y fecha: 18/04/2023. Y esto sería lo perceptible por el usuario si todos los pasos anteriores han sido efectivos: 
 
## Test de Integración

Estos son las pruebas de integración que hemos implementado mediante código y funcionan correctamente: 
1. El html se carga correctamente
2. La conexión con la API de Ryanair se realiza
3. Al introducir valores de entrada y realizar la búsqueda, la información se muestra correctamente

