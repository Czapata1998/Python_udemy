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

numeros = [10, 14, 20, 17, 11, 28, 30, 40, 29]

#Crear funcion que recorra lista y devuelva un string
print("##### RECORRA LISTA Y DEVUELVA UN STR #####")

def mostrarLista(lista):
    resultado = ""
    
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    return resultado

#RECORRER Y MOSTRAR

print("##### RECORRER Y MOSTRAR #####")

# for numero in numeros:
#     print(numero)
    
print(mostrarLista(numeros))
print(mostrarLista(["Kevin", "Andres", "Cristhian"]))

#Oedenar y mostrar    
print("##### ORDENAR Y MOSTRAR #####")

numeros.sort()
print(mostrarLista(numeros))


#Mostrar su longitud    
print("##### MOSTRAR SU LONGITUD #####")

print(len(numeros))


#Buscar un elemento que el cliente pida por teclado    
print("##### Busqueda en la lista #####")


busqueda = int(input("Introduce el número: "))

comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el número: "))
else:
    print(f"Haz introducido el {busqueda}")
    
print(f"### Buscar en la lista el número {busqueda} ###")

search = numeros.index(busqueda)

print(f"el numero buscado existe en la lista, es el indice {search}")
    











 


    

    

