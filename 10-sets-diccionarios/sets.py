"""
SET es un tipo de dato, para tener una coleccion de valor
pero no tine ni indice ni orden
"""

persona = {
    "Kevin",
    "Diego",
    "Vale",
    "Cris"
}

persona.add("Juank")
persona.remove("Cris")

print(persona)
print(type(persona))