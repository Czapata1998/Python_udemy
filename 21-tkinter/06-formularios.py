from tkinter import *

ventana = Tk()
ventana.geometry("700x500")
ventana.title( "Formularios de Cristhian Zapata") 


encabezado = Label(ventana, text="Formularios con Tkinter - Cristhian Zapata")
encabezado.config(
    fg= "black",
    bg= "blue",
    font =("Open Sans", 18),
    padx=10,
    pady=10,
    
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=E)

#Label para el campo (NOMBRE)
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#Campo de texto (NOMBRE)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")


#Label para el campo (APELLIDOS)
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#Campo de texto (APELLIDOS)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")


ventana.mainloop()