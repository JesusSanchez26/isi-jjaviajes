# Bienvenido a nuestro GitHub

## Grupo

* Jesús García-Peñuela Molina-Prados (Frontend)

* Ángela Gijón Flores (Testing)

* Jesús Sánchez Cambronero Campos (Backend)

## Documentación final

Con respecto a la documentación final, hemos ampliado la documentación de usuario realizada en el Sprint 3 junto a la documentación necesaria para cargar la imágen del Docker que sirve para el control.

### Documentación de usuario

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
 ![image](https://user-images.githubusercontent.com/91559952/231840861-92bde736-d637-4eec-bd82-8313026800e5.png)

9.	Cuando ya se haya seleccionado el origen y el destino, habrá que seleccionar la fecha del vuelo, en donde se despliega un calendario para que sea más rápido seleccionarla y cómodo para el usuario, como aparece en la siguiente captura: 
 ![image](https://user-images.githubusercontent.com/91559952/231840915-15920a81-6e20-4547-9f98-00b503c4a866.png)

10.	En este punto ya está toda la información seleccionada, el siguiente paso es darle al botón de Buscar que aparece en la esquina inferior derecha, con la siguiente apariencia: 
 ![image](https://user-images.githubusercontent.com/91559952/231840952-08e19602-9201-413b-819c-3fb321e34739.png)

11.	Cuando la búsqueda se ha realizado, ya sale la información mencionada en el punto 7 sobre el vuelo. En el siguiente ejemplo visual que hemos probado se opta por Origen: Málaga, Destino: Barcelona y fecha: 18/04/2023. Y esto sería lo perceptible por el usuario si todos los pasos anteriores han sido efectivos: 
![image](https://user-images.githubusercontent.com/91559952/231840994-210c0c3c-0a77-4158-ab8b-e1201d896a00.png)

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
