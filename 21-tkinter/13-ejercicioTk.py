"""
Crear un programa que tenga:
- Ventana (Realizado)
- Tamaño fijo (Realizado)
- No redimensionable (Realizado)
- Un menú -Inicio, añadir, informacion, salir  (Realizado)
- Diferentes pantallas (Realizado)
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

#DIFERENTES PANTALLAS

def home():
    #Montar pantalla
    home_label.config(
        fg= "white",
        bg= "black",
        font=("Arial", 30),
        padx=210,
        pady=20
    )
    home_label.grid(row=0, column=0)
    
    
    #Ocultar otras pantalla
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    
    return True


def add():
    #Encabezado
    add_label.config(
        fg= "white",
        bg= "black",
        font=("Arial", 30),
        padx=110,
        pady=20
    )
    add_label.grid(row=0, column=0)
    
    #Campos del formulario
    add_name_label.grid(row=1, column=0, padx=5 , pady=5)
    
    
    #Ocultar otras pantalla
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    
    return True


def info():
    info_label.config(
        fg= "white",
        bg= "black",
        font=("Arial", 30),
        padx=170,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)
    
    
    home_label.grid_remove()
    add_label.grid_remove()
    #data_label.grid_remove()
    return True
    

#Variables importantes
name_data = StringVar()
price_data = StringVar()
descripcion_data = StringVar()

#Definir campos de pantallas (INICIO)
home_label = Label(ventana, text="Inicio")


#Definir campos de pantallas (PRODUCTO - ADD)
add_label = Label(ventana, text="Añadir producto")


#CAMPOS DEL FORMULARIO
#nombre del producto
add_name_label = Label(ventana, text="Nombre del producto")
add_name_entry = Entry(ventana, textvariable=name_data)


#precio del producto
add_price_label = Label(ventana, text="Precio del producto")
add_price_entry = Entry(ventana, textvariable=price_data)


#descripcion del producto
add_descripcion_label = Label(ventana, text="Descripcion del producto")
add_descripcion_entry = Entry(ventana, textvariable=descripcion_data)


#Definir campos de pantallas (INFORMACION)
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por Cristhian Zapata - 2022")


#CARGAR LA PANTALLA DE INICIO 
home()

# Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Informacion", command= info)
menu_superior.add_command(label="Salir", command=ventana.quit)

#Cargar menú
ventana.config(menu=menu_superior)


#Cargar ventana
ventana.mainloop()