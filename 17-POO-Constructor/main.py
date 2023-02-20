from carro import Moto


Moto3 = Moto("Verde militar", "Ktm", 2019, 150, 200, 2)
Moto4 = Moto("Azul", "Pulsar", 2020, 150, 300, 4)
Moto5 = Moto("Rosa", "Discovery", 2022, 170, 100, 5)
Moto6 = Moto("Morado", "Benelli", 2013, 190, 80, 7)

print(Moto3.getInfo())
print("\n ---Tipos---")
print(Moto4.getInfo())
print("\n ---Tipos---")
print(Moto5.getInfo())
print("\n ---Tipos---")
print(Moto6.getInfo())



#DETECTAR TIPADO

if type(Moto5) == Moto: #Se compara el valor del objeto con la clase padre
    print("Es un objeto correcto")
else:
    print("No es un objeto")


#Visibilidad


#print(Moto.soy_publico)
#print(Moto.__soy_privado)
print(Moto.getPrivado(self=Moto))