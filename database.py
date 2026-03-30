import sqlite3

# --- Función para crear las tablas ---
def inicializar_db():
    # Creación del archivo de la base de datos
    conexion = sqlite3.connect('gestion_tareas.db')
    cursor = conexion.cursor()

    # Creación de la tabla de Usuarios
    # Se guarda el 'password_hash' para que sea seguro
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_usuario TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')

    # Creación de la tabla de Tareas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            id_usuario INTEGER,
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
        )
    ''')

    conexion.commit()
    conexion.close()
    print("¡Base de datos y tablas creadas con éxito!")

if __name__ == "__main__":
    inicializar_db()