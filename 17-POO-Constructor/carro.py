class Moto: 
    #Atributos o propiedads (Variables)
    #caracteristicas del coche
    color = "Verde"
    marca = "Victory"
    modelo = "Bomber"
    velocidad = 300
    caballaje = 200
    plazas = 4

    
    soy_publico = "Hola soy un atributo publico"
    
    __soy__privado = "Hola soy un atributo privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas


    #Metodos, son acciones que hace el objeto (coche) (funciones)
    
    def getPrivado(self):
        return self.__soy__privado
    
    def setcolor(self, color): # esta funcion se usa para cambiar el color, o el valor del atributo o variable
        self.color = color
        
    def getcolor(self): # Esta funcion se usa para obtener el color o el nuevo valor de la variable o atributo
        return self.color
    
    def setmodelo(self, modelo): # Se cambia el modelo
        self.modelo = modelo
        
    def getmodelo (self): # se trae el valor del modelo
        return self.modelo
    
    def setmarca(self, marca): # Se cambia el modelo
        self.marca = marca
        
    def getmarca (self): # se trae el valor de la marca
        return self.marca
        
    def setcaballaje(self, caballaje): # Se cambia el Caballaje
        self.caballaje = caballaje
        
    def getcaballaje(self): # se trae el valor de la marca
        return self.caballaje
    
    def setplazas(self, plazas): # Se cambia el valor del atributo plazas
        self.plazas = plazas
        
    def getplazas(self): # se trae el valor de la marca
        return self.plazas
        
    def acelerar(self):
        self.velocidad += 3
    
    def frenar(self):
        self.velocidad -= 8
        
    def getvelocidad(self):
        return self.velocidad
    
    def getInfo(self):
        
        Info = "---Info del coche---"
        Info += "\n color: " + self.getcolor()
        Info += "\n marca: " + self.getmarca()
        Info += "\n modelo: " + str(self.getmodelo()) #Se formatea el tipo de dato para que lea como str y no como int
        Info += "\n caballaje: " + str(self.getcaballaje()) #Se formatea el tipo de dato para que lea como str y no como int
        Info += "\n velocidad: " + str(self.getvelocidad()) #Se formatea el tipo de dato para que lea como str y no como int
        Info += "\n plazas: " + str(self.getplazas()) #Se formatea el tipo de dato para que lea como str y no como int
        
        return Info
        
