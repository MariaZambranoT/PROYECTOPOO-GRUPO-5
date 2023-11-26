#GRUPO 5
#INTEGRANTES:
#ASENCIO MADESCO CARLOS ALEXIS - GONZALEZ RAMIREZ CARLOS ANTONIO - ZAMBRANO TUMBACO MARIA ANGELICA
from revista import Revista
from libro import Libro
from docente import Docente
from estudiante import Estudiante
class Pedido():
    contador_pedido = 0

    def __init__(self, solicitante, lista_material ,fecha_prestamo ,fecha_devolucion):
        Pedido.contador_pedido +=1
        self._id = Pedido.contador_pedido
        self._solicitante = solicitante
        self._lista_material = lista_material
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
    def __str__ (self):
        return f'Pedido: {self.__dict__.__str__()}'

    @property
    def id(self):
        return self._id
    @property
    def solicitante(self):
        return self._solicitante
    @solicitante.setter
    def solicitante(self, solicitante):
        self._solicitante = solicitante
    @property
    def lista_material(self):
        return self._lista_material
    @lista_material.setter
    def lista_material(self, lista_material):
        self._lista_material = lista_material
    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo
    @fecha_prestamo.setter
    def fecha_prestamo(self, fecha_prestamo):
        self._fecha_prestamo = fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion
    @fecha_devolucion.setter
    def fecha_devolucion(self, fecha_devolucion):
        self._fecha_devolucion = fecha_devolucion

    def pedir_material(list_materia, estudiante_docente, materia):
        pass

    def devolver_material(estudiante_docente):
        pass

if __name__ == '__main__':
    l1 = Pedido(solicitante ='Estudiante', lista_material = '', fecha_prestamo = '26/11/2023', fecha_devolucion = '28/11/2023')
    l2 = Pedido(solicitante ='Docente', lista_material = '', fecha_prestamo = '26/11/2023', fecha_devolucion = '27/11/2023')

    print(l1)
    print(l2)