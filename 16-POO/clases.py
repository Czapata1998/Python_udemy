# Programacion orientada a objetos

# DEFINIR UNA CLASE (molde para crear mas objetos de este tipo)
# (coche) con caracteristicas similares

class Coche:
    # Atributos o propiedades o variables
    # caracteristicas del coche
    color = "Verde"
    marca = "Camaro"
    modelo = 2022
    velocidad = 200
    caballaje = 500
    plazas = 2

    # Metodos, son acciones que hacen el objeto (coche) (funciones)
    def setcolor(self, color):  #para modificar un valor de una propiedad
        self.color = color
        
    def getcolor(self):  #para obtener un valor de una propiedad
        return self.color   

    def setmarca(self, marca):  #para modificar un valor de una propiedad
        self.marca = marca
        
    def getmarca(self):
            return self.marca

    def setmodelo(self, modelo):
        self.modelo = modelo

    def acelerar(self):
        self.velocidad += 7

    def frenar(self):
        self.velocidad -= 4

    def getvelocidad(self):
        return self.velocidad

    def setmodelo(self, modelo):
        self.modelo = modelo
        
    def getmodelo(self): #para obtener un valor de una propiedad
        return self.modelo
    
    def setcaballaje(self, caballaje):
        self.caballaje = caballaje
    
    def getcaballaje(self):
        return self.caballaje


# Fin definicion clase

# Crear objetos o instanciar clases
Coche = Coche()

Coche.setmarca("Audi") #Para cambiar los atributos o variables ya definidos de la clase
Coche.setcolor("Amarillo")
Coche.setmodelo(2020)


print(Coche.getmarca(), Coche.getcolor(), Coche.getmodelo()) # Obtener los valores de los atributos o variables

# SE PUEDE COLOCAR .velocidad PERO CON GET ES LA MANERA CORRECTA DE MANIPULAR LOS METODOS
print(f"Velocidad actual: ", Coche.getvelocidad())

Coche.acelerar()
Coche.acelerar()
Coche.acelerar()
Coche.acelerar()  # Aumento la velocidad del coche llamando los metodos o funciones
Coche.frenar()  # Disminuyo la velocidad del coche llamando los metodos o funciones
Coche.frenar()
Coche.frenar()

# SE PUEDE COLOCAR .velocidad PERO CON GET ES LA MANERA CORRECTA DE MANIPULAR LOS METODOS
print("Velocidad nueva: ", Coche.getvelocidad())

print('---------------NUEVO COCHE-------------')
#Crear mas objetos

Coche2 = Coche
print("Coche 2")

Coche2.setcolor("Azul")
Coche2.setmarca("Mercedes")
Coche2.setmodelo(2021)
Coche2.setcaballaje(400)

print(Coche2.getmarca(), Coche2.getcolor(), Coche2.getmodelo(), Coche2.getcaballaje())

print(type(Coche2))

