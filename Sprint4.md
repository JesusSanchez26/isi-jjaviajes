
## Documentación final

Con respecto al Sprint 3, hemos tenido que rediseñar el enfoque de nuestra empresa por problemas con las APIS. Al hacer web scraping y obtener la información de las páginas de Renfe e Interbus, nos hemos dado cuenta de que cualquier cambio que hicieran en la página web respectiva, hacía que nuestra Base de Datos se quedará inutilizable. 
Por ello, hemos buscado una alternativa sobre nuestra aplicación web de viajes, cambiado las API’s e implementado otra alternativa efectiva, que es mostrar posibles viajes mediante la información de vuelos del api de Ryanair y del api de Skyscanner. 
Este cambio nos ha afectado tanto en diseño como en código. Por lo que nuestra aplicación sigue la misma temática, pero con variación en cuanto al tipo de información mostrada. 
Las nuevas API’s seleccionadas, dejando a un lado web scraping, han sido Ryanair y la otra Skyscanner, como hemos comentado anteriormente. La segunda no estaba implementada para el sprint 3, pero ahora para el sprint final se encuentra todo implementado correctamente.
A parte de esto, al usar las 2 API’s desde una misma página, esta deja un máximo de peticiones por cuenta al día, por lo que el token solo se puede usar 20 veces en un mismo día. Por lo que no habría mucho inconveniente, pero si hubiese problemas solo habría que cambiar el token del programa por otro de otra cuenta.


### Documentación de usuario

Nuestra empresa está implementada de tal forma que el usuario sea capaz de visualizarla como una aplicación web. 
En cuanto al diseño del código, hemos implementado una carpeta denominada “templates” que contiene el código HTML que carga la página web para ser visualizada. Ese mismo código contiene su respectivo diseño para tener una apariencia más cómoda y visual para el usuario. 
El código para utilizar las APIs de Ryanair y SkyScanner y su respectiva base de datos no es perceptible ni usable por parte del usuario. 
Por otro lado, el código denominado “index.py” si que es necesario para que el usuario tenga acceso a la hora de carga la página web, ya que es su función. 
Por lo que, para poder usar la aplicación, se tienen que seguir los siguientes pasos: 
1.	Descargarse el código “index.py” que da acceso a la página web
2.	A la hora de la organización de los códigos, la forma de utilizarlo es tener todos los archivos dentro de una misma carpeta: index.py y la carpeta templates con el código del HTML denominado home.html
3.	Una vez hecho esto, desde la propia terminal de Windows se puede ejecutar. Para conseguirlo, se tiene que situar en la zona del ordenador donde tenga la carpeta anterior. Y abrir la carpeta para tener la ruta de los archivos. 
4.	Cuando se esté en este punto, hay que ejecutar el código HTML mediante el archivo index.py, poniendo la siguiente sentencia de código: python index.py
[En el caso de que no se pueda ejecutar podría ser por no tener Flask implementado, en ese caso como paso previo tendría que introducirse en la terminal: pip install Flask]
5.	Una vez que la ejecución esté lista, se abre el navegador del respectivo ordenador personal y se pone la siguiente dirección de acceso: https://localhost:5000 o bien https://127.0.0.1:5000 (el puerto 5000 al haber utilizado “Flask”).
6.	En este punto la página web tiene que visualizarse. 
7.	Primero aparecerá una página para que el usuario haga el login correctamente y así acceder a la página principal de nuestra aplicación web para poder buscar el viaje. 
![image](https://user-images.githubusercontent.com/91602556/234912650-91c31a63-7272-46f0-bbe3-0b5ff44feef8.png)
8.	Cuando el usuario ya esté dentro de la aplicación web, tendrá diferentes casillas para rellenar: destino, origen y fecha; y un botón para Buscar que te da los diferentes vuelos con la siguiente información: origen, destino, número de vuelo, tarifa regular, moneda, asientos disponibles, fecha de salida y de llegada y la duración del vuelo. 
9.	Una vez que pinches dentro de la respectiva casilla de destino y origen, habrá un desplegable con los diferentes lugares de los que se puede viajar, como se muestra en las siguientes capturas: 
 ![image](https://user-images.githubusercontent.com/91559952/231840861-92bde736-d637-4eec-bd82-8313026800e5.png)

9.	Cuando ya se haya seleccionado el origen y el destino, habrá que seleccionar la fecha del vuelo, en donde se despliega un calendario para que sea más rápido seleccionarla y cómodo para el usuario, como aparece en la siguiente captura: 
 ![image](https://user-images.githubusercontent.com/91559952/231840915-15920a81-6e20-4547-9f98-00b503c4a866.png)

10.	En este punto ya está toda la información seleccionada, el siguiente paso es darle al botón de Buscar que aparece en la esquina inferior derecha, con la siguiente apariencia: 
 ![image](https://user-images.githubusercontent.com/91559952/231840952-08e19602-9201-413b-819c-3fb321e34739.png)

11.	Cuando la búsqueda se ha realizado, ya sale la información mencionada en el punto 7 sobre el vuelo. En el siguiente ejemplo visual que hemos probado se opta por Origen: Málaga, Destino: Barcelona y fecha: 18/04/2023. Y esto sería lo perceptible por el usuario si todos los pasos anteriores han sido efectivos: 
![lab isis](https://user-images.githubusercontent.com/91559952/234650490-03d7c163-61c2-4b1c-8977-2342056dba78.jpg)
*Los resultados expresados en minutos son de una API y los que están en horas de la otra. 

### Guía DOCKER
Para el despliegue del servicio usando Docker será necesario seguir los siguientes pasos:
1.	 Descargar el contenido del repositorio de GitHub. Principalmente, los archivos ‘Dockerfile’, ‘index.py’, ‘requirements.txt’ y la carpeta templates con el archivo ‘home.html’. Todo ello se puede encontrar en el Github: https://github.com/JesusSanchez26/isi-jjaviajes 
2.	Descargar Docker. Para descargar Docker seguir los pasos indicados en Campus Virtual. 

    • sudo apt-get install apt-transport-https ca-certificates curl software-propertiescommon 

    • curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    • sudo add-apt-repository "deb [arch=amd64] 
    https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 

    • sudo apt-get update 

    • sudo apt-get install docker-ce

3.	Ejecutar los siguientes comandos. Una vez instalado Docker, dentro del directorio donde tengamos almacenados los archivos descargados, ejecutar los siguientes comandos. 

    • sudo docker build -f Dockerfile -t sprint4:latest . 
    
    • sudo docker run -p 2001:5000 -i sprint4
    
#### Otros comandos interesantes

Para comprobar que tenemos instalado Docker ejecutar el comando:

• sudo docker info

Para comprobar que se ha generado el contenedor ejecutar el comando:

• sudo docker image ls

Para descargar el contenedor generado ejecutar el comando:

• sudo docker save sprint4 > contenedor.tar
