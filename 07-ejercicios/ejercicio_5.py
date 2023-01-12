"""""
Ejercicio 5. Hacer un programa que muestre
todos los numeros entre dos numeros que 
diga el usuario.
"""""

rango_1 = int(input("Favor ingrese el primer valor: "))
rango_2 = int(input("Favor ingrese el segundo valor: "))

if rango_1 < rango_2:
    for contador in range(rango_1, (rango_2 + 1)):
        print(contador )
        
else:
    print("El numero 1 debe ser menor al numero 2")