"""""
# FOR  ES UNA ESTRUCTURA ITERATIVA QUE SE VA REPETIR X VECES

#for variable in elemento_iterable (lista, rango, tupla, diccionarios etc)
     BLOQUE DE INSTRUCIONES

"""""
contador = 0
resultado = 0

for contador in range(0, 10):
    print(f"voy por el {str(contador)}")

    resultado = resultado + contador  # va sumando todos los elementos de la lista
    # resultado += contador // DE ESTA FORMA SE HACE LO MISMO Y DE MANERA MAS OPTIMA
print(f"el resultado es: {resultado}")

# EJEMPLO TABLAS DE MULTIPLICAR

print("\############### EJEMPLO ############")

numero_usuario = int(input("¿De que número quieres ver la tabla de multiplicar?: "))

if numero_usuario < 1:
    print("Favor coloca un numero de mayor rango")
    numero_usuario = int(input("Introduce el nuevo número: "))
if numero_usuario < 1:
    print("El sistema solo permite numeros mayores a 1")
    
    
 
print(f"### Tabla de multiplicar del número {numero_usuario} ####")

for numero_tabla in range(1, 11):
    if numero_usuario == 0:
        print("")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada bro")
