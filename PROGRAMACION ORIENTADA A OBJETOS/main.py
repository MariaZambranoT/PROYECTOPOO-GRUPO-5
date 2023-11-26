#GRUPO 5
#INTEGRANTES:
#ASENCIO MADESCO CARLOS ALEXIS - GONZALEZ RAMIREZ CARLOS ANTONIO - ZAMBRANO TUMBACO MARIA ANGELICA

from revista import Revista
from libro import Libro
from docente import Docente
from estudiante import Estudiante


# Docentes
d1 = Docente(cedula = '0000000001', nombre = 'GUILLERMO', apellido= 'VALAREZO', email='gvalarezo@gmail.com', telefono='0909090909', direccion='s/n', numero_libros=0, activo=True, carrera='ISAC', titulo_3er_nivel='ING', titulo_4to_nivel='MAE')
d2 = Docente(cedula = '0000000002', nombre = 'JOSE', apellido= 'CORDOVA', email='gvalarezo@gmail.com', telefono='0909090909', direccion='s/n', numero_libros=0, activo=True, carrera='ISAC', titulo_3er_nivel='MGS', titulo_4to_nivel='MAE')
print(d1)
print(d2)

# Estudiantes
e1 = Estudiante(cedula = '0958275927', nombre = 'MARIA', apellido= 'ZAMBRANO', email='mzambrano@gmail.com', telefono='0998888888', direccion='el fortin', numero_libros=0, activo=True, carrera='GIG', nivel=3)
e2 = Estudiante(cedula = '0980435681', nombre = 'CARLOS', apellido= 'GONZALES', email='cgonzalezr@gmail.com', telefono='0999999999', direccion='S/N', numero_libros=0, activo=True, carrera='GIG', nivel=3)
print(e1)
print(e2)

l1 = Libro(codigo='1', autor='ELVIS', titulo='DESARROLLO EN PYTHON', anio=2019, editorial='USA', disponible=True, cantidad_disponible=10,tipo_pasta='DURA')
print(l1)