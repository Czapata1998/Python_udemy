"""""
While es una estructura de control que repite la ejecucion de una serie de instrucciones
tantas veces como sea necesario, hasta que deje de cumplirse la condicion 
while condicion:
   bloque de instrucciones
   actualizaciones de contador
"""""

# contador = 1

# while contador <= 100:
#     print(f"Estoy en el numero {contador}")
#     contador += 1
    
# #############################################

# contador = 1

# muestrame = str(0)

# while contador <= 100:
#     muestrame = muestrame + "," + str(contador)
#     contador = contador +1
    
# print(muestrame)


# print("\############### EJEMPLO ############")

numero_usuario = int(input("Introduce un numero porfavor, para la tabla: "))


if numero_usuario < 1:
    numero_usuario = 1
    
    
print(f"tabla del numero {numero_usuario}")

contador = 1

while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador}")
    contador += 1
else:
    print("tabla terminada")
       