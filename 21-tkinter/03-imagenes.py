from tkinter import *
from PIL import Image, ImageTk #https://bobbyhadz.com/blog/python-no-module-named-pil

ventana = Tk()
ventana.geometry("2000x2000")

Label(ventana, text="Hola, soy crissssss").pack(anchor=CENTER)

imagen = Image.open('./21-tkinter/imagenes/kanye.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack(anchor=E)
ventana.mainloop()