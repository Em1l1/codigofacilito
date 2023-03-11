# Respuestas por parte del servidor

Hasta este punto del curso ya tenemos en claro que es el protocolo HTTP y las arquitecturas clientes servidor y REST, ahora, ya para ir finalizando la parte introductoria, me gustaría explicarte los diferentes tipos de respuestas que pueden existir para una petición. 😄

Como mencionamos anteriormente, un servidor se encuentra obligado a responder a cada una de las peticiones realizadas por un cliente

Las respuetas puede ser desde texto plano, un maquetado HTML, un objeto JSON, hasta archivos un poco más complejos, tales como imágenes, vídeos, audios, pdf s, etc ...

Sin embargo, también es importante mencionar que al utilizar, ya sea, el protocolo HTTP o HTTPS existen diferentes *estatus* para notificar el estado de una petición. Estos estatus se representan mediante un valor numérico, y a cada uno de estos valores se les conocen como *status code*, o código de estatus por su traducción al español.

Estos códigos abarcan un rango de números enteros, que comprenden del 100 al 599.

Y podemos agruparlos en 5 categorías.

- Respuestas informativas (100–199),
- Respuestas satisfactorias (200–299),
- Redirecciones (300–399),
- Errores de los clientes (400–499),
- Errores de los servidores (500–599).

Veamos un par de ejemplos.

Comencemos con el grupo: *Respuestas informativas*. Este grupo abarcan del rango 100 al 199. Y cualquier valor que se rse encuentre en este rango hará referencia a un status informativo.

Por ejemplo, si el cliente recibe como status Code 100, esto le indica que hasta ahora todo va bien, y debe continuar con la solicitud al servidor.

Otro ejemplo pudiera ser el código 102, que le indica al cliente que el servidor ha recibido la petición y aún se encuentra procesándola..

Estos son algunos código informativos, por su puesto no lo son todos. Pero sí, me atrevo a decir, los más relevantes.

------

El segundo grupo, *Respuestas satisfactorias*, como su nombre nos indican, serán códigos que le indiquen al cliente que la petición se realizo de forma exitosa, y que no ha ocurrido ningún tipo de error.

Este grupo abarca del rango, 200 al 299.

Algunos ejemplos son:

El código 200, que le indica al cliente que la petición y respuesta han sido un éxito.

El código 201, inducida que la reacción de un nuevo recurso fue exitosa.

Por mencionar algunos códigos.

------

Por su parte, el tercer grupo: *Redirecciones* abarca del rango 300 al 399, y cualquier número que se encuentre dentro de este rango indica que hubo algún tipo de redireccionamiento al momento de completar la petición.

Por ejemplo. El código 301 le indica al cliente que el recurso que ha solicitado ha sido cambiado, ya no se encuentra en la ruta indicada, y por lo tanto no fue posible encontrarlo.

El código 302 indica que el recurso solicitado ha sido cambiado de forma temporal, por el momento no se encuentra disponible pero lo hará en un futuro.

De igual forma este son algunos código para comprender este grupo.

------

Ahora hablemos del cuatro grupo, el grupo de *Errores de cliente*. Este grupo fue diseñado para poder hacerle saber al cliente que la petición no puede ser completada por que existe un error por parte de él.

Este grupo abarca del rango 400 al 499.

Algunos ejemplos son los siguientes:

Error 400 Bad request, Esta respuesta significa que el servidor no pudo interpretar la petición por una sintaxis invalida.

Error 401 Unathorize. Es necesario autenticarse para que el servidor pueda dar una respuesta satisfactoria al cliente.

Error 403 Forbide. El cliente no posee los permisos necesarios para completar la operación

Etc...

------

Y finalmente el grupo 5: *Errores del servidor*. Grupo de códigos que comprenden del número 500 al 599. Este grupo como su nombre lo indica le permiten conocer al cliente que ha habido un error por parte del servidor, y la operación, la petición no puede ser completada.

Algunos ejemplos son lo siguientes:

Error 500: Internal server error: El servidor ha tenido un error y bno sabe como manejarlo.

Error 503: Service Unavailabl: Ser vidro no esta listo para responder a una peticón. Una causa muy comun de este error pude deberse a que el servidor este caido por mantenimiento o está sobre cargado.

------

Listo, estos son los 5 grupos de códigos de estatus que debemos conocer.

Es importante, si bien no conocer todos los códigos al pie de la letra, por lo menos si tener en mente los 5 grupos, ya que a partir de ellos sabremos exactamente que responder por cada petición de un cliente, y de esta forma estaremos creando servicios web que sigan con el standares y protocolos previamente definidos.