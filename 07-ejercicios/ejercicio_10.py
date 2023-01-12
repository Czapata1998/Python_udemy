"""""
El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla cuantos han aprobado 
"""""

contador = 1

aprobados = 0

suspendidos = 0

numero_alumnos = int(input("cuantos alumnos tienes?"))

while contador <= numero_alumnos:
    nota = float(input(f"¿Que nota le asignamos al alumno {contador} ? :"))

    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1

    contador += 1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {suspendidos}")
