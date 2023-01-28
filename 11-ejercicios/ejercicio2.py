"""
Ejercicio 2: escribir un programa que añada valores a una lista mientras su longitud sea menor a 120 y luego mostrar la lista, usar while y for 
"""

''' coleccion = []
contador = 0

while contador < 120:
    coleccion.append(f"elemento - {contador}")
    print(coleccion[contador])
    contador += 1

print(coleccion[77]) '''
coleccion = []

for contador in range (0, 120):
    coleccion.append(f"elemento- {contador}")
    print( coleccion[contador])
    
print(f"el resutado es {coleccion}")