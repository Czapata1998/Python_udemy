"""
Diccionario: Tipo de dato que almacena datos.
En formato clave > Valor 
Es parecido a un array asociativo a un objeto json. 
"""

persona = {
    "nombre" : "Cristhian", # Primero se inserta la clave, luego el valor
    "Carrera" : "Ingenieria de sistemas",
    "direccion" : "Mirador de llano grande"
}

print(type(persona))
print(persona["Carrera"]) #Para traer el valor de la clave



#Lista con diccionarios 

Contactos = [
    {
       'nombre' : 'cris', 
       'Carrera' : 'Ingenieria de sistemas',
       'direccion' : 'Mirador de llano grande'
    },
    {
       'nombre' : 'Santi', 
       'Carrera' : 'Ingenieria de software',
       'direccion' : 'Mirador de llano grande 2' 
    },
    {
       'nombre' : 'Kevin', 
       'Carrera' : 'Ingenieria de software II',
       'direccion' : 'Mirador de llano grande 3' 
    }
]

Contactos[0]['nombre'] = "Cristhian Zapata"
print(Contactos[0]['nombre']) # LLamar una lista con el valor que se desee de ella

print("\nListado de contactos")

for contacto in Contactos:
    print(f"nombre del contacto: {contacto['nombre']}")
    print(f"carrera del contacto: {contacto['Carrera']}")
    print("----------------------------------")