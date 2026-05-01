# PFO 2: Sistema de Gestión de Tareas con API y Base de Datos
Este proyecto consiste en una API REST desarrollada con Flask que permite el registro y la autenticación de usuarios de forma segura, utilizando SQLite para la persistencia de datos.

## Instrucciones de Ejecución

1) Preparar la base de datos: Ejecutar el archivo ` database.py ´ para crear las tablas de usuarios y tareas.

2) Iniciar el servidor: Ejecutar `servidor.py`. El servidor quedará activo en `http://127.0.0.1:5000`.

3) Interactuar con el cliente: En una nueva terminal, ejecutar cliente.py para registrar usuarios e iniciar sesión.

## Pruebas realizadas con Thunder Client

Para verificar el correcto funcionamiento de la API, se testearon los siguientes endpoints:

*   **POST `/registro`**: Creación de nuevos usuarios con almacenamiento de contraseña hasheada.
*   **POST `/login`**: Validación de credenciales comparando el texto plano enviado con el hash almacenado.
*   **GET `/tareas`**: Verificación de disponibilidad del servicio mediante el retorno de una estructura HTML de bienvenida.

# Preguntas conceptuales
**¿Por qué hashear contraseñas?**

El hasheo es una medida de seguridad crítica. Al convertir la contraseña en un código irreversible (hash), nos aseguramos de que, si la base de datos es comprometida, nadie pueda ver las contraseñas originales en texto plano. Esto protege la identidad y seguridad de los usuarios.

**Ventajas de usar SQLite en este proyecto**

Simplicidad: No requiere configurar un servidor de base de datos externo (como MySQL o PostgreSQL).

Portabilidad: Toda la base de datos es un único archivo (.db), lo que facilita mover el proyecto entre diferentes computadoras.

Eficiencia: Es ideal para aplicaciones de escritorio o proyectos de mediana escala como este sistema de gestión.

## Capturas de Pruebas Exitosa

### Registro de Usuario
![Registro](Capturas/registro_exitoso.png)

### Inicio de Sesión
![Login](Capturas/login_exitoso.png)

### Endpoint de Tareas
![Tareas](Capturas/endpoint_tareas.png)

### Vista en el navegador de Tareas
![HTML](Capturas/vista_navegador_tareas.png)