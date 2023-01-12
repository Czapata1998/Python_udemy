"""""

Mostrar todas las tablas de multiplicar del 1 al 10 mostrando el titulo de la tabla y luego las multiuplicaciones 
"""""

for cabecera in range (1, 11):
    print("###############")
    print(f"----Tabla del: {cabecera}----")
    print("###############")
    
    for numero in range(1, 11):
        print(f"{cabecera} x {numero} = {cabecera * numero}")
    
    print("\n")
    