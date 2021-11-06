========================
    Recurso Rutas de viaje
========================

Recurso POST
-------------

    .. http:post:: /api/ruta/

    Crea una ruta de viaje con los destinos que prefiera el usuario

    * **Campos obligatorios**

        :service: **(string)** Nombre del tipo de servicio
        :viaje: **(int)** id de viaje
        :servicios_disponibles: **(int)** id del servicio **se puede pasar multiples veces**


    * **Ejemplo de petición**

        .. host:: http

            POST /api/users/login/
            Content-Type: json

            {
                "service": "alquiler",
                "viaje": id,
                "servicios_disponibles: 1,
                "servicios_disponibles": 3
            }

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

                {
                "service": "restaurante",
                "viaje": 13,
                "servicios_disponibles": [
                    1,
                    2
                ]
                }
            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

                {
                "viaje": [
                    "Invalid pk \"18\" - object does not exist."
                ],
                 "service": [
                    "\"estaurante\" is not a valid choice."
                ]
                  "servicios_disponibles": [
                    "Invalid pk \"7\" - object does not exist."
                ]
}
                }

Recurso GET
--------------

    
    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "id": 1,
                "service": "alquiler",
                "viaje": 13,
                "servicios_disponibles": [
                {
                    "id": 1,
                    "region": "bogota",
                    "description": "restaurante Alfonso pumarejo",
                    "phone": "3213454324",
                    "price": 12455
                },
            HTTP/1.1 404 Not Found
            Content-Type: json

                {
                "detail": "Not found."
                }
               
                {
                "detail": "Authentication credentials were not provided."
                }



:status 200: Petición completada
:status 201: Usuario o token creado
:status 301: Redirigido debido a una solicitud de watch con una URL mal escrita
:status 400: Valores inválidos
:status 401: Token de autorización inválido


