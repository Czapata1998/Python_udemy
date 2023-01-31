"""
Crear un programa que compruebe si una variable está vacia y si esta vacia, rellenarla con texto
en minusculas y mostrarlo en mayusculas
"""

# Mi solucion

''' texto = "klk "

if texto == "":
    print("La variable está vacia")
elif texto != "":
    texto += "joder esto si es programar"
    


print(texto.upper()) '''


# Solucion udemy

texto = " texto"

if len(texto.strip()) <= 0:
    texto = "Hola soy un texto en minuscula"
    print(texto.upper())
else:
    print(f"el texto es{texto}")
    
    
    #Comentario de prueba
