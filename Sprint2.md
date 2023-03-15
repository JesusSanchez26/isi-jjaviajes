# SPRINT 2

## Tecnologías a usar

> -	Lenguajes de programación: la aplicación utiliza el lenguaje de programación Python y para obtener información usa lenguaje web, en concreto HTML, para el desarrollo   de la interfaz y la lógica de la aplicación.

> -	Frameworks y librerías: la aplicación utiliza algún framework o librería de desarrollo web, como Pandas, para agilizar el proceso de desarrollo y mejorar la calidad   del código. También se usa Selenium, que es un entorno de pruebas de software y se utiliza para el web scraping.

> -	APIs: la aplicación utiliza las APIs públicas proporcionadas BlaBlaCar para obtener la información de los viajes y mostrarlos en la aplicación. Y además para obtener   información utilizamos web scraping de las páginas de Renfe y Interbús.

> -	Bases de datos: la aplicación usaría una base de datos, ya sea MySQL, ORACLE u otra, para almacenar la información de los usuarios y viajes correctamente, y permitir   búsquedas.

> -	Herramientas de control de versiones: Para gestionar el código fuente de la aplicación y colaborar en su desarrollo, se utiliza una herramienta de control de           versiones, la cual es GitHub.


## Contrato Mercantil

> -	**Objeto del contrato:** en este apartado se incluye el servicio que se va a prestar. En nuestro caso es una plataforma web que va a prestar servicio a un grupo de usuarios que buscan rutas de transporte desde un origen hasta un destino en una fecha determinada para que puedan elegir la ruta más óptima para ellos. La aplicación utilizará las páginas de Renfe, Blabacar e Interbus para listar estos viajes. 

> -	**Identificación de las partes:** dentro de nuestra empresa va a tres partes involucradas. Los usuarios que son los que usan nuestra plataforma web, las empresas de las cuales obtenemos la información para mostrarle a los usuarios y nuestra empresa que tiene la responsabilidad de dar el servicio de información de rutas a los clientes. 

> -	**Obligaciones de las partes:** en nuestra empresa hay dos partes involucradas, nuestra empresa que vamos a tener una responsabilidad de mantener la plataforma actualizada y funcional. Y la otra parte es con respecto a las empresas de transporte: Renfe, Blabacar e Interbus; que tendrían que proporcionarnos información actualizada y precisa de las rutas disponibles. 

> -	**Condiciones del servicio:** la empresa se compromete a dar acceso a la aplicación mencionada anteriormente. Por lo que se tiene que dar acceso a un cliente y que pueda obtener una lista de viajes disponibles. Como empresa no nos haremos cargo de la responsabilidad de retraso o cancelación de los viajes, ya que eso es responsabilidad de las páginas mencionadas. 

> -	**Responsabilidades y Garantías:** no se garantiza la exactitud, puntualidad, integridad, calidad, fiabilidad o disponibilidad de la aplicación y se reserva el derecho de suspender, modificar, restringir o cancelar el acceso a la aplicación en cualquier momento y sin previo aviso. 
La empresa tampoco se hará cargo de ningún daño indirecto, incidental, especial o consecuencial, incluyendo, sin limitación, pérdida de beneficios, ingresos, oportunidades, pérdida de datos o interrupción del negocio, resultante del uso o la imposibilidad de utilizar la aplicación.

> -	**Confidencialidad:** hay obligaciones para proteger información confidencial en nuestro proyecto; tales como la información de pago de nuestros clientes y también a las contraseñas de estos. Se aplicará seguridad con respecto a estos datos y a los propios de la empresa. Con esto se pretender proteger la información confidencial de los usuarios y la relacionado con el proyecto. Además, la empresa se compromete a la confidencialidad de la información con el presente contrato y a no divulgarla a terceros sin el consentimiento previo y por escrito de la otra parte. 

> -	**Precio y condiciones de pago:** como se mencionó en el Sprint 1 las formas de pago de nuestra aplicación son cuotas mensuales y anuales, con descuento a determinados tipos de clientes. Con respecto a las empresas de transporte que mostramos de nuestra plataforma no tienen que abonarnos nada. La prestación se abonará por adelantado y será no reembolsable. Hay diferentes métodos de pago y se considerará efectivo cuando se reciban en la cuenta bancaria designada por la empresa JJAViajes. 

> -	**Resolución de conflictos:** Cualquier conflicto que surja en relación con el presente contrato será resuelto mediante mediación o, en su defecto, mediante arbitraje de conformidad con las leyes vigentes en España. Si no se llega a un acuerdo por medio de la mediación o el arbitraje, se someterá la resolución de la controversia a los tribunales competentes en Ciudad Real.


## Interfaces y estructuras de datos 

Como interfaz vamos a tener una interfaz de usuario (UI) que será la parte visible al usuario de nuestra plataforma web. A través de ella, los usuarios pueden realizar búsquedas de rutas de transporte con un origen y destino. Tiene que ser una aplicación fácil de usar para proporcionar una experiencia agradable al usuario. Algunas de las características que incluiremos en nuestra interfaz serán:

> - Campo de origen: es un campo de entrada donde el usuario especificará el origen de su viaje. 
> - Campo de destino: es un campo de entrada donde el usuario especificará el destino de su viaje. 
> - Campo de fecha: es un campo de entrada en el que el usuario puede especificar la fecha en la que quiere viajar. 
> - Botón de búsqueda: es un botón en el que el usuario debe de hacer click para buscar las rutas de transporte en relación con los campos de entrada mencionados. 
> - Lista de resultados: es una lista de resultados donde se muestran las rutas de transporte disponibles que coinciden con los criterios seleccionados e introducidos de búsqueda del usuario. 

Con respecto a la estructura de datos de nuestra plataforma, tendremos una tabla de rutas que almacenará los datos de las rutas disponibles que se pueden mostrar a los usuarios. Dentro de la tabla, los campos que incluiremos será origen, destino, fecha, precio, aplicación de transporte, hora de salida y hora de llegada.

Además, tendremos que integrar los datos de Renfe, Blablacar e Interbus que son las aplicaciones de las cuales mostraremos rutas. Considerando la estructura de datos como un tabla de datos de rutas del proveedor, una para cada aplicación, donde se almacene la información de las rutas disponibles incluyendo los mismos campos que la estructura de datos anterior. 

Como ayuda, estamos planteándonos añadir una tabla de datos de proveedores en la que incluyamos el nombre del proveedor, el sitio web del proveedor y la API del proveedor. 

Adicionalmente, a lo largo del desarrollo de la empresa podríamos incluir integración de más proveedores a parte de los tres mencionados, funcionalidades de filtrado y ordenamiento de resultados para hacer más personalizada la experiencia de usuario e integración de sistemas de pago, para que el usuario pueda comprar los boletos a través de la plataforma, en vez de dirigir a la página del proveedor. Aunque en la etapa y desarrollo inicial de nuestro proyecto solo incluiremos lo mencionado al principio. Estas serán integraciones y funcionalidades que nos replantearemos de cara al futuro con el correcto desarrollo y despliegue de nuestra plataforma web. 
