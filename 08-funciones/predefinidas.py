# nombre = "klk"
# #Funciones generales

# print(type(nombre))


# #Detectar el tipado

# comprobar = isinstance(nombre, str)

# if comprobar:
#     print("Esa variable es un string")
# else:
#     print("El valor no coincide ")
    
# if not isinstance(nombre, float):
#     print("La variable no es un numero con decimales")
    


# #Limpiar espacios

# frase = "        mi contenido       "
# print (frase)
# print (frase.strip())

# #eliminar variables

# year = 2022

# print(year)

# del year 
# print(year)

#Comprobar variable vacia

# texto = " ff "

# if len(texto) <= 0:
#     print("La variable está vacia")
# else:
#     print(f"La variable tiene caracteres {len(texto)}")
    
#Encontrar caracteres

# frase = "La vida es bella"

# print(frase.find("vida"))

#Reemplazar palabras en un string

frase = "anuel"

nueva_frase = frase.replace("anuel", "moto")
print(nueva_frase)


#Mayusculas y minusculas
nombre = "nombre"

print(nombre)
print(nombre.lower()) #Para convewrtir a minusculas
print(nombre.upper()) #Para convertir a mayusculas
