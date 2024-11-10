from Clase_Persona import Persona

class Pasajero(Persona):
    def __init__(self, identificacion, nombre, apellido1, apellido2, fechaNacimiento, genero, activo, idCabina, cantidadPasajeros):
        super().__init__(self, identificacion, nombre, apellido1, apellido2, fechaNacimiento, genero, activo)
        self.idCabina = idCabina
        self.cantidadPasajeros = cantidadPasajeros
        
    def registrar(self):
        """self.identificacion = input("Digite el número de identificación del pasajero: ")
        self.nombre = input("Digite el nombre del pasajero: ")
        self.apellido1 = input("Digite el primer apellido del pasajero: ")
        self.apellido2 = input("Digite el segundo apellido del pasajero: ")
        self.identificacion = input("Digite el número de identificación del pasajero: ")"""
    
    def modificar(self):
        pass
    
    def listar(self):
        pass
    
    def desactivar(self):
        pass 