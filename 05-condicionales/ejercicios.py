print("####\n EJERCICIO 1####")
# Costruir un programa que al recibir como dato el salario de un profesor de una universidad calcule
# el incremento del salario de acuerdo con el siguiente criterio y escriba el nuevo salario del profesor.

# Salario < $ 18,000 entonces incremente un 12%
# $18,000 <= salario  <= $30.000 entonces incremento 8%
# $30.000 > salario <= $50,000 entonces incremento de un 7%
# $50,000 > salario entonces incremento de 6%


# salario = float(input("Ingrese el salario del profe, porfa:  "))

# if salario  < 18000:
#     salario += (salario * 0.12)

#     print(f"Su nuevo salario es {salario}")

# elif salario >= 18000 and salario <= 30000:
#      salario += (salario * 0.08)
#      print(f"su nuevo salario es: {salario}")

# elif salario > 30000 and salario <= 50000:
#      salario += (salario * 0.07)
#      print(f"su nuevo salario es: {salario}")


# elif salario > 50000:
#      salario += (salario * 0.06)
#      print(f"su nuevo salario es: {salario}")

print("####\n EJERCICIO 2####")
# Construir programa que determine, al recibir como datos dos numeros enteros, si un numero
# es divisor de otro.

# Datos: N1 y N2 (variables de tipo entero que representan los datos que se ingresan)


# numero_1 = int(input("Favor ingrese un umero: "))
# numero_2 = int(input("Favor ingrese un umero: "))

# if numero_1 % numero_2 == 0:
#     print("el numero es divisible")
# else:
#     print("valio burguer")


print("####\n EJERCICIO 3 ####")

# Construir un programa que, al recibir como datos de entrada tres valores enteros diferentes entre si,
# determine si los mismos están en orden creciente

# numero_1 = int(input("Favor ingrese un numero: "))
# numero_2 = int(input("Favor ingrese un numero mayor al anterior: "))
# numero_3 = int(input("Favor ingrese un numero mayor al anterior: "))

# if numero_1 < numero_2 and numero_3:
#     print(f"los numeros son: {numero_1}, {numero_2}, {numero_3}")

# else:
#     print("Porfa ingrese numeros mayores en forma creciente")


# if numero_1 < numero_2 and numero_2 < numero_3:
#     print("Porfa ingrese numeros mayores en forma creciente")
# else:
#     print(f"los numeros son: {numero_1}, {numero_2}, {numero_3}")


print("####\n EJERCICIO 4####")

# En una tienda departamental ofrecen descuentos a los clientes en la navidad, de acuerdo con el monto de su compra. El criterio para establecer el descuento se muestra abajo.
# Contruye un programa que, al recibir como dato el monto de la compra del cliente, obtenga el precio real que debe pagar luego de aplicar el descuento correspondiente.

# compra < $800 entonces descuento 0%
# $800 <= compra <= $1500 entonces descuento del 10%
# $1500 < compra <= $5000 entonces descuento de 15%
# $5000 < compra entonces descuento de 20%

# compra = float(input("digite el valor de su compra: "))

# if compra < 800:
#     compra = compra
#     print(f"el valor de su compra es {compra}")
# elif compra >= 800 and compra <= 1500:
#     compra = compra - (compra * 0.10)
#     print(
#         f"felicidades tienes un descuento en tu compra del 10% cancela: {compra}")
# elif compra > 1500 and compra <= 5000:
#     compra = compra - (compra * 0.15)
#     print(
#         f"felicidades tienes un descuento en tu compra del 15% ancela: {compra}")
# elif compra > 5000:
#     compra = compra - (compra * 0.20)
#     print(
#         f"felicidades tienes un descuento en tu compra del 20% ancela: {compra}")


print("####\n EJERCICIO 5####")

# Costruir un programa que, al recibir como datos tres numeros reales, identifique cual es el mayor.
# considera que los numeros pueden ser iguales

# numero_1 = int(input("Ingrese un numero real: "))
# numero_2 = int(input("Ingrese un numero real: "))
# numero_3 = int(input("Ingrese un numero real: "))

# if numero_1 == numero_2 and numero_3:
#     print("los numeros son iguales")
# elif numero_1 > numero_2 and numero_1 > numero_3:
#     print("El numero 1 la tiene mas larga")
# elif numero_2 > numero_1 and numero_2 > numero_3:
#     print("El numero 2 la tiene mas grandee")
# elif numero_3 > numero_1 and numero_3 > numero_2:
#     print("La tres es la mas mejor")

print("####\n EJERCICIO 6####")

