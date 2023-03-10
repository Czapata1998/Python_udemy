"""
CALCULADORA:
-Dos campos de texto
-4 botones para las operaciones
-Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Ejercicio completo de Tkinter / Cristhian Zapata")
ventana.geometry("400x400")
ventana.config(bd=25)


def convertirFloat(numero):
    try:
        result = float(numero) 
    except:
        result = 0
        messagebox.showerror("Error", "Introduzca valores numericos")
    return result


def sumar():
    resultado.set(convertirFloat(numero1.get()) + convertirFloat(numero2.get()))
    #messagebox.showerror("Error", "Introduce datos numericos") 
    mostarResultado()
    
def restar():
    resultado.set(convertirFloat(numero1.get()) - convertirFloat(numero2.get()))
    #messagebox.showerror("Error", "Introduce datos numericos")
    mostarResultado() 
    
    
def multiplicar():
    resultado.set(convertirFloat(numero1.get()) * convertirFloat(numero2.get()))
    #messagebox.showerror("Error", "Introduce datos numericos")
    mostarResultado()
    
def dividir():
    resultado.set(convertirFloat(numero1.get()) / convertirFloat(numero2.get()))
    #messagebox.showerror("Error", "Introduce datos numericos")  
    mostarResultado()
    
def mostarResultado():
    messagebox.showinfo("resultado", f"el resultado de la operacion es {resultado.get()}")
    numero1.set("")
    numero2.set("")
   
   
   
numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar() 

marco = Frame(ventana, width=340, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
    
    
    
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer numero").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo numero").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()
#Crear botones
Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()
