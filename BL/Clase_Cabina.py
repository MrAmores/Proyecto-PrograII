from DB_CONFIG.conexion import conexionDB
class Cabina():
    conexion = conexionDB()
    miconexion = conexion.cursor()

    def __init__(self, idCabina, capacidad, disponibilidad, tamanho, precio):
        self.idCabina = idCabina
        self.capacidad = capacidad
        self.disponibilidad = disponibilidad
        self.tamanho = tamanho
        self.precio = precio

    def capturaDatos(self):
        # Validation of idCabina
        while True:
            self.idCabina = input("Digite el ID de la cabina: ").strip()
            if self.idCabina:
                self.disponibilidad=True
                break
            else:
                print("El ID de la cabina no puede estar vacío o contener solo espacios.")
                
        # Validation of capacity
        while True:
            try:
                self.capacidad = int(input("Digite la capacidad de la cabina: ")).strip()
                if self.capacidad:
                    break
                else:
                    print("La capacidad de la cabina no puede estar vacía o contener solo espacios.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
        
        # Validation of size
        while True:
            self.tamanho = input("Digite el tamaño de la cabina: ").strip()
            if self.tamanho:
                break
            else:
                print("El tamaño de la cabina no puede estar vacío o contener solo espacios.")
        # Validation of price
        while True:
            try:
                precio = float(input("Digite el precio de la cabina: ").strip())
                if precio > 0:
                    self.precio = precio
                    break
                else:
                    print("El precio debe ser un número positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

    def ingresaCabina(self):
        # Consulta SQL de inserción
        ingreso = "INSERT INTO cabina (idCabina, capacidad, disponibilidad, tamanho, precio) VALUES (%s, %s, %s, %s, %s)"
        datos = (self.idCabina, self.capacidad, self.disponibilidad, self.tamanho, self.precio)
        # Ejecutar la consulta e ingresar datos
        Cabina.miconexion.execute(ingreso, datos)
        Cabina.conexion.commit()
        print("Se ha ingresado la cabina exitosamente.")

    def modificaCabina(capacidad, disponibilidad, tamanho, precio, id):
        # Consulta SQL de modificación
        modificar = ("update cabina set capacidad = %s, "
                     "disponibilidad = %s, "
                     "tamanho = %s,"
                     "precio = %s,"
                     "where idCabina = %s")
        datos = (capacidad, disponibilidad, tamanho, precio, id)
        # Ejecutar la consulta y modificar datos
        Cabina.miconexion.execute(modificar, datos)
        Cabina.conexion.commit()
        print("Se han modificado los datos de la cabina exitosamente.")

    def obtener_cabinas_disponibles(acompanantes):
        # Solicitar la información del usuario
            capacidad_cabina = acompanantes + 1
            # Consulta para filtrar cabinas disponibles según la capacidad requerida
            consulta = """
                SELECT * FROM cabinas
                WHERE disponibilidad = TRUE AND capacidad = %s
                ORDER BY capacidad;
            """
            Cabina.miconexion.execute(consulta, (capacidad_cabina,))
            cabinas_disponibles = Cabina.miconexion.fetchall()
            # Mostrar los resultados al usuario
            if cabinas_disponibles:
                print(f"\nCabinas disponibles para {capacidad_cabina} personas:")
                for cabina in cabinas_disponibles:
                    print(f"ID: {cabina[0]}, Capacidad: {cabina[1]}, Disponibilidad: {cabina[2]}, Tamaño: {cabina[3]}, Precio: {cabina[4]}")
                
                # Solicitar al usuario seleccionar una cabina
                id_seleccionado = input("\nIngrese el ID de la cabina que desea: ").strip()
                print(f"Ha seleccionado la cabina con ID: {id_seleccionado}")
            else:
                print("\nNo hay cabinas disponibles para la capacidad solicitada.")



            
    def agregar(self):
        pass
    
    def modificar(self):
        pass
    
    def listar(self):
        pass
    
    def desactivar(self):
        pass
    
