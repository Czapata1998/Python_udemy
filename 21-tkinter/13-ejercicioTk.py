"""
Crear un programa que tenga:
- Ventana (Realizado)
- Tamaño fijo (Realizado)
- No redimensionable (Realizado)
- Un menú
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente 
- Mostrar datos listados en la pantalla principal
- Opcion de salir 
"""

from tkinter import *

ventana = Tk()
ventana.title("Ejercicio final - tkinter")
ventana.geometry("500x500")
ventana.resizable(0, 0)


ventana.mainloop()