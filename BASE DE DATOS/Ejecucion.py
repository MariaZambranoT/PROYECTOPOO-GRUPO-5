#GRUPO 5
#INTEGRANTES:
#ASENCIO MADESCO CARLOS ALEXIS - GONZALEZ RAMIREZ CARLOS ANTONIO - ZAMBRANO TUMBACO MARIA ANGELICA
from docente import Docente
from estudiante import Estudiante
from libro import Libro
from revista import Revista
from pedido import Pedido

# Creamos objetos de Docente
docente1 = Docente(cedula='1234567890', nombre='Juan', apellido='Perez', email='juan@gmail.com', telefono='123456789', direccion='Calle 123', numero_libros=0, activo=True, carrera='Informática', titulo_3er_nivel='Licenciatura', titulo_4to_nivel='Maestría')

# Creamos objetos de Estudiante
estudiante1 = Estudiante(cedula='987654322', nombre='Maria', apellido='Gomez', email='maria@gmail.com', telefono='987654321', direccion='Calle 456', numero_libros=0, activo=True, carrera='Ingeniería', nivel=3)

# Creamos objetos de Libro
libro1 = Libro(codigo='L001', autor='Autor Libro 1', titulo='Título Libro 1', anio=2022, editorial='Editorial 1', disponible=True, cantidad_disponible=10, tipo_pasta='Dura')

# Creamos objetos de Revista
revista1 = Revista(codigo='R001', autor='Autor Revista 1', titulo='Título Revista 1', anio=2022, editorial='Editorial 2', disponible=True, cantidad_disponible=5, tipo='Física')

# Creamos objetos de Pedido
pedido1 = Pedido(solicitante=estudiante1, lista_material=[libro1, revista1], fecha_prestamo='2023-01-01', fecha_devolucion='2023-01-15')

# Procedemos a imprimir información de los objetos creados
print(docente1)
print(estudiante1)
print(libro1)
print(revista1)
print(pedido1)