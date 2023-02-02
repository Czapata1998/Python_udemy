"""
Crear una lista con el contenido de esta tabla:
Accion     Aventura               Deportes
GTA        ASSINS CRED            FIFA
COD        CRASH                  PRO 21
PUG        PRINCIPE DE PERSIA     MOTOGP

Mostrar esta info ordenada
"""

tabla = [
    {
        "categoria":  "ACCION",
        "juegos": ["GTA", "COD", "PUG"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSINS CRED", "CRASH", "PRINCIPE DE PERSIA"]
    },
     {
        "categoria": "DEPORTES",
        "juegos": ["FIFA", "PRO 21", "MOTOGP"]
    }
]

for categoria in tabla:
    print(f"--------{categoria['categoria']}---------------")
    for juego in categoria['juegos']:
        print(juego)