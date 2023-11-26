#GRUPO 5
#INTEGRANTES:
#ASENCIO MADESCO CARLOS ALEXIS - GONZALEZ RAMIREZ CARLOS ANTONIO - ZAMBRANO TUMBACO MARIA ANGELICA
from persona import Persona
class Estudiante(Persona):

    contador_estudiante = 0

    def __init__(self ,cedula :str ,nombre :str ,apellido :str ,email :str ,telefono :str ,direccion :str
                 ,numero_libros :int ,activo :bool ,carrera :str, nivel :int):
        Estudiante.contador_estudiante +=1
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libros = numero_libros
        self._activo = activo
        self._carrera = carrera
        self._id = Estudiante.contador_estudiante
        self._nivel = nivel
        super(Estudiante, self).__init__(cedula = cedula, nombre = nombre, apellido= apellido, email=email, telefono=telefono, direccion=direccion, numero_libros=numero_libros, activo=activo, carrera=carrera)

    def __str__ (self):
        return f' Estudiante : {self.__dict__.__str__()}'
    @property
    def id (self):
        return self._id
    @property
    def nivel(self):
        return self._nivel
    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    @classmethod
    def pedir_libro(self )->bool:
        pass

    @classmethod
    def devolver_libro(self )->bool:
        pass

if __name__ == '__main__':
    e1 = Estudiante(cedula = '0958275927', nombre = 'Maria', apellido= 'Zambrano', email='mzambrano@gmail.com', telefono='0998888888', direccion='el fortin', numero_libros=0, activo=True, carrera='GIG', nivel=3)
    e2 = Estudiante(cedula = '0980435687', nombre = 'Carlos', apellido= 'Gonzalez', email='cgonzalezr@gmail.com', telefono='0999999999', direccion='S/N', numero_libros=0, activo=True, carrera='GIG', nivel=3)

    print(e1)
    print(e2)
