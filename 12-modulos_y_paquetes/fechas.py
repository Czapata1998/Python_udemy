"""
Modulo de fechas python
"""

import datetime

print(datetime.date.today()) #fecha actual


fecha_completa = datetime.datetime.now() #fecha y hora exacta en la que estamos

print(fecha_completa)

print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)


fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S ") #Formatear una fecha o darle fotmato

print(f"Mi fecha personalizada es {fecha_personalizada}")


print(datetime.datetime.now().timestamp()) #Fechas en otros formatos