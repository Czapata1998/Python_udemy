from tkinter import *

ventana = Tk()
ventana.geometry("700x500")
ventana.title( "Formularios de Cristhian Zapata") 


encabezado = Label(ventana, text="Formularios con Tkinter - Cristhian Zapata")
encabezado.config(
    fg= "black",
    bg= "blue",
    font =("Open Sans", 18),
    padx=8,
    pady=10,
    
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=N)

#Label para el campo (NOMBRE)
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#Campo de texto (NOMBRE)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")


#Label para el campo (APELLIDOS)
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#Campo de texto (APELLIDOS)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")


#Label para el campo (DESCRIPCION)
label = Label(ventana, text="Descripcion")
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)


#Campo de texto grande
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(
    width=30, 
    height=5,
    font=("Arial", 12),
    padx= 15,
    pady= 15
)

# Botones
Label(ventana).grid(row=4, column=1)

boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(padx=10, pady=10, bg="green", fg="white")





ventana.mainloop()