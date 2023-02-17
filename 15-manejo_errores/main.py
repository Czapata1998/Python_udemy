# Capturar errores y excepciones y manejar errores en codigo
# suceptibles a errores o fallos

''' try:
    nombre = input('Cual es tu nombre? :')

    if len(nombre) > 1:
        nombre_usuario = 'El nombre es: ' + nombre
    elif len(nombre) <= 1:
        print("El nombre es demasiado corto")


    print(nombre_usuario)
except:
    print("Ha ocurrido un error, ingresa bien el nombre")
    
else:
    print('Todo funciono correctamente')
    
finally:
    print("Fin de la iteraccion") '''

# print("##### Recorrer y mostrar#####")
# try:
#     numero = [3, 5, 7, 9, 10, 13]

#     busqueda = int(input("Introduce el numero: "))

#     comprobar = isinstance(busqueda, int)
#     while not comprobar or busqueda <= 0:
#      busqueda = int(input("Introduce el numero: "))
#     else:
#      print(f"Has introducido el {busqueda}")

#     print(f"buscar en la lista {busqueda}")

#     search = numero.index(busqueda)
#     print(f"el numero buscado en la lista indice es {search}")
# except:
#     print("El numero no existe en la lista, ingrese uno que si este")
# else:
#     print('Todo funciono correctamente')
    
# finally:
#     print("Fin de la iteraccion") 


# Multiples excepciones
# try:
#     numero = int(input("Numero para elevarlo al cuadrado: "))

#     print(f"El cuadrado de un numero es: {numero*numero}")
# except TypeError:
#     print("Debes ingresar numeros enteros, no textos, recuerda revisar si tus inputs si estan convertidos en enteros")
    
# except ValueError:
#     print("No Ingreses texto por favor ingresa numeros")
# except Exception as e:
#     print("H acorrido un error: ", type(e).__name__)  #Capturar el error de una forma mas elegante y ordenada
    


#Excepciones personalizadas
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad >= 110 or edad <= 5:
        ''' print("La edad introducida no es real, por favor introduce una verdadera")
        edad = int(input("Introduce la edad: ")) '''
        raise ValueError("La edad que se introdujo no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")

    else:
        print(f"Bienvenido al master en python {nombre}")
except ValueError:
    print("Introduce los datos correctamente")
    
    
