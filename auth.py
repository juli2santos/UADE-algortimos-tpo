usuarios = ["usuario1", "usuario2", "usuario3"]
contrasenas = ["password1", "password2", "password3"]

def menu_login():
    print("1. Iniciar sesión.")
    print("2. Registrarse.")
    print("3. Salir.")
    opcion = int(input("Ingrese el numero de la opcion: "))
    return opcion

def registrar_usuario(usuarios, contrasenas, username, password):
    if username in usuarios:
        print("El nombre de usuario ya existe.")
        return False
    usuarios.append(username)
    contrasenas.append(password)
    print("Usuario registrado exitosamente.")
    return True

def verificar_credenciales(usuarios, contrasenas, username, password):
    for i in range(len(usuarios)):
        if usuarios[i] == username and contrasenas[i] == password:
            print("Inicio de sesión exitoso.")
            return True
    print("Nombre de usuario o contraseña incorrectos.")
    return False