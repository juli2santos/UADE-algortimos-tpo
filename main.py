from tickets.ticket import validar_empleados

def menu():
        print("\n--- Menú Ticketrack ---")
        print("1. Añadir Ticket")
        print("2. Actualizar Ticket")
        print("3. Generar Reporte")
        print("4. Mostrar Tickets")
        print("5. Salir")    
        opcion = int(input("Elige una opción: "))
        while opcion != 5:
            if opcion == 1: 
                print('proximamente1')
                opcion = int(input("Elige una opción: "))
            elif opcion == 2:
                print('proximamente2')
                opcion = int(input("Elige una opción: "))
            elif opcion == 3:
                print('proximamente3')
                opcion = int(input("Elige una opción: "))
            elif opcion == 4:
                print('proximamente4')
                opcion = int(input("Elige una opción: "))
            else:
                opcion = input("Elige una opción: ")

def main():
    total_empleados = validar_empleados()

    lista_empleados = [0] * total_empleados

    print("total",len(lista_empleados))

    filas = total_empleados
    columnas = 12 # 12 una por cada mes

    matriz_empleados = []

    for f in range(filas):
        matriz_empleados.append([0]*columnas)

    """Menú principal para la gestión de tickets."""
    menu()

        


if __name__ == '__main__':
    main()