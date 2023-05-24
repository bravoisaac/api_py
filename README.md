
**instalar dependencias:**
    
        pip install flask_jwt_extended
        pip install pymongo
        pip install flask_restful
        pip install flask  
        pip install bson 
        

**iniciar servidor:**

        python app.py
        python appProducto.py
        python appCompra.py 


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
        "username":"Test",
        "password":"111111"
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
Aquí tienes la documentación de la API proporcionada con referencias sobre cómo utilizar cada función:

# API de Productos

Esta API permite realizar operaciones relacionadas con la gestión de productos.

## Endpoints

### 1. Agregar un nuevo producto

**URL:** `/api/v1/products`

**Método:** `POST`

**Descripción:** Agrega un nuevo producto a la base de datos.

**Parámetros de entrada:**
- `name` (cadena): Nombre del nuevo producto.
- `description` (cadena): Descripción del nuevo producto.
- `price` (número): Precio del nuevo producto.
- `marca` (cadena): Marca del nuevo producto.
- `stock` (entero): Cantidad en stock del nuevo producto.

**Parámetros de entrada ejemplo posman:**
  - Ejemplo de POST:
    ```
    {
        "name": "PC Gamer Ultimate",
        "description": "Potente computadora para juegos de última generación",
        "price": 2499.99,
        "marca":"azus",
        "stock": 5
    }
    ```

**Respuestas:**
- Código 200 OK: El producto se agregó correctamente.
  - Ejemplo de respuesta:
    ```
    {
        "status": "Producto creado con éxito"
    }
    ```

#### Uso:
Para agregar un nuevo producto, realiza una solicitud POST a la URL `/api/v1/products` con los parámetros `name`, `description`, `price`, `marca` y `stock` en el cuerpo de la solicitud. Los valores deben proporcionarse de acuerdo a los tipos especificados. 

### 2. Obtener todos los productos

**URL:** `/api/v1/productsAll`

**Método:** `GET`

**Descripción:** Obtiene todos los productos registrados en la base de datos.

**Respuestas:**
- Código 200 OK: Se obtienen los productos correctamente.
  - Ejemplo de respuesta:
    ```
    [
        {
            "_id": "<ID>",
            "name": "<name>",
            "description": "<description>",
            "price": <price>,
            "marca": "<marca>",
            "stock": <stock>
        },
        ...
    ]
    ```

#### Uso:
Para obtener todos los productos, realiza una solicitud GET a la URL `/api/v1/productsAll`. Se devolverá una lista de todos los productos registrados en la base de datos.

### 3. Obtener un producto por ID

**URL:** `/api/v1/product/<product_id>`

**Método:** `GET`

**Descripción:** Obtiene un producto específico según su ID.

**Parámetros de entrada:**
- `product_id` (cadena): ID del producto.

**Respuestas:**
- Código 200 OK: Se obtiene el producto correctamente.
  - Ejemplo de respuesta:
    ```
    {
        "_id": "<ID>",
        "name": "<name>",
        "description": "<description>",
        "price": <price>,
        "marca": "<marca>",
        "stock": <stock>
    }
    ```
- Código 404 Not Found: No se encontró ningún producto con el ID especificado.

#### Uso:
Para obtener un producto por su ID, realiza una solicitud GET a la URL `/api/v1/product/<product_id>`, donde `<product_id>` es el ID del producto que deseas obtener. Se devolverá el producto correspondiente si se encuentra, de lo contrario, se devolverá un código de estado 404.

### 4. Actualizar un producto por ID

**

URL:** `/api/v1/product/<product_id>`

**Método:** `PUT`

**Descripción:** Actualiza un producto específico según su ID.

**Parámetros de entrada:**
- `product_id` (cadena): ID del producto.
- `name` (cadena): Nuevo nombre del producto.
- `description` (cadena): Nueva descripción del producto.
- `price` (número): Nuevo precio del producto.
- `marca` (cadena): Nueva marca del producto.
- `stock` (entero): Nueva cantidad en stock del producto.

**Parámetros de entrada ejemplo posman:**
  - Ejemplo de PUT:
    ```
    {
        "name": "Nuevo nombre del producto",
        "description": "Nueva descripción del producto",
        "price": 99.99,
        "marca":"Nueva marca del producto",
        "stock": 10
    }
    ```

**Respuestas:**
- Código 200 OK: El producto se actualizó correctamente.
  - Ejemplo de respuesta:
    ```
    {
        "status": "Producto actualizado con éxito"
    }
    ```
- Código 404 Not Found: No se encontró ningún producto con el ID especificado.

#### Uso:
Para actualizar un producto por su ID, realiza una solicitud PUT a la URL `/api/v1/product/<product_id>`, donde `<product_id>` es el ID del producto que deseas actualizar. Los parámetros `name`, `description`, `price`, `marca` y `stock` deben proporcionarse en el cuerpo de la solicitud con los nuevos valores que deseas asignar al producto.

### 5. Eliminar un producto por ID

**URL:** `/api/v1/product/<product_id>`

**Método:** `DELETE`

**Descripción:** Elimina un producto específico según su ID.

**Parámetros de entrada:**
- `product_id` (cadena): ID del producto.

**Respuestas:**
- Código 204 No Content: El producto se eliminó correctamente.
- Código 404 Not Found: No se encontró ningún producto con el ID especificado.

