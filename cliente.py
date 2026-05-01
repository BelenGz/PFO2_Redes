import requests

URL_BASE = "http://127.0.0.1:5000"

def menu_principal():
    print("\n--- SISTEMA DE GESTIÓN DE TAREAS ---")
    print("1. Registrarse")
    print("2. Iniciar Sesión")
    print("3. Salir")
    return input("Elegí una opción: ")

def menu_tareas():
    while True:
        print("\n--- PANEL DE TAREAS (SESIÓN INICIADA) ---")
        print("1. Ver Bienvenida (Tareas)")
        print("2. Cerrar Sesión")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            r = requests.get(f"{URL_BASE}/tareas")
            print("\nRespuesta del servidor:", r.text)
        elif opcion == "2":
            print("Cerrando sesión y volviendo al menú principal...")
            break

def registrar_usuario():
    usuario = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    datos = {"usuario": usuario, "contraseña": password}
    
    respuesta = requests.post(f"{URL_BASE}/registro", json=datos)
    
    if respuesta.status_code == 201:
        print(f"¡Éxito! {respuesta.json().get('mensaje')}")
    else:
        print(f"Error {respuesta.status_code}: {respuesta.json().get('error')}")

def login_usuario():
    usuario = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    datos = {"usuario": usuario, "contraseña": password}
    
    respuesta = requests.post(f"{URL_BASE}/login", json=datos)
    
    if respuesta.status_code == 200:
        print("\n¡Éxito!", respuesta.json().get("mensaje"))
        # Acceso permitido: Entramos al submenú de tareas
        menu_tareas()
    else:
        print("\nError:", respuesta.json().get("error"))

if __name__ == "__main__":
    while True:
        opcion = menu_principal()
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login_usuario()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break