def holamundo(nombre):
    return f"Hola que tal estas, {nombre}"


def restar(op1, op2):
    print(f"El resultado es {op1-op2}")
    
def multiplicar(op1, op2):
    print(f"El resultado es {op1*op2}")
    
def dividir(op1, op2):
    print(f"El resultado es {op1/op2}")

''' 
def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2
    
    cadena = ""
    
    if basicas == False:
      cadena += "Suma: " + str(suma)
      cadena += "\n"
      cadena += "Resta: " + str(resta)
      cadena += "\n"
    else:
      cadena += "multiplicacion: " + str(multi)
      cadena += "\n"
      cadena += "Division: " + str(division)
    
    return cadena

print(calculadora(5, 2, True)) '''
