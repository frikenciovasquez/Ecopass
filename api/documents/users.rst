#token de acceso = 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

========================
    Recurso Usuarios
========================

Recurso LOGIN
-------------

    .. http:post:: /api/users/login/

    Inicia sesión con credenciales de usuario

    * **Campos obligatorios**

        :username: **(string)** Nombre de usuario
        :password: **(string)** Contraseña del usuario

    * **Ejemplo de petición**

        .. host:: http

            POST /api/users/login/
            Content-Type: json

            {
                "username": "usuariosprueba",
                "password": "usuariosprueba"
            }

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "user": {
                    "username": "Usuario",
                    "first_name": "Nombre_de_usuario",
                    "last_name": "apellido_de_usuario",
                    "cedula": "123456789",
                    "phone": "123456789",
                    "email": "ejemplo@admin.com",
                    "Empresa": false
                },
                "access_token": "3432b4501b1c8ecfd12d03989e7817095f2c92ab"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "non_field_errors": [
                    "Credenciales incorrectas"
                ]
            }

Recurso SIGNUP
--------------

    .. http:post:: /api/users/signup/

    Realiza el registro de un usuario

    * **Campos obligatorios**

        :username: **(string)** Nombre de usuario
        :password: **(string)** Contraseña del usuario
        :password_confirmation: **(string)** Verificación de la contraseña del usuario
        :email: **(email)** Correo del usuario en formato usuario@organizacion.tipo

    * **Ejemplo de petición**

        .. host:: http

            POST /api/users/signup/
            Content-Type: json

            {
    
                 "username":"usuario",
                 "password":"contraseña",
                 "password_confirmation" : "contraseña",
                 "email": "email@usuario.com"
    
            }

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "user": {
                    "username": "usuario",
                    "first_name": "Nombre",
                    "last_name": "apellido_de_usuario",
                    "cedula": "cedula",
                    "phone": "telefono",
                    "email": "usuario@admin.com",
                    "Empresa": false
                },
                "access_token": "9be6430833052c3e3f2608520e2bf6122e564675"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "username": [
                    "Este campo debe ser único."
                ],
                "email": [
                    "Este campo debe ser único."
                ]
            }  



Recurso LOGOUT
--------------

    .. http:get:: /api/users/logout/

    Cierra la sesión activa

    * **Campos obligatorios**

        :Authorization: **(token)** Token del usuario

    * **Ejemplo de petición**

        .. host:: http

            GET /api/users/logout/
            Content-Type: None
            Authorization: Token 4bb5315c61eae164656d2765b46a5447073d09b5

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "Éxito": "Sesión cerrada correctamente"
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Las credenciales de autenticación no se proveyeron"
            }


:status 200: Petición completada
:status 201: Usuario o token creado
:status 301: Redirigido debido a una solicitud de watch con una URL mal escrita
:status 400: Valores inválidos
:status 401: Token de autorización inválido