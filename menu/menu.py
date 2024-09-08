from tickets.mostrar_tickets import mostrar_tickets
from tickets.ticket import cargar_ticket_manual
from validadores.validadores import obtener_opcion
from tickets.mostrar_tickets import modificar_matriz


def menu(matriz_empleados, columnas, ids):
    print("\n--- Menú Ticketrack ---")
    print("1. Añadir Ticket")
    print("2. Actualizar Ticket")
    print("3. Generar Reporte")
    print("4. Mostrar Tickets")
    print("5. Salir")

    opcion = obtener_opcion()
    while opcion != 5:
        if opcion == 1:
            cargar_ticket_manual(matriz_empleados, ids)

        elif opcion == 2:
            modificar_matriz(matriz_empleados, ids)

        elif opcion == 3:
            print("Proximamente - Generar Reportes")

        elif opcion == 4:
            mostrar_tickets(matriz_empleados, columnas, ids)

        else:
            print("opcion no validad")
        opcion = obtener_opcion()


# Falta agregar submenus de diferentes opciones, como por ej, dentro de la generacion de reportes, la posibilidad de
# generar diferentes tipos de reportes, ya sea por empleado, en total por empleado, trimestral, un empleado en particular
# Ademas de el submenu de poder modificar o eliminar tickets de cada empleado en la 2 opcion
