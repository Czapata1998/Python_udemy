from tkinter import *

ventana = Tk()

#ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido al programa")
texto.config(
            fg="white",
            bg="black",
            padx=20,
            pady=20,
            font=("Consolas", 30)
)

texto.pack(side=TOP ) #LEFT RIGHT BOTTON



texto = Label(ventana, text="prueba") #Nombre especifico de las variables para llamarlos en desorden
texto.config(
    justify=RIGHT,
    height=2,
    bg="blue",
    padx=10,
    pady=10,
    cursor="circle", #Forma un cursor sobre el texto colocar spider jsjsj
    font=("Consolas", 20)
    
)
texto.pack(side=TOP, fill=X, expand=YES) #PARA MOVER EL TEXTO, PERO SOLO FUNCIONA DENTRO DE PACK

texto = Label(ventana, text="El diablo es bien pendejo")
texto.config(
    justify=RIGHT,
    height=2,
    bg="orange",
    padx=20,
    pady=20,
    cursor="circle" #Forma un cursor sobre el texto colocar spider jsjsj
    
)
texto.pack(side=LEFT, fill=X, expand=YES) #PARA MOVER EL TEXTO, PERO SOLO FUNCIONA DENTRO DE PACK

texto = Label(ventana, text="El diablo es bien pendejo 2")
texto.config(
    justify=RIGHT,
    height=2,
    bg="green",
    padx=20,
    pady=20,
    cursor="circle" #Forma un cursor sobre el texto colocar spider jsjsj
    
)
texto.pack(side=LEFT, fill=X, expand=YES) #PARA MOVER EL TEXTO, PERO SOLO FUNCIONA DENTRO DE PACK


texto = Label(ventana, text="El diablo es bien pendejo 3")
texto.config(
    justify=RIGHT,
    height=2,
    bg="red",
    padx=20,
    pady=20,
    cursor="circle" #Forma un cursor sobre el texto colocar spider jsjsj
    
)
texto.pack(side=LEFT, fill=X, expand=YES) #PARA MOVER EL TEXTO, PERO SOLO FUNCIONA DENTRO DE PACK


ventana.mainloop()