# La HERENCIA ES: Posibilidad de compartir atributos y metodos entre clases, y que diferentes clases hereden de otras

class Persona:
    
    ''' 
    nombre
    apellidos
    altura
    edad 
    '''
    def getnombre(self):
        return self.nombre
    
    def getapellidos(self):
        return self.apellidos
    
    def getaltura(self):
        return self.altura
    
    def getedad(self):
        return self.edad
    
    def setnombre(self, nombre):
        self.nombre = nombre
    
    def setapellidos(self, apellidos):
        self.apellidos = apellidos
        
    def setaltura(self, altura):
        self.altura = altura
        
    def setedad (self, edad):
        self.edad = edad
        
        
    def hablar (self):
        return "Estoy hablando"
    
    def caminar (self):
        return "Estoy caminando"
    
    def dormir (self):
        return "Estoy mimido"
    
    
class informatico(Persona):
    '''
     lenguajes
     experiencia
    '''
    
    
    
    def __init__(self):
        self.lenguajes = "Htlm, css, javascript, python"
        self.experiencia = 5
        
    def getlenguajes(self):
        return  self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def repararapc(self):
        return "Reparando el pc"

        
        
    

    
    def getInfo(self):
            
        Info = "---Info de la perosna---"
        Info += "\n Nombre: " + self.getnombre()
        Info += "\n Apellidos: " + self.getapellidos()
        Info += "\n Altura: " + str(self.getaltura()) #Se formatea el tipo de dato para que lea como str y no como int
        Info += "\n edad: " + str(self.getedad()) #Se formatea el tipo de dato para que lea como str y no como int
       
            
        return Info
    

class TecnicoRedes(informatico):
    
    
    def __init__(self):
        super().__init__()
        self.auditarredes = "Experto"
        self.experienciaredes = 4
        
        
    def auditoria(self):
        return "Estoy auditando una red"
    

    
    
    
    
    
    