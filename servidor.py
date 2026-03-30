from flask import Flask, request, jsonify
# Importación de herramientas para proteger las contraseñas
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

# --- Función para conectar con la base de datos ---
def conectar_db():
    return sqlite3.connect('gestion_tareas.db')

# --- REGISTRO DE USUARIOS ---
@app.route('/registro', methods=['POST'])
def registro():
    # Se reciben los datos del nuevo usuario
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')

    # PROTECCIÓN: Se convierte la contraseña en un texto cifrado
    password_encriptada = generate_password_hash(contrasena)

    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        # Se guarda en la base de datos SQLite
        cursor.execute('INSERT INTO usuarios (nombre_usuario, password_hash) VALUES (?, ?)', 
                       (usuario, password_encriptada))
        conexion.commit()
        conexion.close()
        return jsonify({"mensaje": "¡Usuario creado con éxito!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Ese nombre de usuario ya existe"}), 400

# --- INICIO DE SESIÓN ---
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')

    conexion = conectar_db()
    cursor = conexion.cursor()
    # Se busca al usuario por nombre
    cursor.execute('SELECT password_hash FROM usuarios WHERE nombre_usuario = ?', (usuario,))
    resultado = cursor.fetchone()
    conexion.close()

    # Se verifica si el usuario existe y si la contraseña coincide con el hash
    if resultado and check_password_hash(resultado[0], contrasena):
        return jsonify({"mensaje": "Bienvenido, inicio de sesión correcto"}), 200
    else:
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

# --- GESTIÓN DE TAREAS ---
@app.route('/tareas', methods=['GET'])
def tareas():
    # Mensaje de bienvenida en formato HTML
    return "<h1>Bienvenido al Sistema de Gestión de Tareas</h1><p>Página de inicio.</p>"

# --- Iniciar el servidor ---
if __name__ == "__main__":
    # El servidor correrá en http://127.0.0.1:5000
    app.run(debug=True, port=5000)