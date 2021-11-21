========================
    Recurso Viajes
========================

Recurso POST
-------------

    .. http:post:: /api/travel/

    Crea un viaje con la credencial activa (TOKEN) del usuario

    * **Campos obligatorios**


        :transporte: **(string)** metodo de transporte que va a utilizar el usuario
        :user: **(string)** id del usuario activo de la sesion
        :date_start: **(Date)** fecha de inicio del viaje
        :date_end: **(Date)** fecha de fin del viaje

    * **Opciones de transporte**
        :avion: **(Aereo)**
        :bus: **(Terrestre)**
        :barco: **(Maritimo)**
       
    * **Ejemplo de petición**

        .. host:: http

            POST /api/travel/
            Content-Type: json

            {
                "transporte": "opciones",
                "user": "id activo"
                "date_start: "2021-10-19"
                "date_end": "2021-10-19"
            }

    * **Ejemplos de respuesta** 

        .. host:: http/api/travel/

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
            "id": 19,
            "date_start": "2021-10-28",
            "date_end": "2021-10-29",
            "transporte": "bus",
            "user": 14,
            "ruta_de_viaje": []
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

                {
                "transporte": [
                    "\"avions\" is not a valid choice."
                ],
                "user": [
                    "Invalid pk \"123\" - object does not exist."
                ]
                }


                [
                "Falta fechas"
                ]

                [
                "fechas invalidas, fecha de reservacion 8 dias previos, fecha minima de duracion de viaje 1 dia"
                ]
                
Recurso GET
--------------


    * **Ejemplos de respuesta** 

        .. host:: http/api/travel/

            HTTP/1.1 201 CREATED
            Content-Type: json

                {
                "id": 10,
                "date_start": "2021-10-19",
                "date_end": "2021-10-19",
                "transporte": "bus",
                "user": 12,
                "ruta_de_viaje": [
                    {
                    "id": 5,
                    "rute_name": "la mera fiesta full farra",
                    "viaje": 10,
                    "ruta_destinos": [
                        {
                        "id": 3,
                        "nombre": "cascada de mistrato",
                        "vacations_type": "Aventura",
                        "region": "Andina",
                        "price": 123456
                        },
                        {
                        "id": 5,
                        "nombre": "prueba1",
                        "vacations_type": "medicinal",
                        "region": "Andina",
                        "price": 46464
                        }
                    ]
                    }
                ]
                }

            HTTP/1.1 401 Unauthorized
            Content-Type: json
               
                {
                "detail": "Authentication credentials were not provided."
                }

            HTTP/1.1 404 Not Found
            Content-Type: json                
                {
                "detail": "Not found."
                } 



:status 200: Petición completada
:status 201: Usuario o token creado
:status 301: Redirigido debido a una solicitud de watch con una URL mal escrita
:status 400: Valores inválidos
:status 401: Token de autorización inválido
:status 404: Objeto no encontrado