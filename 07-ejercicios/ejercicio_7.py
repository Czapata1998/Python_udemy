"""""
Hacer un programa que muestre los numeros impares entre dos numeros que decida el usuario
"""""

numero1 = int(input("favor digita un numero: "))
numero2 = int(input("favor digita un numero: "))

if numero1 < numero2:
    for contador in range(numero1, (numero2 + 1)):
        if contador%2 ==0:
            print(f"{contador} es PAR")
        else:
            print(f"{contador} es IMPAR")
else:
    print("El numero 1 debe ser mayor al 2")