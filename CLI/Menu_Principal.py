from CLI.Pasajero_cli import mostrar_menu_pasajero
from CLI.Trabajador_cli import mostrar_menu_trabajador
from CLI.Cabina_cli import mostrar_menu_cabina
from CLI.Rol_cli import mostrar_menu_rol
from CLI.Servicio_cli import mostrar_menu_servicio
from CLI.Solicitud_cli import mostrar_menu_solicitud_servicio
def mostrar_menu_principal():
    opc = 0
    while True:
        print("""
        --------------------------------------
        ---       Sistema de Gestión       ---
        --------------------------------------
        1 - Gestión Pasajeros
        2 - Gestión Trabajadores
        3 - Gestión Cabinas
        4 - Gestión de Roles
        5 - Gestión Servicios
        6 - Gestión de Solicitud de Servicios
        7 - Salir
        --------------------------------------
        """)
        try:
            opc = int(input("Seleccione una opción: "))
            if opc == 1:
                mostrar_menu_pasajero()
            elif opc == 2:
                mostrar_menu_trabajador()
            elif opc == 3:
                mostrar_menu_cabina()
            elif opc == 4:
                mostrar_menu_rol()
            elif opc == 5:
                mostrar_menu_servicio()
            elif opc == 6:
                mostrar_menu_solicitud_servicio()
            elif opc == 7:
                print("SALIENDO DEL SISTEMA")
                break
            else:
                print("Opción no valida. Intente de nuevo.")
        except ValueError as e:
            print(f"Error: {e}. Intente ingresar un número válido.")