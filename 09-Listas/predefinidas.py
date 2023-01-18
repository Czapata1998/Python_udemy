cantantes = ['eliud', 'kendo', 'nach', 'xxxtentacion', 'eladio carrion']

numeros = [1,2,9,4,6,7,5,8,8]

#Ordenar una lista SORT

print(numeros)

numeros.sort()
print(numeros)

#Añadir elementos

cantantes.append("Gabriel rodigrez")

cantantes.insert(1, "Niko eme") #Otro metodo para agregar a la lista

print(cantantes)

#Eliminar elementos de una lista

cantantes.pop(3)
cantantes.remove('eliud')

#print(cantantes)

#Dar la vuelta a la lista

print(numeros)
numeros.reverse()
print(numeros)

#Buscar dentro de una lista

print('nach' in cantantes)

#contar elementos
print(len(cantantes))

#cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

#Conseguir indice

print(cantantes.index("kendo"))

#Unir listas

cantantes.extend(numeros)

print(cantantes)