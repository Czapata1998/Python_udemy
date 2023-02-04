"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer funcion que recorra lista de numeros y devuelva un string
- Ordenarla y mostrarla  
- Mostrar su longitud
- Buscar algun elemento que el usuario pida por teclado
"""

#SOLUCION MIA
# enteros = [8, 1, 7, 2, 6, 3, 5, 4]

# print (8 in enteros)

# print(len(enteros))

# enteros.sort()
# print(enteros)

# for enteros in range(1, 9):
#     print(enteros)
    
#SOLUCION UDEMY

#Crear la lista

numeros = [4, 6, 7, 9, 2, 4, 13, 15,16]

#Recorrer y mostrar

# print("##### Recorrer y mostrar#####")
# mostrarLista = "mostrar lista"
# for numero in numeros:
#     print(numero)
    
# print(mostrarLista(numeros))
# print(mostrarLista(["Kevin", "Jovy", "Cristhian"]))

# #Oedenar y mostrar    
# print("##### ORDENAR Y MOSTRAR #####")

# numeros.sort()

# print(mostrarLista(numeros))

print("##### Recorrer y mostrar#####")

numero = [3, 5, 7, 9, 10, 13]

busqueda = int(input("Introduce el numero: "))

comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el numero: "))
else:
    print(f"Has introducido el {busqueda}")
    
print(f"buscar en la lista {busqueda}")

search = numeros.index(busqueda)
print(f"el numero buscado en la lista indice es {search}")












 


    

    

