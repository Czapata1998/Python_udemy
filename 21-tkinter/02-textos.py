from tkinter import *

ventana = Tk()

ventana.geometry("700x500")

texto = Label(ventana, text="Haciendo pruebas")
texto.config(
            fg="white",
            bg="black",
            padx=20,
            pady=20,
            font=("Consolas", 30)
)

texto.pack()

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

texto = Label(ventana, text=pruebas(nombre="Cristhian", apellidos="Zapata", pais="Colombia")) #Nombre especifico de las variables para llamarlos en desorden
texto.config(
    justify=RIGHT,
    width=200,
    height=2,
    bg="blue",
    padx=20,
    pady=20,
    cursor="circle", #Forma un cursor sobre el texto colocar spider jsjsj
    font=("Consolas", 30)
    
)
texto.pack(anchor=SE) #PARA MOVER EL TEXTO, PERO SOLO FUNCIONA DENTRO DE PACK

texto = Label(ventana, text="El diablo es bien pendejo")
texto.config(
    justify=RIGHT,
    height=2,
    bg="orange",
    padx=20,
    pady=20,
    cursor="circle" #Forma un cursor sobre el texto colocar spider jsjsj
    
)
texto.pack(anchor=E) #PARA MOVER EL TEXTO, PERO SOLO FUNCIONA DENTRO DE PACK


ventana.mainloop()