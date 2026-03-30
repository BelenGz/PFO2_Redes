# PFO 2: Sistema de Gestión de Tareas con API y Base de Datos
Este proyecto consiste en una API REST desarrollada con Flask que permite el registro y la autenticación de usuarios de forma segura, utilizando SQLite para la persistencia de datos.

## Instrucciones de Ejecución

1) Preparar la base de datos: Ejecutar el archivo ` database.py ´ para crear las tablas de usuarios y tareas.

<<<<<<< HEAD
2) Iniciar el servidor: Ejecutar `servidor.py`. El servidor quedará activo en `http://127.0.0.1:5000`.

3) Interactuar con el cliente: En una nueva terminal, ejecutar cliente.py para registrar usuarios e iniciar sesión.

# Preguntas conceptuales
**¿Por qué hashear contraseñas?**

El hasheo es una medida de seguridad crítica. Al convertir la contraseña en un código irreversible (hash), nos aseguramos de que, si la base de datos es comprometida, nadie pueda ver las contraseñas originales en texto plano. Esto protege la identidad y seguridad de los usuarios.

**Ventajas de usar SQLite en este proyecto**

Simplicidad: No requiere configurar un servidor de base de datos externo (como MySQL o PostgreSQL).

Portabilidad: Toda la base de datos es un único archivo (.db), lo que facilita mover el proyecto entre diferentes computadoras.

Eficiencia: Es ideal para aplicaciones de escritorio o proyectos de mediana escala como este sistema de gestión.
