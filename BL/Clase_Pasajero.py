from Clase_Persona import Persona
import re #Esta biblioteca funciona para realizar validación de atributos

class Pasajero(Persona):
    def __init__(self, identificacion, nombre, apellido1, apellido2, fechaNacimiento, genero, activo, idCabina, cantidadPasajeros):
        super().__init__(self, identificacion, nombre, apellido1, apellido2, fechaNacimiento, genero, activo)
        self.idCabina = idCabina
        self.cantidadPasajeros = cantidadPasajeros
        
    def registrar(self):
        # Validación de identificación
        while True:
            self.identificacion = input("Digite el número de identificación del pasajero: ").strip()
            if self.identificacion:
                break
            else:
                print("El número de identificación no puede estar vacío o contener solo espacios.")
        # Validación del nombre
        while True:
            self.nombre = input("Digite el nombre del pasajero: ").strip()
            if self.nombre:
                break
            else:
                print("El nombre no puede estar vacío o contener solo espacios.")
        # Validación del primer apellido
        while True:
            self.apellido1 = input("Digite el primer apellido del pasajero: ").strip()
            if self.apellido1:
                break
            else:
                print("El primer apellido no puede estar vacío o contener solo espacios.")
        # Validación del segundo apellido
        while True:
            self.apellido2 = input("Digite el segundo apellido del pasajero: ").strip()
            if self.apellido2:
                break
            else:
                print("El segundo apellido no puede estar vacío o contener solo espacios.")
        # Validación de la fecha de nacimiento en formato yyyy-MM-dd
        while True:
            self.fechaNacimiento = input("Digite la fecha de nacimiento del pasajero (yyyy-MM-dd): ").strip()
            if re.match(r"^\d{4}-\d{2}-\d{2}$", self.fechaNacimiento):
                break
            else:
                print("Formato de fecha no válido. Use el formato yyyy-MM-dd.")
        # Validación del género
        while True:
            gen = input("""
            Seleccione el género:
            F - Femenino
            M - Masculino
            """).strip().upper()
            if gen in ["F", "M"]:
                self.genero = gen
                break
            else:
                print("Opción no válida. Ingrese 'F' para Femenino o 'M' para Masculino.")
        #Valida que sea un dato entero        
        while True:
            try:
                cantidad_personas = int(input("Digite la cantidad de personas: ").strip())
                if cantidad_personas > 0:
                    self.cantidadPasajeros = cantidad_personas
                    break
                else:
                    print("La cantidad de personas debe ser un número entero positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
        objPasajero = Pasajero(self.identificacion, 
                               self.nombre, 
                               self.apellido1, 
                               self.apellido2, 
                               self.fechaNacimiento, 
                               self.genero, 
                               activo=True, 
                               idCabina=None, 
                               cantidadPasajeros=self.cantidadPasajeros)                
                
    def modificar(self):
        pass
    
    def listar(self):
        pass
    
    def desactivar(self):
        pass 