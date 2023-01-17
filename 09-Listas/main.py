"""
LISTAS (arrays)

Son colecciones o conjuntos de datos/valores, bajo
un unico nombre.
Para acceder a esos valores podemos usar un indice numerico.
"""

# pelicula = "Batman"
# peliculas = ["Avatar", "Gato con botas", "El señor de los anillos", "Superman", "Flash", "Harry potter"]
# cantantes = list(('Eliud', 'gabriel', 'shalom', 'Redimi2', 'Niko Eme' ))
# variada = ["nombre", 40, 25.3, True, "Texto"]

# años = list(range(2020,2030 +1))
# print(peliculas)
# print(cantantes)
# print(años)
# print(variada)

#Indices 

# peliculas[0] = "La monja" #Reemplazar elemento en una lista
# print(peliculas[1]) #Buscar un elemento puntual en una lista
# print(peliculas)
# print(cantantes[0:])

#Añadir elementos a lista

# cantantes.append("Rubinsky") #Añadir elementos a una lista

# print(cantantes)

#Recorrer listas 

# print("\n*******LISTADO DE PELICULAS*********")
# nueva_peli = ""
# while nueva_peli != "parar":
#     nueva_peli = input("Introduce la nueva pelicula: ")
#     if nueva_peli == "parar":
#         break
#     peliculas.append(nueva_peli)
    

# for pelicula in peliculas:
#     print(f"{peliculas.index(pelicula)+1} {pelicula}") 
    
    

#listas multidimencionales

print("\n********Listado de contactos**********")

contactos =[
    [
        'Cristhian',
        'cristhianjulian22@gmail.com'
    ],
    [
        'Kevin',
        'kevincachondo@gmail.com'
    ],
    [
        'Juank',
        'juank@gmail.com'
    ]
]
    
for contacto in contactos:
    print(contacto[0:1])
    



