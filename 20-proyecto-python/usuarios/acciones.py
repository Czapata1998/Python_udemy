import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("\nOk, vamos a registrarte en el sistema...")

        nombre = input("Por favor digita tu nombre: ")
        apellidos = input("Por favor digita tus apellidos: ")
        email = input("Digite por favor su correo electronico: ")
        password = input("Ingresa tu contrasena: ")
        
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        
        if registro [0] >= 1:
            print(f"perfecto {registro[1].nombre} te has registrado con el correo {registro[1].email}")
        else:
            print("No te has registrado correctamente")
    
    def login(self):
        print("\nOk. identificate en el sistema")
        email = input("Digite por favor su correo electronico: ")
        password = input("Ingresa tu contrasena: ")