# Costruye un programa que te permita convertir de pulgadas a milimetros,
# de yardas a metros y de millas a kilometros

# Consideraciones
# - 1 pulgada equivale a 25.40 milimetros.
# - 1 yarda equivale a 0.9114 metros
# - 1 milla equivale a 1.6093 kilometros

# solucion con condicionales

# opcion = int(input("**MENÚ**  \n1. pulgadas a milimetros \n2. Yardas a metros \n3. Millas a kilometros \n"
#                      "Ingrese la opcion que desea: "))

# if opcion == 1:
#     pulgadas=int(input("Ingrese la cantidad de pulgadas a convertir: "))
#     milimetros = pulgadas * 25.40
#     print(f"{pulgadas} pulgadas equivalen a : {milimetros} milimetros")
# elif opcion == 2:
#     yarda = int(input("Ingrese la cantidad de yardas a convertir: "))
#     metros = yarda * 0.9114
#     print(f"{yarda} yardas equivalen a: {metros} metros")
# elif opcion == 3:
#     milla = int(input("Ingrese la cantidad de millas a convertir: "))
#     kilometro = milla * 1.6093
#     print(f"{milla} millas equivalen a: {kilometro} kilometros")
# else:
#     print("las opciones no son validas")
    

print("####\n EJERCICIO 7####")
# En algunas oficinas del gobierno pagan horas extras a los burocratas, ademas de salarios correspondiente.

# Escribe un programa que permita calcular la cantidad a pagar a un trabajado tomando en cuenta su salario
# y las horas extra trabajadas.

# las horas extra se calculan en funcion de la informacion de abajo.

# cada trabajador puede tener como maximo 30 horas extra, si tiene mas, solo se le pagaran las primeras 30.
# los trabajadores con categoria 4 o mayor a 4 no podran recibir este beneficio.

# categoria 1 - $40 por hora extra
# categoria 2 - $50 por hora extra
# categoria 3 - $85 por hora extra    

# salario = float(input("Ingrese el salario del trabajador: "))

# categoria = int(input("Ingrese la categoria del trabajador:  "))

# if categoria == 1: 
#     numero_horas_extra=int(input("Ingrese la cantidad de horas extra que ha hecho el trabajador: "))
#     if numero_horas_extra < 30:
#         salario= salario +(numero_horas_extra * 40)
#         print(f"El salario del empleado es {salario}")
#     else:
#         salario += (30 * 40) 
#         print("es mucha plata bro")      
# elif categoria == 2:
#     numero_horas_extra=int(input("Ingrese la cantidad de horas extra que ha hecho el trabajador: "))
#     if numero_horas_extra < 30:
#         salario= salario + (numero_horas_extra * 50)
#         print(f"El salario del empleado es {salario}")
#     else:
#         salario += (30 * 50) 
#         print("es mucha plata bro")   
# elif categoria == 3:
#     numero_horas_extra=int(input("Ingrese la cantidad de horas extra que ha hecho el trabajador: "))
#     if numero_horas_extra < 30:
#         salario= salario + (numero_horas_extra * 85)
#         print(f"El salario del empleado es {salario}")
#     else:
#         salario += (30 * 85) 
#         print("es mucha plata bro") 
# else:
#     print("No puedes recibir el beneficio")        

print("####\n EJERCICIO 7####")

# Construye un programa que permita realizar la conversion de medida de pesos, longitud y volumen, de acuerdo 
# con las conversiones dadas.
# se deben escribir el valor a convertir, la medida en que se está expresando el valor, el nuevo valor y la nueva medida correspondiente.

# MEDIDAS DE LONGITUD

# 1 pulgada = 25.40 milimetros
# 1 yarda = 0.9144 metros 

# MEDIDAS DE VOLUMEN:
# 1 pie ^3 = 0.02832 metros ^3
# 1 yarda ^3 = 0.7646 metros ^3


# MEDIDAS DE PESO:

# 1 onza = 28.35 gramos
# 1 libra = 0.45359 kilogramos

# Switch case

# Condicionales 
# Diccionarios 

#con condicionales

opcion_medidas =int(input("***MENÚ PRINCIPAL***\n1 MEDIDAS DE LONGITUD\n2 MEDIDAS DE VOLUMEN"
                          "\n3 MEDIDAS DE PESO\n ESCOJA LA OPCIÓN QUE DESEA:"))


if opcion_medidas == 1:
    print("\n***MEDIDAS DE LONGITUD***\n")
    opcion_submenu=int(input("1. Pulgadas a milimetros \n2. Yardas a metros \n Escoja la opción que desea: "))
    
