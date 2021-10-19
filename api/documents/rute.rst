========================
    Recurso Rutas de viaje
========================

Recurso POST
-------------

    .. http:post:: /api/ruta/

    Crea una ruta de viaje con los destinos que prefiera el usuario

    * **Campos obligatorios**

        :rute_name: **(string)** Nombre de la ruta turistica
        :viaje: **(int)**id de viaje
        :ruta_destinos: **(int)** id del destino **se puede pasar multiples veces**


    * **Ejemplo de petición**

        .. host:: http

            POST /api/users/login/
            Content-Type: json

            {
                "rute_name": "nombrePrueba",
                "viaje": id,
                "ruta_destinos: 1,
                "ruta_destinos": 3
            }

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

                {
                "id": 6,
                "rute_name": "prueba thunder client",
                "viaje": 11,
                "ruta_destinos": [
                    3
                ]
                }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

                {
                "viaje": [
                    "Invalid pk \"18\" - object does not exist."
                ],
                "ruta_destinos": [
                    "Invalid pk \"9\" - object does not exist."
                ]
                }

Recurso GET
--------------

    
    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

                {
                    "id": 6,
                    "rute_name": "prueba thunder client",
                    "viaje": 11,
                    "ruta_destinos": [
                    {
                        "id": 3,
                        "nombre": "cascada de mistrato",
                        "vacations_type": "Aventura",
                        "region": "Andina",
                        "price": 123456
                    }
                    ]
                }

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