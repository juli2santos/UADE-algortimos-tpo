from tickets.ticket import validar_empleados
from tickets.ticket import generar_ids
from menu.menu import menu
from auth import registrar_usuario, verificar_credenciales

def main():

    usuarios = [
        ["usuario1", "password1"],
        ["usuario2", "password2"],
        ["usuario3", "password3"]
    ]

    # Ingreso de usuario y contraseña
    sesion_actual = verificar_credenciales(usuarios, "usuario1", "password1")
    if not sesion_actual:
        print("Inicio de sesión fallido.")
        return
    
    # Registro de usuario
    """ registro_exitoso = registrar_usuario(usuarios, "usuario4", "password4") """


    total_empleados = validar_empleados()
    #print("total empleados",len(lista_empleados))
    filas = total_empleados #Cantidad de empleados 
    columnas = 12 # 12 una por cada mes

    matriz_empleados = [] #lista para inicializar la matriz
    ids= [] #lista de ids para empleados

    for f in range(filas):
        matriz_empleados.append([0]*columnas) #creacion de matriz de forma dinamica 

    if not ids:
            generar_ids(len(matriz_empleados), ids) #generacion de ids automaticamente post ingresar numero de empleados
    
    """Menú principal para la gestión de tickets."""

    menu(matriz_empleados, columnas, ids)
    


if __name__ == '__main__':
    main()