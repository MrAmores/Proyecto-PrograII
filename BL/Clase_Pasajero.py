from BL.Clase_Persona import Persona
from BL.Clase_Cabina import Cabina 
from DB_CONFIG.conexion import conexionDB

class Pasajero(Persona):
    conexion = conexionDB()
    miconexion = conexion.cursor()
    
    def __init__(self, identificacion, nombre, apellido1, apellido2, fechaNacimiento, genero, activo, idCabina):
        super().__init__(identificacion, nombre, apellido1, apellido2, fechaNacimiento, genero, activo)
        self.idCabina = idCabina
                 
    def capturaDatos(self):
         # Validation of identification
        while True:
            self.identificacion = input("Digite el número de identificación del pasajero: ").strip()
            if self.identificacion:
                self.activo = True
                break
            else:
                print("El número de identificación no puede estar vacío o contener solo espacios.")
        # Validation of name
        while True:
            self.nombre = input("Digite el nombre del pasajero: ").strip()
            if self.nombre:
                break
            else:
                print("El nombre no puede estar vacío o contener solo espacios.")
        # Validation of the first last name
        while True:
            self.apellido1 = input("Digite el primer apellido del pasajero: ").strip()
            if self.apellido1:
                break
            else:
                print("El primer apellido no puede estar vacío o contener solo espacios.")
        # Validation of the second last name
        while True:
            self.apellido2 = input("Digite el segundo apellido del pasajero: ").strip()
            if self.apellido2:
                break
            else:
                print("El segundo apellido no puede estar vacío o contener solo espacios.")
                
        # Validation of date of birth in yyyy-MM-dd format
        while True:
            try:
                anhoNacimiento = int(input("Digite el año de nacimiento del pasajero: ").strip())
                if anhoNacimiento > 0:
                    self.fechaNacimiento = anhoNacimiento
                    break
                else:
                    print("El año de nacimiento debe de ser una numero positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")     
        # Gender validation
        while True:
            gen = input("""
            Seleccione el género:
            F - Femenino
            M - Masculino
            """).strip().upper()
            if gen == "F":
                self.genero = "Femenino"
                break
            elif gen == "M":
                self.genero = "Masculino"
            else:
                print("Opción no válida. Ingrese 'F' para Femenino o 'M' para Masculino.")
                
        while True:
            try:
                cantidad_pasajeros = int(input("Digite la cantidad de acompañantes que vienen con usted: "))
                if cantidad_pasajeros > 0:
                    print("No se permite ingresar números negativos.")
                else:
                    Cabina.obtener_cabinas_disponibles(cantidad_pasajeros)
                    while True:
                        try:
                            cabina = int(input("Selecione el id de la cabina: ").strip())
                            if cabina > 0:
                                self.idCabina = cabina
                                break
                            else:
                                print("Entrada inválida. Por favor, ingrese un número entero.")
                        except ValueError:
                            print("Entrada inválida. Por favor, ingrese un número entero.")           
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")           
                              
    def modificar(self, nombre, apell_1, apell_2, anho_nacimiento, genero, id):
         # Consulta SQL de modificación
        modificar = ("update pasajero set nombre = %s, "
                     "apell_1 = %s, "
                     "apell_2 = %s,"
                     "anho_nacimiento = %s,"
                     "genero = %s,"
                     "where idPasajero = %s")
        datos = (nombre, apell_1, apell_2, anho_nacimiento, genero, id)
        # Ejecutar la consulta y modificar datos
        Pasajero.miconexion.execute(modificar, datos)
        Pasajero.conexion.commit()
        print("Se han modificado los datos del pasajero exitosamente.")
    
    def listar(self):
        print("Listado de pasajeros en el sistema:")
        # Ejecutar la consulta y listar datos
        Pasajero.miconexion.execute("select * from pasajero")
        datos = Pasajero.miconexion.fetchall()
        for i in datos:
            print(i)
    
    def desactivar(self, id):
        modificar = "UPDATE pasajero SET activo = %s WHERE idRol = %s"
        datos = (False, id)
        # Ejecutar la consulta y inactivar datos
        Pasajero.miconexion.execute(modificar, datos)
        Pasajero.conexion.commit()
        print("Se ha borrado el pasajero exitosamente.")
    
    def ingresaPasajero(self):
        # Consulta SQL de inserción
        ingreso = "INSERT INTO pasajero (idPasajero, nombre, apell_1, apell_2, anho_nacimiento, genero, activo, idCabina) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (self.identificacion, self.nombre, self.apellido1, self.apellido2, self.fechaNacimiento,self.genero,self.activo,self.idCabina)
        # Ejecutar la consulta e ingresar datos
        Pasajero.miconexion.execute(ingreso, datos)
        Pasajero.conexion.commit()
        print("Se ha ingresado al pasajero exitosamente.")       
    
    

