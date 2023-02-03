import os 
from pathlib import Path, PurePath

#Nombre de ruta de scrip de python
#print(type(os.getcwd())) #obtener un texto de la ruta
#print(type(Path.cwd())) #obtener funcionalidades extras


#Listar archivos o carpetas, me retorna todos los archivos y carpetas de proyecto

#print(os.listdir())
#print(os.listdir('09-Listas'))

#print(list(Path('11-ejercicios').iterdir()))

#Unir rutas

#print(os.path.join(os.getcwd(), '11-ejercicios'))

#print(PurePath.joinpath(Path.cwd(), '13-paquetes')) #Para unir correctamente


#4 como crear carpetas usando python

#os.mkdir('Prueba')
#Path('Prueba').mkdir(exist_ok=True) #Crear la carpeta pero con path


#Crear carpetas dentro de carpetas

#os.makedirs(os.path.join('Prueba','Scripts'))
#PurePath.joinpath(Path.cwd(), 'Prueba2' , 'Scripts2').mkdir(parents=True) #Otra forma de crear caretas dentro de carpetas


#RENOMBRAR ARCHIVOS O CARPETAS

#os.rename('Prueba2', 'Pruebilla')

''' path_actual = Path('Pruebilla', )
path_objetivo = Path('Pruebilla2', )

Path.rename(path_actual, path_objetivo)

for file in os.listdir(): #Renombrar archivos de extencion en especifico, por ejemplo csv
    if file.endswith('.csv'):
     os.rename(file,f'2021_{file}') '''
     

#COMPROBAR SI EXITE UN ARCHIVO

''' print(os.path.exists('Pruebilla2')) '''

''' archivo = Path('Pruebilla20')
print(archivo.exists()) '''


#METADATA DATA QUE DESCRIBE OTRA DATA

#print(os.path.abspath('Pruebilla2'))

# script = Path('ficheros.py')

# print(script.resolve())
# print(script.stem)
# print(script.suffix) #Que tipo de archivo es
# print(script.stat().st_size) 
