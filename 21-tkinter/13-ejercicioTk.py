"""
Crear un programa que tenga:
- Ventana (Realizado)
- Tamaño fijo (Realizado)
- No redimensionable (Realizado)
- Un menú -Inicio, añadir, informacion, salir 
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente 
- Mostrar datos listados en la pantalla principal
- Opcion de salir 
"""

from tkinter import *

#Definir la ventana
ventana = Tk()
ventana.title("Ejercicio final - tkinter")
ventana.geometry("500x500")
ventana.resizable(0, 0)


# Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio")
menu_superior.add_command(label="Añadir")
menu_superior.add_command(label="Informacion")
menu_superior.add_command(label="salir")

ventana.config(menu=menu_superior)


#Cargar ventana
ventana.mainloop()