from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showinfo("Alerta", "Hola Soy Cristhian Zapata") #showwarning = SACA UNA ALERTA DE PELIGRO, showerror= SACA UNA ALERTA DE ERROR


Button(ventana, text="Mostrar alerta!!!!!", command=sacarAlerta ).pack()



def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "Quieres continuar ejecutnado la app?") #showwarning = SACA UNA ALERTA DE PELIGRO, showerror= SACA UNA ALERTA DE ERROR
    if resultado != "si":
        MessageBox.showinfo("Salir", f"Adios {nombre}")
        ventana.destroy()  #Me permite cerrar la ventana
        

Button(ventana, text="Salir", command=lambda : salir("Cristhian") ).pack() #LAMBDA EJECUTA LA FUNCION DESPUES DE DAR CLIC EN EL BOTON

ventana.mainloop()

