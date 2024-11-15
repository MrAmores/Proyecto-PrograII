from DB_CONFIG.conexion import conexionDB    
class Rol():
    conexion = conexionDB()  # Se establece una única conexión para toda la clase
    miconexion = conexion.cursor()
    
    def __init__(self, idRol, nombre, descripcion, departamento, salario, activo):
        self.idRol = idRol
        self.nombre = nombre
        self.descripcion = descripcion
        self.departamento = departamento
        self.salario = salario
        self.activo = activo
    
    def capturaDatos(self):
        # Validación de idRol
        while True:
            self.idRol = input("Digite el ID del rol: ").strip()
            if self.idRol:
                break
            else:
                print("El ID del rol no puede estar vacío o contener solo espacios.")
                
        # Validación de nombre
        while True:
            self.nombre = input("Digite el nombre del rol: ").strip()
            if self.nombre:
                break
            else:
                print("El nombre del rol no puede estar vacío o contener solo espacios.")
        
        # Validación de descripción
        while True:
            self.descripcion = input("Digite la descripción del rol: ").strip()
            if self.descripcion:
                break
            else:
                print("La descripción no puede estar vacía o contener solo espacios.")
        
        # Validación de departamento
        while True:
            self.departamento = input("Digite el departamento del rol: ").strip()
            if self.departamento:
                break
            else:
                print("El departamento no puede estar vacío o contener solo espacios.")   
        # Validación de salario como número decimal positivo
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
                            
        # Crear instancia con datos capturados
        objRol = Rol(self.idRol, self.nombre, self.descripcion, self.departamento, self.salario, True)
        objRol.ingresaRol()

    def ingresaRol(self):
        # Consulta SQL de inserción
        ingreso = "INSERT INTO rol (idRol, nombre, descripcion, departamento, salario) VALUES (%s, %s, %s, %s, %s, %s)"
        datos = (self.idRol, self.nombre, self.descripcion, self.departamento, self.salario, self.activo)
        # Ejecutar la consulta e ingresar datos
        Rol.miconexion.execute(ingreso, datos)
        Rol.conexion.commit()
        print("Se ha ingresado el rol exitosamente.")

    def modificaRol(self, nombre, descripcion, departamento, salario, id):
        # Consulta SQL de modificación
        modificar = ("update rol set nombre = %s, "
                     "descripcion = %s, "
                     "departamento = %s,"
                     "salario = %s,"
                     "where idRol = %s")
        datos = (nombre, descripcion, departamento, salario, id)
        # Ejecutar la consulta y modificar datos
        Rol.miconexion.execute(modificar, datos)
        Rol.conexion.commit()
        print("Se han modificado los datos del rol exitosamente.")

    def listar(self):
        print("Listado de roles en el sistema:")
        # Ejecutar la consulta y listar datos
        Rol.miconexion.execute("select * from rol")
        datos = Rol.miconexion.fetchall()
        for i in datos:
            print(i)

    def desactivaRol(self, id):
        modificar = "UPDATE rol SET activo = %s WHERE idRol = %s"
        datos = (False, id)
        # Ejecutar la consulta y inactivar datos
        Rol.miconexion.execute(modificar, datos)
        Rol.conexion.commit()
        print("Se ha borrado el rol exitosamente.")

    