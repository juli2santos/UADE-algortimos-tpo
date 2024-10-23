from menu.menu import menu
from auth import registrar_usuario, verificar_credenciales, menu_login
from validadores.validadores import validar_empleados 
from tickets.ticket import generar_ids


def main():
    # Listas paralelas para usuario y contraseñas
    usuarios = ["usuario1", "usuario2"]
    contrasenas = ["password1", "password2"]

    continuar = True

    while continuar:
        opcion = menu_login()
        
        if opcion == 1:
            username = input("Ingrese nombre de usuario: ")
            password = input("Ingrese contraseña: ")
            if verificar_credenciales(usuarios, contrasenas, username, password):
                print("Acceso concedido.")
                total_empleados = validar_empleados()
                filas = total_empleados  # Cantidad de empleados
                columnas = 12  # 12 una por cada mes

                matriz_empleados = []  # lista para inicializar la matriz
                ids = []  # lista de ids para empleados

                for f in range(filas):
                    matriz_empleados.append([0] * columnas)  # creacion de matriz de forma dinamica

                if not ids:  # generacion de ids automaticamente post ingresar numero de empleados
                    generar_ids(len(matriz_empleados), ids)
                tickets = []
                """Menú principal para la gestión de tickets."""
                menu(matriz_empleados, columnas, ids, tickets)
            else:
                print("Acceso denegado.")
        elif opcion == 2:
            username = input("Ingrese nombre de usuario: ")
            password = input("Ingrese contraseña: ")
            registrar_usuario(usuarios, contrasenas, username, password)
        elif opcion == 3:
            print("Saliendo del sistema.")
            continuar = False
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()