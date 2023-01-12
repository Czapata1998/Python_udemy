"""""
¿CUANTO ES EL X % DE X NUMERO? SACAR PORCENTAJE A NUMEROS
"""""

numero_1 = int(input ("favor ingrese un numero: "))

porcentaje = int(input(f"que porcentaje desea sacar de {numero_1}: "))

operacion = (numero_1 * (porcentaje/100))

print(f"el {porcentaje}% de {numero_1} es: {operacion}")