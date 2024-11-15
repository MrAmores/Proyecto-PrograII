class Rol():
    def __init__(self, idRol, nombre, descripcion, departamento, salario, activo):
        self.idRol=idRol
        self.nombre=nombre
        self.descripcion=descripcion
        self.departamento=departamento
        self.salario=salario
        self.activo=activo

    def registrar(self):
        # Validation of idRol
        while True:
            self.idRol = input("Digite el ID del rol: ").strip()
            if self.idRol:
                break
            else:
                print("El ID del rol no puede estar vacío o contener solo espacios.")
                
        # Validation of name
        while True:
            self.nombre = input("Digite el nombre del rol: ").strip()
            if self.nombre:
                break
            else:
                print("El nombre del rol no puede estar vacío o contener solo espacios.")
        
        # Validation of description
        while True:
            self.descripcion = input("Digite la descripción del rol: ").strip()
            if self.descripcion:
                break
            else:
                print("La descripción no puede estar vacía o contener solo espacios.")
        
        # Validación del departamento
        while True:
            self.departamento = input("Digite el departamento del rol: ").strip()
            if self.departamento:
                break
            else:
                print("El departamento no puede estar vacío o contener solo espacios.")
        
        # Validación del salario como número decimal positivo
        while True:
            try:
                salario = float(input("Digite el salario del rol: ").strip())
                if salario > 0:
                    self.salario = salario
                    break
                else:
                    print("El salario debe ser un número positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                        
        objRol = Rol(self.idRol, self.nombre, self.descripcion, self.departamento, self.salario, activo=True)

    def modificar(self):
        pass

    def listar(self):
        pass

    def desactivar(self):
        pass
    