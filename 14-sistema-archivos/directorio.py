import os, shutil


#Crear carpeta

if not os.path.isdir("./prueba"): #Si en el directorio no se encuentra esta carpeta entonces creela
    os.mkdir("./prueba")
else:
    print('El directorio ya existe')
    
#Eliminar una carpeta

#os.rmdir('./prueba')

#COPIAR CARPETAS

''' ruta_original = "./prueba3"
ruta_nueva = "./fichero_copiado.txt"

shutil.copytree(ruta_original, ruta_nueva) '''

#Listar archivos que hay en una carpeta

print("Contenido de mi carpeta: ")

Contenido = os.listdir("./13-paquetes") #en una variable se almacen la solicitud y luego se llama con un print para mostrar el rersultado

print(Contenido)

#Tambien se pede hacarr de esta manera para recorrer el contenido de mi carpeta
for fichero in Contenido:
    print(f"fichero es {fichero}")
    