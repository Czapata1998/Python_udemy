#Tkinter 
#Modulo para crear interfaces graficas de usuario


from tkinter import * #Importamos todo lo de la libreria
import os.path


class Programa:
    
    def __init__(self):
        self.title = "Python clases"
        self.icon = './21-tkinter/imagenes/brave.ico'
        self.icon_alt = './imagenes/brave.ico'
        self.size = "770x470"
        self.resizable = False
        
    def cargar(self):
        #Crear una ventana raiz
        ventana = Tk()
        self.ventana = ventana

        #Cambio en el tamano de la ventana
        ventana.geometry(self.size)

        #titulo de la ventana
        ventana.title(self.title)


        #comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon_alt)


        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon)

        #ICONO DE LA VENTANA
        ventana.iconbitmap(ruta_icono)


        #Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()



        #BLOQUEAR EL TAMANO DE LA VENTANA
        if self.resizable:
            
            ventana.resizable(1, 1)
            
        else:
            ventana.resizable(0, 0)



        # arrancar y mostrar la ventana hasta que se cierre
        #ventana.mainloop()

    def addTexto(self, dato):    
        texto = Label(self.ventana, text=dato )
        texto.pack()

    def mostrar(self):
        # arrancar y mostrar la ventana hasta que se cierre  
        self.ventana.mainloop()
        


#Instanciar mi programa

programa = Programa()
programa.cargar()
programa.addTexto("Metodo cris")
programa.mostrar()

