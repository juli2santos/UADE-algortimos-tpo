from tickets.ticket import validar_empleados
from tickets.mostrar_tickets import mostrar_tickets
from tickets.ticket import generar_ids
def menu(matriz_empleados, columnas, ids):
        print("\n--- Menú Ticketrack ---")
        print("1. Añadir Ticket")
        print("2. Actualizar Ticket")
        print("3. Generar Reporte")
        print("4. Mostrar Tickets")
        print("5. Salir")    
        opcion = int(input("Elige una opción: "))
        while opcion != 5:
            if opcion == 1: 
                if not ids:
                    generar_ids(len(matriz_empleados), ids)
                opcion = int(input("Elige una opción: "))
            elif opcion == 2:
                print('proximamente2')
                opcion = int(input("Elige una opción: "))
            elif opcion == 3:
                print('proximamente3')
                opcion = int(input("Elige una opción: "))
            elif opcion == 4:
                mostrar_tickets(matriz_empleados, columnas, ids)
                opcion = int(input("Elige una opción: "))
            else:
                opcion = input("Elige una opción: ")

def main():
    total_empleados = validar_empleados()

    lista_empleados = [0] * total_empleados

    print("total empleados",len(lista_empleados))

    filas = total_empleados
    columnas = 12 # 12 una por cada mes

    matriz_empleados = []
    ids= []
    for f in range(filas):
        matriz_empleados.append([0]*columnas)


    """Menú principal para la gestión de tickets."""
    menu(matriz_empleados, columnas, ids)
    


if __name__ == '__main__':
    main()