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

compra = float(input("digite el valor de su compra: "))

if compra < 800:
    compra = compra
    print(f"el valor de su compra es {compra}")
elif compra >= 800 and compra <= 1500:
    compra = compra - (compra * 0.10)
    print(
        f"felicidades tienes un descuento en tu compra del 10% cancela: {compra}")
elif compra > 1500 and compra <= 5000:
    compra = compra - (compra * 0.15)
    print(
        f"felicidades tienes un descuento en tu compra del 15% ancela: {compra}")
elif compra > 5000:
    compra = compra - (compra * 0.20)
    print(
        f"felicidades tienes un descuento en tu compra del 20% ancela: {compra}")