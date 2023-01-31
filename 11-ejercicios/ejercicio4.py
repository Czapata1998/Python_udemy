"""
Crear un script que tenga cuatro vaariables, una lista, un string, 
un entero y un booleano y que imprima un mensaje segun el tipo de dato de cada variable
"""


def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "El tipo de dato es una lista"
    elif tipo == str:
        result = "El tipo de dato es un String"
    elif tipo == int:
        result = "El tipo de dato es un entero"
    elif tipo == bool:
        result = "El tipo de dato es booleano"

    return result


def comprobarTipo(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""

    if test:
        result = f"Este dato es de tipo {traducirTipo(tipo)}"
    else:
        result= "El dato no es correcto"

    return result


mi_lista = ["Cris", 5, 77.4]

texto = "Hola, como vas"

numero = 77

verdadero = True

print(comprobarTipo(mi_lista, list))
print(comprobarTipo(texto, str))
print(comprobarTipo(numero, int))
print(comprobarTipo(verdadero, bool))
