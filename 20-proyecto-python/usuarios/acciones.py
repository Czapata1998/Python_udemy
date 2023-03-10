import usuarios.usuario as modelo
import notas.acciones 

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
            print(f"\nperfecto {registro[1].nombre} te has registrado con el correo {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")
    
    def login(self):
        print("\nOk. identificate en el sistema")
        
        try:
            email = input("Digite por favor su correo electronico: ")
            password = input("Ingresa tu contrasena: ")
            
            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()
            
            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto intentalo mas tarde")
            
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles: 
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - borrar notas (borrar)
        - Salir (salir)
        """)
        
        accion = input("Que quieres hacer?: ")
        hazEl= notas.acciones.Acciones()
        
        
        
        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
            
            
        elif accion == "borrar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
            
        
        elif accion == "salir":
            print(f" {usuario[1]}, Hasta pronto")
            exit()
               
            
       
        
