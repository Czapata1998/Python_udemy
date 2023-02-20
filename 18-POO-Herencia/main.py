import clases

persona = clases.Persona()

persona.setnombre("Cristhian Julian")
persona.setapellidos("Zapata Ladino")
persona.setaltura("1.70")
persona.setedad("24 years")

print(f"La persona es: {persona.getnombre()} {persona.getapellidos()}")

print(persona.dormir())

print("------------------------")

informatico = clases.informatico()

informatico.setnombre("Juli")

informatico.setapellidos("Ladino")


print(f"El informatico es {informatico.getnombre()} {informatico.getapellidos()}")

print(informatico.getlenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("------------------------")


tecnico = clases.TecnicoRedes()

tecnico.setnombre("Rubio")

print(tecnico.auditarredes, tecnico.getlenguajes(), tecnico.getnombre())





