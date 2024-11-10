from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, identificacion, nombre, apellido1, apellido2, fechaNacimiento, genero, activo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.fechaNacimiento = fechaNacimiento
        self.genero = genero
        self.activo = activo
        
    @abstractmethod
    def registrar(self):
        pass
    @abstractmethod
    def modificar(self):
        pass
    @abstractmethod
    def listar(self):
        pass
    @abstractmethod
    def desactivar(self):
        pass

        
        

        
        
    
