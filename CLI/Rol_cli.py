from BL.Clase_Roles import Rol
def mostrar_menu_rol():
    while True:
        print("""
        ------------------------------
        ---    Gestión de Roles    ---   
        ------------------------------
        1 - Registrar Rol
        2 - Modificar Rol
        3 - Eliminar Rol
        4 - Listar Rol
        5 - Volver al Menú Principal
        ------------------------------
        """)
        try:
            opcion = int(input("Selecione una opción: ")) 
            
            if opcion == 1:
                pass
                # registrar()
            elif opcion == 2:
                pass
                # modificar()
            elif opcion == 3:
                pass
                # desactivar()
            elif opcion == 4:
                # listar()
                pass
            elif opcion == 5:
                break  
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as e: 
            print(f"Error: {e}. Intente ingresar un número válido.")
