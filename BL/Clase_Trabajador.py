from Clase_Persona import Persona
class Trabajador(Persona):
    def __init__(self, identificacion, nombre, apellido1, apellido2, fechaNacimiento, genero, activo, idRol):
        super().__init__(identificacion, nombre, apellido1, apellido2, fechaNacimiento, genero, activo)
        self.idRol=idRol
    
    def registrar(self):
        pass

    def modificar(self):
        pass

    def listar(self):
        pass

    def desactivar(self):
        pass