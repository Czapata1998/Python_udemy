from io import open
import pathlib
import shutil 

# #Abrir archivo o carpeta

# ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
# archivo = open(ruta, "a+")



# #Ecribir dentro de un archivo o fichero

# archivo.write("****Soy algo agregado desde python*******\n")

# #Cerrar archivo

# archivo.close()

# #Abrir archivos
# ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
# archivo_lectura = open(ruta, "r+")

# #Leer contenido

# contenido = archivo_lectura.read()

# print(contenido)

# #Leer contenido y guardarlo en lista

# lista = archivo_lectura.readlines
# archivo_lectura.close()

# for frase in lista:
#     ''' lista_frase = frase.split()
#     print(lista_frase) '''
#     print("- " +frase.upper())
    
# #Copiar archivos

# ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
# ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
# shutil.copyfile(ruta_original, ruta_nueva)


#Mover archivos 

''' ruta_original = str(pathlib.Path().absolute()) + "/.ficheros.py"
ruta_nueva = str(pathlib.Path().absolute()) + "/./ficheros.py"

shutil.move(ruta_original, ruta_nueva) '''

#ELIMINAR ARCHIVOS

import os
''' ruta_nueva = str(pathlib.Path().absolute()) + "/ficheros.py"
os.remove(ruta_nueva) '''


#Comprobar si una archvo existe o no

import os.path

#print (os.path.abspath("../"))
ruta_comprobar = os.path.abspath("./") + "./ficheros.py"
ruta_comprobar = "./ficheros.py"
ruta = str(pathlib.Path().absolute()) + "./ficheros.py"

if os.path.abspath (ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")