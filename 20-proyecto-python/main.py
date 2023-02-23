"""
Proyecto Python y Msql
-Abrir Asistente
-Login o registro
-Si elegimos registro, creara un usuario en la base de datos 
-Crear nota, mostrar nota, borrarlas.
"""
from usuarios import acciones

print("""
Acciones disponibles:
    -Registro
    -Login
""")


realiza = acciones.Acciones()
accion = input("Que quieres hacer?: ")

if accion == "Registro" or accion== "registro":
    realiza.registro()
elif accion == "Login" or accion == "login":
    realiza.login()
    
    