from tkinter import *

ventana = Tk()
ventana.geometry("700x700")

ventana.title("Menú")

mi_menu = Menu(ventana )
ventana.config(menu=mi_menu)

#archivo
archivo = Menu(mi_menu, tearoff=0)
archivo.add_command(label="Nuevo archivo")
archivo.add_command(label="Nueva ventana")
archivo.add_separator()

archivo.add_command(label="Abrir archivo")
archivo.add_command(label="Abrir carpeta")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.quit)

#Editar
editar = Menu(mi_menu, tearoff=0)
editar.add_command(label="Editar archivo")
editar.add_command(label="Guardar nuevo")
editar.add_command(label="Exportar")

editar.add_separator()
editar.add_command(label="Salir", command=ventana.quit)


#Seleccionar
seleccionar = Menu(mi_menu, tearoff=0)
seleccionar.add_command(label="Editar archivo")
seleccionar.add_command(label="Guardar nuevo")
seleccionar.add_command(label="Exportar")

seleccionar.add_separator()
seleccionar.add_command(label="Salir", command=ventana.quit)

#Opciones de menú
mi_menu.add_cascade(label= "Archivo", menu=archivo)
mi_menu.add_cascade(label= "Editar", menu=editar)
mi_menu.add_cascade(label= "Seleccionar", menu=seleccionar)

ventana.mainloop()