"""""
Hacer un programa que pida numero al usuario indefinidamene hasta que meta un 111
"""""

contador = 1

while contador < 100:
    numero = int(input("Introduce un numero: "))
    
    if numero == 111 or 13 :
        print("lo encontraste weeeeee")
        break
    else:
        print(f"Has introducido el {numero}")
    