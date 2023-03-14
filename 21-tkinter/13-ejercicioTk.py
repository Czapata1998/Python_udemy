"""
Crear un programa que tenga:
- Ventana (Realizado)
- Tamaño fijo (Realizado)
- No redimensionable (Realizado)
- Un menú -Inicio, añadir, informacion, salir  (Realizado)
- Diferentes pantallas (Realizado)
- Formulario de añadir productos (Realizado)
- Guardar datos temporalmente (Realizado)
- Mostrar datos listados en la pantalla principal
- Opcion de salir 
"""

from tkinter import *

#Configuracion de la ventana
ventana = Tk()
ventana.geometry("400x400")
ventana.title("Ejercicio Cristhian Zapata Tk")
ventana.resizable(0,0)

#PANTALLAS 
def home():
    #Montando la pantalla
    home_label.config(
        fg= "white",
        bg= "black",
        font=("Arial", 30),
        padx=160,
        pady=20
    )
    home_label.grid(row=0, column=0)
    products_box.grid(row=1)
    
    #LISTAR LOS PRODUCTOS
    for product in products:
        if len(product) == 3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="------------").grid()
            
    
    
    #Ocultar otras pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    

    return True

def add():
    #ENCABEZADO
    add_label.config(
        fg= "white",
        bg= "black",
        font=("Arial", 30),
        padx=90,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)
    
    #CAMPOS DEL FORMULARIO (NOMBRE)
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
    
    #CAMPOS DEL FORMULARIO (PRECIO)
    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    
    #CAMPOS DEL FORMULARIO (DESCRIPCION)
    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )
    
    #SEPARADOR DE BOTON, UBICAION DE FILA
    add_separator.grid(row=4)
    
    
    boton.grid(row=5, column=1, sticky=NW)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white", 
    )
    
    #Ocultar otras pantallas
    info_label.grid_remove()
    data_label.grid_remove()
    home_label.grid_remove()
    products_box.grid_remove()
    
    
    return True

def info():
    info_label.config(
        fg= "white",
        bg= "black",
        font=("Arial", 30),
        padx=100,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)
    
    #Ocultar otras pantallas
    add_label.grid_remove()
    home_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()
    
    return True 

#funcion para agregar productos
def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)
    
    home()

# VARIABLES IMPORTANTES 
products = []
name_data = StringVar()
price_data = StringVar()


#Definir campos de pantalla (INICIO)
home_label = Label(ventana, text="Inicio")
products_box = Frame(ventana, width=250)

#Definir campos de pantalla (AÑADIR PRODUCTOS)
add_label = Label(ventana, text="Añadir producto")

#######################################################


#Crear campos del formulario (NOMBRE)
add_frame = Frame(ventana) #Ocultar campos del formulario de las otras ventanas

add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame, textvariable= name_data)

#Crear campos del formulario (PRECIO)
add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame, textvariable= price_data)

#Crear campos del formulario (DESCRIPCION)
add_description_label = Label(add_frame, text="Descripción: ")
add_description_entry = Text(add_frame, )

#separar el boton del campo de texto
add_separator = Label(add_frame)

boton = Button(add_frame, text="Guardar", command=add_product)


######################################################

#Definir campos de pantalla (INFORMACION)
info_label = Label(ventana, text="Informacion")
data_label = Label(ventana, text="Creado por Cristhian Zapata - 2023")


#Cargar la pantalla de inicio
home()


#MENÚ SUPERIOR
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

#Cargar el menú
ventana.config(menu=menu_superior)


#Ejecuta o carga la ventana 
ventana.mainloop()