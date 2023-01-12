# condicionales IF

# color = "rojo"

# if color == "rojo":
#     print ("el color si es rojo")

# else:
#     print ("el color no es rojo we ")

# #condicional pidiendo datos por consola
# color = input("¿cual es mi color favorito?")

# if color == "rojo":
#     print ("el color si es rojo")

# else:
#     print ("el color no es rojo we ")

# //////////////////////////////////////////
# OPERADORES DE COMPARACION

# == igual
# != diferente
# < menor que
# > mayor que
# <= menor o igual que
# >= mayor o igual que

# Operadores lógicos
# and = y
# or = o
# ! = negacion
# not = no

print("\n///////////// ejemplo 1")

# year = 2021

# if year >= 2021:
#     print("el año es el correcto")
# else:
#     print("no es el año, año viejo")


print("\n///////////// ejemplo 2")

# year = int(input("en que año estamos?"))

# if year != 2023:
#     print("el año es el correcto")
# else:
#     print("Ese no es el año en el que estamos, pedazo de estúpido!!!")


# print("\n///////////// ejemplo 3 anidando condicionales")

# nombre = input("Digite su nombre ")

# ciudad = input("Digite su ciudad ")

# continente = input("Digite su continente ")

# edad = int(input("Digite su edad "))

# mayoria_edad = int(input("¿Cual es la mayoría de edad en tu país? "))

# if edad >= mayoria_edad:
#     print(f"{nombre}, eres mayor de edad")

#     if continente == "America" "Sur America" "america" "sur america":
#         print(
#             f"{nombre}, alto capo, {continente}, es hermoso y tu ciudad {ciudad}, tambien lo es")
#     else:
#         print(
#             f"que triste que no vivas en america y vivas en esa porqueria de {continente}")
# else:
#     print(f"{nombre}, eres muy chico aun")


print("\n///////////// ejemplo 4 ")


# dia = int(input("digite un numero del 1 al 7: "))

# if dia == 1:
#     print("Lunes")
# else:
#     if dia == 2:
#         print("Es martes")
#     else:
#         if dia == 3:
#             print("Es miercoles")
#         else:
#             if dia == 4:
#                 print("Es jueves")
#             else:
#                 if dia == 5:
#                     print("Es Viernes")
#                 else:
#                     if dia == 6:
#                         print("Es Sábado")
#                     else:
#                         if dia == 7:
#                             print("Es Domingo")
#                         else:
#                             print("chupa pijas")

print("\n///////////// ejemplo 5 ")

# dia = int(input("digita un numero del uno al 7 para saber el día: "))

# if dia == 1:
#     print("el dia es lunes bro ")
# elif dia ==2:
#     print("El dia es martes men")
# elif dia ==3:
#     print("el dia es miercoles")
# elif dia == 4:
#     print("el dia es jueves")
# elif dia == 5:
#     print("el dia es viernes")
# elif dia == 6:
#     print("sabaditoo, disfruta el fin de semana")
# elif dia == 7:
#     print("ya es domingooooooooo, disfrutalo ")
# else:
#     print("\n///////////// ATENCIONNNNN ")
#     print("nananananana digita la opcion que es, traga chotas ")



print("\n///////////// ejemplo 6 ")

# edad_minima = 18

# edad_maxima = 65

# edad_oficial = int(input("¿Tienes edad para trabajar? Introduce tu edad: "))

# if edad_oficial >= 18 and edad_oficial <= 65:
    
#     print("es apto para trabajar")
# else:
#     print("No está en edad de trabjar")
    
    
print("\n///////////// ejemplo 7 ")

# pais = input("ingresa el pais donde vives: ")

# if pais == "Mexico" or pais == "España" or pais == "Colombia":
#     print(f"{pais}, Aca hablan español")
# else:
#     print(f"{pais}, aca hablan mamadas")
    
    
# print("\n///////////// ejemplo 8 ")

# pais = "dubai"

# if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
#     print(f"{pais}, Aca hablan mamadas")
# else:
#     print(f"{pais}, aca hablan español")


print("\n///////////// ejemplo 9 ")

pais = "ROMBIA"

if  pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais}, Aca no hablan Español")
else:
    print(f"{pais}, aca hablan español")