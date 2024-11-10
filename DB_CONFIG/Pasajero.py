from CLI.Pasajero_cli import Pasajero

base_datos_pasajeros = []

# Simulación de una base de datos en una lista
def agregar_pasajero(pasajero):
    base_datos_pasajeros.append(pasajero)
    print(f"Pasajero {pasajero.nombre} agregado exitosamente.")

# Método para imprimir la lista de pasajeros
def imprimir_base_datos():
    print("Lista de pasajeros en la base de datos:")
    for pasajero in base_datos_pasajeros:
        print(pasajero)

# Creación de instancias de la clase Pasajero
pasajero1 = Pasajero("12345678", "Juan", "Pérez", "López", "1990-05-15", "M", True, "C001", 3)
pasajero2 = Pasajero("87654321", "María", "Gómez", "Díaz", "1985-08-20", "F", True, "C002", 2)
pasajero3 = Pasajero("11223344", "Carlos", "Ramírez", "Torres", "1992-12-01", "M", False, "C003", 1)

# Agregar pasajeros a la base de datos
agregar_pasajero(pasajero1)
agregar_pasajero(pasajero2)
agregar_pasajero(pasajero3)

# Imprimir la base de datos simulada
imprimir_base_datos()
