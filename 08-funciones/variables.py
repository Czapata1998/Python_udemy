"""
Variables locales: Se definen dentro de la funcion y no
se puede usar fuera de ella, solo estan disponibles dentro.
A no ser que hagamos reurn.

Variables globales: Son las que se declaran fuera de una funcion y
estan disponibles dentro y fuera de ellas.
"""

#Variable global

frase = "pruebas de python"

print(frase)

def holaMundo():
    frase = "Hola mundo!!"
    print("dentro de la funcion")
    print(frase)
    
    year = 2021
    print(year)
    
holaMundo()