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

print("##### Recorrer y mostrar#####")
mostrarLista = "mostrar lista"
for numero in numeros:
    print(numero)
    
print(mostrarLista(numeros))
print(mostrarLista(["Kevin", "Jovy", "Cristhian"]))

#Oedenar y mostrar    
print("##### ORDENAR Y MOSTRAR #####")

numeros.sort()

print(mostrarLista(numeros))










 


    

    

