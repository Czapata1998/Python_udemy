"""""
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre concreto que pueden reutilizarse invocando a la funcion tantas veces como sea necesario


def nombreDeMiFuncion(parametros):
     #BLOQUE DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
"""""

# print("######## Ejemplo 1 ########")

# # Definiendo la funcion


#  def nombres_personas():
#     print("Victor")
#      print("Juan")
#      print("Adolfo")
#     print("Raul")
#      print("Kendo")
#      print("Cristhian")
#      print("\n")


#  Invocar funcion (la puedo invocae cuantas veces quiera)
# nombres_personas()

#  print("######## Ejemplo 2 ########")


#  def mostrar_nombre(nombre):
#      print(f"tu nombre es {nombre}")


#  mostrar_nombre("cristhian")
#  mostrar_nombre("mauro")
#  mostrar_nombre("jovy")

#  #########################################


#  def mostrar_nombre(nombre, edad):
#      print(f"tu nombre es {nombre}")

#      if edad >= 18:
#          print("y eres mayor de edad")
# #    else:
#          print("eres un crio jodeer")


#  nombre = input("Introduce tu nombre: ")
#  edad = int(input("Introduce tu edad: "))
#  mostrar_nombre(nombre, edad)


#  print("######## Ejemplo 3 ########")


#  def tabla(numero):
#      print(f"tabla de multiplicar del {numero}")

#      for contador in range(11):
#          operacion = numero*contador
#          print(f"{numero} x {contador} = {operacion}")
#      print("\n")

#  tabla(3)
#  tabla(7)
#  tabla(6)


#  print("######## Ejemplo 3.1 ########")

#  for ntabla in range(1, 11):
#      tabla(ntabla)


#  print("######## Ejemplo 3.2 ########")

#  numero = int(input("Digite un numero entero: "))

#  for tabla in range(1, 11):
#      print(f"{numero} x {tabla} = {tabla * numero} ")

print("######## Ejemplo 4 ########")

#Parametros opcionales


def getEmpleado(nombre, dni=None):
     print("Empleado")
     print(f"Nombre: {nombre}")
     if dni != None:
       print(f"DNI: {dni}")
       

getEmpleado("Cristhian Zapata", "3207928312")

# Ejemplo 5: parametros opcionales y return devolver datos


def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    
    return saludo

print( saludame("Cristhian Zapata"))


print("\n######## Ejemplo calculadora ########")

    
def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2
    
    cadena = ""
    
    if basicas == False:
      cadena += "Suma: " + str(suma)
      cadena += "\n"
      cadena += "Resta: " + str(resta)
      cadena += "\n"
    else:
      cadena += "multiplicacion: " + str(multi)
      cadena += "\n"
      cadena += "Division: " + str(division)
    
    return cadena

print(calculadora(5, 2, True))
    
    
    
print("\n######## Ejemplo 7 ########")


def getNombre(nombre):
    texto = f"El nombre {nombre} "
    return texto

def getApellidos(apellido):
    texto = f"El apellido es {apellido} "
    return texto

def Devuelvetodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" +  getApellidos(apellido)
    return texto

print(Devuelvetodo("cris", "zapata"))


print("\n######## Ejemplo 8 funciones lambda ########")

dime_el_año = lambda year: f"el año es {year * 2 }"

print(dime_el_año(2034))


# Hola

# adioh

# desde el job