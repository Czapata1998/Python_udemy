"""
Modulo de paquetes
"""

print("Probando paquetes: ")

from mipaquete import pruebas, herramientas # Traer modulos juntos
from mipaquete import pruebas

from mipaquete import herramientas

#Trae las funciones de los paquetes creados
pruebas.probar()

herramientas.nombrecompleto("Cristhian", "Zapata")