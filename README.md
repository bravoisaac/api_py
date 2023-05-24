Aquí tienes la documentación de la API proporcionada con referencias sobre cómo utilizar cada función:

# API de Usuarios

Esta API permite realizar operaciones relacionadas con la gestión de usuarios.

## Endpoints

### 1. Agregar un nuevo usuario

**URL:** `/api/v1/users`

**Método:** `POST`

**Descripción:** Agrega un nuevo usuario a la base de datos.

**Parámetros de entrada:**
- `username` (cadena): Nombre de usuario del nuevo usuario.
- `password` (cadena): Contraseña del nuevo usuario.

**Parámetros de entrada ejemplo posman:**
  - Ejemplo de POST:
    ```
    {
        "username":"jase",
        "password":"111112"
    }
    ```

**Respuestas:**
- Código 200 OK: El usuario se agregó correctamente.
  - Ejemplo de respuesta:
    ```
    {
        "status": "Usuario creado con éxito"
    }
    ```

#### Uso:
Para agregar un nuevo usuario, realiza una solicitud POST a la URL `/api/v1/users` con los parámetros `username` y `password` en el cuerpo de la solicitud. El nombre de usuario y la contraseña deben proporcionarse como cadenas.

### 2. Iniciar sesión

**URL:** `/api/v1/login`

**Método:** `POST`

**Descripción:** Permite a un usuario iniciar sesión y obtener un token de acceso.

**Parámetros de entrada:**
- `username` (cadena): Nombre de usuario.
- `password` (cadena): Contraseña del usuario.

**Respuestas:**
- Código 200 OK: El inicio de sesión fue exitoso. Se devuelve un token de acceso.
  - Ejemplo de respuesta:
    ```
    {
        "access_token": "<token>"
    }
    ```
- Código 401 Unauthorized: Las credenciales proporcionadas son incorrectas.

#### Uso:
Para iniciar sesión, realiza una solicitud POST a la URL `/api/v1/login` con los parámetros `username` y `password` en el cuerpo de la solicitud. El nombre de usuario y la contraseña deben proporcionarse como cadenas. Si las credenciales son correctas, se devolverá un token de acceso en la respuesta.

### 3. Obtener todos los usuarios

**URL:** `/api/v1/usersAll`

**Método:** `GET`

**Descripción:** Obtiene todos los usuarios registrados en la base de datos.

**Respuestas:**
- Código 200 OK: Se obtienen los usuarios correctamente.
  - Ejemplo de respuesta:
    ```
    [
        {
            "_id": "<ID>",
            "username": "<username>",
            "password": "<password>"
        },
        ...
    ]
    ```

#### Uso:
Para obtener todos los usuarios, realiza una solicitud GET a la URL `/api/v1/usersAll`. Se devolverá una lista de todos los usuarios registrados en la base de datos.

### 4. Obtener un usuario por ID

**URL:** `/api/v1/users/<users_id>`

**Método:** `GET`

**Descripción:** Obtiene un usuario específico según su ID.

**Parámetros de entrada:**
- `users_id` (cadena): ID del usuario.

**Respuestas:**
- Código 200 OK: Se obtiene el usuario correctamente.
  - Ejemplo de respuesta:
    ```
    {
        "_id": "<ID>",
        "username": "<username>",
        "password": "<password>"
    }
    ```
- Código 404 Not Found: No se encontró ningún usuario con el ID especificado.

#### Uso:
Para obtener un usuario por su ID, realiza una solicitud GET a la URL `/api/v1/users/<users_id>`, donde `<users_id>` es el ID

 del usuario que deseas obtener. Se devolverá el usuario correspondiente si se encuentra, de lo contrario, se devolverá un código de estado 404.

### 5. Eliminar un usuario por ID

**URL:** `/api/v1/user/<user_id>`

**Método:** `DELETE`

**Descripción:** Elimina un usuario específico según su ID.

**Parámetros de entrada:**
- `user_id` (cadena): ID del usuario.

**Respuestas:**
- Código 204 No Content: El usuario se eliminó correctamente.
- Código 404 Not Found: No se encontró ningún usuario con el ID especificado.

#### Uso:
Para eliminar un usuario por su ID, realiza una solicitud DELETE a la URL `/api/v1/user/<user_id>`, donde `<user_id>` es el ID del usuario que deseas eliminar. Se devolverá un código de estado 204 si el usuario se eliminó correctamente, de lo contrario, se devolverá un código de estado 404.

# Notas importantes

- Se requiere la conexión a una base de datos MongoDB. El URI de conexión está configurado en el código de la aplicación.
- Algunas rutas de los endpoints están comentadas con la anotación `#@jwt_required()`, lo cual indica que se requiere autenticación mediante JSON Web Tokens (JWT) para acceder a ellas.
