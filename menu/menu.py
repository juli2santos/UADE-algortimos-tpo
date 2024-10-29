from tickets.ticket import *
from validadores.validadores import obtener_opcion
from reportes.reportes import reporte_anual, reporte_anual_individual, reporte_mensual, reporte_desemp_empleados, mostrar_reporte_detallado

def print_submenu():
    print("\n --- Submenú Reportes ---")
    print("1. Reporte Anual de Todos los Empleados")
    print("2. Reporte Anual Individual")
    print("3. Reporte Mensual")
    print("4. Reporte de Desempeño de Empleados")
    print("5. Reporte detallado de tickets")
    print("6. Salir")

def sub_menu_reportes(matriz_empleados, ids):
    print_submenu()

    opcion = obtener_opcion()
    while opcion != 6:
        if opcion == 1:
            reporte_anual(matriz_empleados)
            print_submenu()

        elif opcion == 2:
            reporte_anual_individual(matriz_empleados, ids)
            print_submenu()
        elif opcion == 3:
            reporte_mensual(matriz_empleados, ids)
            print_submenu()
        elif opcion == 4:
            reporte_desemp_empleados(matriz_empleados, ids)
            print_submenu()
        elif opcion == 5:
<<<<<<< Updated upstream
            mostrar_reporte_detallado(matriz_empleados, ids)
=======
            exportar_tickets_csv(matriz_empleados, ids,archivo_salida='reporteDetallado.csv')
>>>>>>> Stashed changes
            print_submenu()
        else:
            print("opcion no valida")
        opcion = obtener_opcion()

def print_menu():
    print("\n --- Menú Ticketrack ---")
    print("1. Añadir Tickets.")
    print("2. Modificar Tickets.")
    print("3. Generar Reporte.")
    print("4. Mostrar Tickets.")
    print("5. Generar carga inicial")
    print("6. Salir.")

def menu(matriz_empleados, columnas, ids, tickets):
    print_menu()
    opcion = obtener_opcion()
    while opcion != 6:
        if opcion == 1:
            cargar_tickets(matriz_empleados, ids, tickets)
            print_menu()

        elif opcion == 2:
            actualizar_tickets(matriz_empleados, ids)
            print_menu()

        elif opcion == 3:
            sub_menu_reportes(matriz_empleados, ids)
            print_menu()
        elif opcion == 4:
            mostrar_tickets(matriz_empleados, columnas, ids)
            print_menu()
        if opcion == 5:
            generarCargaInicial(matriz_empleados, ids, tickets)
            print_menu()
        else:
            print("Opcion no valida")
        opcion = obtener_opcion()
    print(f'\n Hasta luego.')

