from tickets.mostrar_tickets import mostrar_tickets, modificar_matriz
from tickets.ticket import cargar_ticket_manual
from validadores.validadores import obtener_opcion
from reportes.reportes import reporte_anual, reporte_anual_individual, reporte_mensual

def print_submenu():
    print("\n--- Submenú Reportes ---")
    print("1. Reporte anual de todos los empleados")
    print("2. Reporte Anual Individual")
    print("3. Reporte Mensual")
    print("4. Reporte de Desempeño de Empleados")
    print("5. Salir")

def sub_menu_reportes(matriz_empleados, ids):
    print_submenu()

    opcion = obtener_opcion()
    while opcion != 5:
        if opcion == 1:
            reporte_anual(matriz_empleados)
            print_submenu()

        elif opcion == 2:
            reporte_anual_individual(matriz_empleados, ids)
            print_submenu()
        elif opcion == 3:
            reporte_mensual(matriz_empleados)
            print_submenu()
        else:
            print("opcion no valida")
        opcion = obtener_opcion()

def print_menu():
    print("\n--- Menú Ticketrack ---")
    print("1. Añadir Tickets")
    print("2. Modificar Tickets ")
    print("3. Generar Reporte")
    print("4. Mostrar Tickets")
    print("5. Salir")


def menu(matriz_empleados, columnas, ids):
    print_menu()

    opcion = obtener_opcion()
    while opcion != 5:
        if opcion == 1:
            modificar_matriz(matriz_empleados, ids)
            print_menu()

        elif opcion == 2:
            cargar_ticket_manual(matriz_empleados, ids)
            print_menu()

        elif opcion == 3:
            sub_menu_reportes(matriz_empleados, ids)
            print_menu()
        elif opcion == 4:
            mostrar_tickets(matriz_empleados, columnas, ids)
            print_menu()

        else:
            print("Opcion no valida")
        opcion = obtener_opcion()
    print('Hasta luego.')

# Falta agregar submenus de diferentes opciones, como por ej, dentro de la generacion de reportes, la posibilidad de
# generar diferentes tipos de reportes, ya sea por empleado, en total por empleado, trimestral, un empleado en particular
# Ademas de el submenu de poder modificar o eliminar tickets de cada empleado en la 2 opcion
