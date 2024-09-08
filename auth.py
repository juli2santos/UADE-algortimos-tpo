def registrar_usuario(matriz_usuarios, username, password):
    for usuario in matriz_usuarios:
        if usuario[0] == username:
            print("El nombre de usuario ya existe.")
            return False
    matriz_usuarios.append([username, password])
    print("Usuario registrado exitosamente.")
    return True

def verificar_credenciales(matriz_usuarios, username, password):
    for usuario in matriz_usuarios:
        if usuario[0] == username and usuario[1] == password:
            print("Inicio de sesión exitoso.")
            return True
    print("Nombre de usuario o contraseña incorrectos.")
    return False