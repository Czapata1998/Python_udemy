#La poo me permite que mi codigo sea escalabale sostenible y reutilizable
#Fundamentos de POO: CLASES: Es el molde que nos permite crear nuestros objetos
#ATRIBUTOS, PROPIEDADES O VARIABLES: Ejemplo: nombre, color, marca modelo, llantas
#METODOS: Acciones que puede hacer nuestro objeto, arrancar acelerar frenar, apagar luces, apagar la radio etc
#Abstraccion: Utilizar objetos sin conocer el funcionamiento interno, la clase funcionaria para otro cualquier tipo de objeto
#HERENCIA: Heredad unas de otras, como propiedades y metodos, por ejemplo un objeto moto, puede heredar el color de un carro
#MODULARIDAD: Dividir mi app en partes mas pequenas y mas concretas para que se enfoquen en algo mas especifico
#clases separadas que representan funciones de codigo en concreto, tambien para encapsular codigo que solo se usara en cosas muy especificas
#OCULTACION: Cada objeto tiene sus datos en concreto y solo deben modificarse desde dentro de la clase, y para esto es importante tener dentro de la clase los metodos getter y seterr


#Definir una clase (Molde para crear mas objetos de ese tipo)

class Moto: 
    #Atributos o propiedads (Variables)
    #caracteristicas del coche
    color = "Verde"
    marca = "Victory"
    modelo = "Bomber"
    velocidad = 300
    caballaje = 200
    plazas = 4
    
    #Metodos, son acciones que hace el objeto (coche) (funciones)
    def setcolor(self, color): # esta funcion se usa para cambiar el color, o el valor del atributo o variable
        self.color = color
        
    def getcolor(self): # Esta funcion se usa para obtener el color o el nuevo valor de la variable o atributo
        return self.color
    
    def setmodelo(self, modelo): # Se cambia el modelo
        self.modelo = modelo
    
    def setmarca(self, marca): # Se cambia el modelo
        self.marca = marca
        
    def getmodelo (self): # se trae el valor del modelo
        return self.modelo
    
    def getmarca (self): # se trae el valor de la marca
        return self.marca
        
    def acelerar(self):
        self.velocidad += 3
    
    def frenar(self):
        self.velocidad -= 8
        
    def getvelocidad(self):
        return self.velocidad
    
    
    #Fin definicion clase
    
    #Crear un objeto o instanciar la clase
    
coche = Moto() 

coche.setcolor("negro") #  Se le cambian los valores a la propiedad o variable
coche.setmodelo("Venom") # se le cambian los valores a la propiedad o variable

print(coche.getmarca(), coche.getmodelo(), coche.getcolor())
print("La velocidad de la moto es", coche.getvelocidad())
    
coche.acelerar()
coche.acelerar() # Llamamos a las funciones o metodos para modificar la funcion del objeto
coche.acelerar()
coche.acelerar()

coche.frenar()
coche.frenar()
coche.frenar()

print("La velocidad de la moto es:", coche.getvelocidad())


#Crear mas objetos 
print("----------Objeto numnero 2------------")


moto2 = Moto()

moto2.setcolor("amarillo")
moto2.setmodelo(2023)
moto2.setmarca("Bws")

print(moto2.getcolor(), moto2.getmodelo(), moto2.getmarca())


print(type(moto2))