#### Uso:
Para eliminar un producto por su ID, realiza una solicitud DELETE a la URL `/api/v1/product/<product_id>`, donde `<product_id>` es el ID del producto que deseas eliminar. Se devolverá un código de estado 204 si el producto se eliminó correctamente, de lo contrario, se devolverá un código de estado 404.
Aquí tienes la documentación de la API que has proporcionado:

# API de Pedidos

Esta API permite realizar operaciones relacionadas con la gestión de pedidos.

## Endpoints

### 1. Crear un nuevo pedido

**URL:** `/api/v1/orders`

**Método:** `POST`

**Descripción:** Crea un nuevo pedido.

**Parámetros de entrada:**
- `users_id` (cadena): ID del cliente que realiza el pedido.
- `produc_id` (cadena): ID del producto solicitado en el pedido.
- `quantity` (entero): Cantidad del producto solicitado.

**Parámetros de entrada ejemplo Posman:**
  - Ejemplo de POST:
    ```
    {
        "users_id": "6464037c0a4eb752b6c7c966",
        "produc_id": "646aeebaeaae2aef3abb7c8e",
        "quantity": 1
    }
    ```

**Respuestas:**
- Código 200 OK: El pedido se creó correctamente.
  - Ejemplo de respuesta:
    ```
    {
        "status": "Pedido creado con éxito"
    }
    ```
- Código 404 Not Found:
  - Si no se encuentra el cliente con el ID especificado: `{"status": "Cliente no encontrado"}`.
  - Si no se encuentra el producto con el ID especificado: `{"status": "Producto no encontrado"}`.
- Código 400 Bad Request: Si el producto no tiene stock suficiente.
  - Ejemplo de respuesta: `{"status": "Stock insuficiente"}`.

#### Uso:
Para crear un nuevo pedido, realiza una solicitud POST a la URL `/api/v1/orders` con los parámetros `users_id`, `produc_id` y `quantity` en el cuerpo de la solicitud. Asegúrate de proporcionar los IDs válidos del cliente y el producto, así como la cantidad requerida. Si el cliente y el producto existen y hay suficiente stock disponible, se creará el pedido y se actualizará el stock del producto.

### 2. Actualizar un pedido por ID

**URL:** `/api/v1/order/<order_id>`

**Método:** `PUT`

**Descripción:** Actualiza un pedido específico según su ID.

**Parámetros de entrada:**
- `order_id` (cadena): ID del pedido.
- `users_id` (cadena): Nuevo ID del cliente que realiza el pedido.
- `produc_id` (cadena): Nuevo ID del producto solicitado en el pedido.
- `quantity` (entero): Nueva cantidad del producto solicitado.

**Parámetros de entrada ejemplo Posman:**
  - Ejemplo de PUT:
    ```
    {
        "users_id": "6464037c0a4eb752b6c7c966",
        "produc_id": "646aeebaeaae2aef3abb7c8e",
        "quantity": 2
    }
    ```

**Respuestas:**
- Código 200 OK: El pedido se actualizó correctamente.
  - Ejemplo de respuesta:
    ```
    {
        "status": "Pedido actualizado con éxito"
    }
    ```
- Código 404 Not Found:
  - Si no se encuentra el pedido con el ID especificado: `{"status": "Pedido no encontrado"}`.
  - Si no se encuentra el cliente con el ID especificado: `{"status": "Cliente no encontrado"}`.
  - Si no se encuentra el producto con el ID especific

ado: `{"status": "Producto no encontrado"}`.
- Código 400 Bad Request: Si el producto no tiene stock suficiente.
  - Ejemplo de respuesta: `{"status": "Stock insuficiente"}`.

#### Uso:
Para actualizar un pedido por su ID, realiza una solicitud PUT a la URL `/api/v1/order/<order_id>`, donde `<order_id>` es el ID del pedido que deseas actualizar. Los parámetros `users_id`, `produc_id` y `quantity` deben proporcionarse en el cuerpo de la solicitud con los nuevos valores que deseas asignar al pedido. Asegúrate de proporcionar IDs válidos del cliente y el producto, y verificar que haya suficiente stock disponible antes de actualizar el pedido.

### 3. Eliminar un pedido por ID

**URL:** `/api/v1/order/<order_id>`

**Método:** `DELETE`

**Descripción:** Elimina un pedido específico según su ID.

**Parámetros de entrada:**
- `order_id` (cadena): ID del pedido.

**Respuestas:**
- Código 204 No Content: El pedido se eliminó correctamente.
- Código 404 Not Found: No se encontró ningún pedido con el ID especificado.

#### Uso:
Para eliminar un pedido por su ID, realiza una solicitud DELETE a la URL `/api/v1/order/<order_id>`, donde `<order_id>` es el ID del pedido que deseas eliminar. Se devolverá un código de estado 204 si el pedido se eliminó correctamente, de lo contrario, se devolverá un código de estado 404.

## Notas importantes

- Se requiere la conexión a una base de datos MongoDB. El URI de conexión está configurado en el código de la aplicación.
- Algunas rutas de los endpoints están comentadas con la anotación `#@jwt_required()`, lo cual indica que se requiere autenticación mediante JSON Web Tokens (JWT) para acceder a ellas.
- Asegúrate de proporcionar IDs válidos del cliente y el producto, y verificar el stock disponible antes de realizar operaciones de creación y actualización de pedidos.
