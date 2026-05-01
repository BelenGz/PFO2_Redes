import requests

URL_BASE = "http://127.0.0.1:5000"

def menu():
    print("\n--- SISTEMA DE GESTIÓN DE TAREAS ---")
    print("1. Registrarse")
    print("2. Iniciar Sesión")
    print("3. Ver Bienvenida")
    print("4. Salir")
    return input("Elegí una opción: ")

def registrar_usuario():
    usuario = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    
    datos = {"usuario": usuario, "contraseña": password}
    
    # Se realiza el pedido al servidor
    respuesta = requests.post(f"{URL_BASE}/registro", json=datos)
    
    # --- MODIFICACIÓN AQUÍ ---
    if respuesta.status_code == 201:
        print(f"¡Éxito! {respuesta.json().get('mensaje')}")
    else:
        print(f"Error {respuesta.status_code}: {respuesta.json().get('error')}")

def login_usuario():
    usuario = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    
    datos = {"usuario": usuario, "contraseña": password}
    
    # Verificación de credenciales
    respuesta = requests.post(f"{URL_BASE}/login", json=datos)
    
    if respuesta.status_code == 200:
        print("¡Éxito!", respuesta.json().get("mensaje"))
    else:
        print("Error:", respuesta.json().get("error"))

if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login_usuario()
        elif opcion == "3":
            # Prueba rápida del GET
            r = requests.get(f"{URL_BASE}/tareas")
            print("\nRespuesta del servidor:", r.text)
        elif opcion == "4":
            break