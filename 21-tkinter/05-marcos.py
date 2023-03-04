from tkinter import *

ventana= Tk()

ventana.title("Mater en python")
ventana.geometry("700x700")


marco_padre = Frame(ventana, width=250, height=250)

marco_padre.pack(side=BOTTOM, anchor=S ,fill=X, expand=YES) #RIGHT DERECHA


marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd=8,
    relief= "solid" #Dar estilos al borde de la ventana, RAISED            
)
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

Label(marco, text="Primer marco").pack(side=LEFT, anchor=SW)


marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="green",
    bd=8,
    relief= "solid" #Dar estilos al borde de la ventana, RAISED
             
)
marco.pack(side=RIGHT, anchor=SE)

marco_padre = Frame(ventana, width=250, height=250)

marco_padre.pack(side=TOP, anchor=N ,fill=X, expand=YES) #RIGHT DERECHA

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="pink",
    bd=8,
    relief= "solid" #Dar estilos al borde de la ventana, RAISED
             
)
marco.pack(side=LEFT )

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="orange",
    bd=8,
    relief= "solid" #Dar estilos al borde de la ventana, RAISED
             
)
marco.pack(side=RIGHT )


ventana.mainloop()