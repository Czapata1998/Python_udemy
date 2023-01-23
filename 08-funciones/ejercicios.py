"""
Programa que tome 3 notas de un estudiante y diga la nota final del curso.
Tenga en cuenta que la primera y segunda nota valen el 30% de la nota final. La tercera nota vale el 40%
"""
# def calcularNota(nota_1, nota_2, nota_3):
#     return (nota_1*0.3) + (nota_2*0.3) + (nota_3*0.4)

# nota_1 = float(input("Ingresa la primer nota del estudiante: "))
# nota_2 = float(input("Ingresa la segunda nota del estudiante: "))
# nota_3 = float(input("Ingresa la tercer nota del estudiante: "))

# notaFinal = calcularNota(nota_1, nota_2, nota_3)

# if notaFinal <= 5.9:
#     print("El estudiante reprobó")
# elif notaFinal >= 6 and notaFinal <= 8:
#     print("El estudiante pasó bien")
# elif notaFinal >= 8.1 and notaFinal <= 10:
#     print("El estudiante sacó nota sobresaliente")
    

# print(f"la nota final del estudiante es {notaFinal}")


"""
Programa que calcule el IVA de una compra del 19% sobre el valor total de la compra
"""
# def calcularIva(compra):
#      iva = compra *0.19
#      return iva

# compra =  float(input("Ingrese el valor de su compra: "))

# iva = calcularIva(compra)

# print(f"el precio de la compra sin iva es de {compra} y mas el iva es {compra+iva}")


"""
Programa que calcule la tabla de multiplicar de cualquier numero entero
dado por el usuario. Debe calcular la tabla desde el 0 hasta el 12.
"""

# def calcularTabla(numero1, numero2):
#     return str(numero1) + "*" + str(numero2) + "=" + str(numero1*numero2)

# numero = int(input("Ingrese el numero entero: "))

# for entero in range(0, 13):
#     print(calcularTabla(numero, entero))

"""
Saludar 2
"""

# def saludar2 (nombre):
#     print(f"Hola {nombre} como estas?")
    
# # nombre = input("Ingresa tu nombre: ")

# saludar2("")
# saludar2("")
    
"""
Funciones con retorno
"""

# def suma(a, b):
#     resultado = a + b
#     return resultado

# valor = suma(10 , 5)

# print(f"la suma da como resultado {valor}")

# valor = suma(20 , 5)

# print(f"la suma da como resultado {valor}")


# def suma2 (a , b):
#     return a + b

# valorr = suma2(11, 9)

# print(f"la suma da como resultado {valorr}")



# def prueba (a, b):
#     Resultado = a + b
#     return  Resultado

# a = int(input("Ingrese el primer digito para la suma: "))
# b = int(input("Ingrese el segundo digito para la suma: "))

# resultado = prueba(a , b)

# print(f"El resultado es {resultado}")


def sonIguales (num1, num2):
    return num1 == num2

num1 = int(input("Ingrese el primer : "))
num2 = int(input("Ingrese el segundo digito : "))


result = sonIguales(num1, num2)
if (result == True):
    print("Los numeros son iguales")
else:
    print("Los numeros no coinciden")



print(f"El resultado es {result}")
    