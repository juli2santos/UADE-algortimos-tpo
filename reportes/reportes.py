from validadores.validadores import opcion_reutilizable, opcion_reporte
from archivoSalida.archivos import exportar_tickets_csv, exportar_tickets_empleado_csv, exportar_tickets_mes_csv


#SEGUIR AGREGANDO TRY-EXCEPT PARA CASOS EN LOS QUE NO HAYA CARGA INICIAL EN LAS SUMAS POR EJ DE REPORTE ANUAL INDIVIDUAL, SUM(LEN(MATRIZ_EMPLEADOS))


def sumaEmpleadosRecursivo(matriz_empleados, i=0):
    try:
        if i == len(matriz_empleados):
            return 0
        else:
            total_tickets = sum(len(matriz_empleados[i][j]) for j in range(12))
            return total_tickets + sumaEmpleadosRecursivo(matriz_empleados, i+1)
    except IndexError:
        print('Error - Matriz Vacia')
        return 0 
    except TypeError:
        print('Error - Matriz Vacia')
        return 0 
    except Exception:
        print('Error Inesperado')
        return 0 


def mostrar_reporte_detallado(matriz_empleados, ids):
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

    for i, id_empleado in enumerate(ids):
        print(f"\n--- Reporte Detallado para Empleado {id_empleado} ---")
        
        for j, mes in enumerate(meses):
            tickets_mes = matriz_empleados[i][j]
            if tickets_mes:
                print(f"\nMes: {mes}")
                
                for ticket_id, ticket_info in tickets_mes.items():
                    print(f"  Ticket ID: {ticket_id}")
                    print(f"    Descripción: {ticket_info.get('descripcion', '')}")
                    print(f"    Fecha: {ticket_info.get('fecha', '')}")
                    print(f"    Prioridad: {ticket_info.get('prioridad', '')}")
            else:
                print(f"\nMes: {mes} - No hay tickets registrados.")

    print("\n--- Fin del Reporte ---")

def reporte_anual(matriz_empleados, ids):
    total = sumaEmpleadosRecursivo(matriz_empleados)
    print(f'\n --- El total anual de tickets de todos los empleados es de {total}. ---')
    print('\n Seleccione el tipo de salida que desea para recibir los detalles de los tickets: ')
    print('1. Mostrar en Consola')
    print('2. Exportar a CSV')
    try:
        opcion = opcion_reporte()
        if opcion == 1:
            mostrar_reporte_detallado(matriz_empleados, ids)
        elif opcion == 2:
            archivo_salida = input("Ingrese el nombre del archivo CSV (por defecto: 'tickets.csv'): ") or "tickets.csv"
            exportar_tickets_csv(matriz_empleados, ids, archivo_salida)
    except ValueError:
        print('')

def reporte_anual_individual(matriz_empleados, ids):
    print('1. Mostrar reporte por consola')
    print('2. Exportar reporte detallado a un archivo CSV')
    opcion = opcion_reporte()
    
    while True:
        try:
            if opcion == 1:
                print(f'\n --- IDs de los empleados: {ids}. ---')
                id_empleado = int(input("Ingrese el ID del empleado del cual desea generar el reporte anual: "))

                while id_empleado not in ids:
                    id_empleado = int(input('Error - ID inexistente. Ingrese un ID valido: '))

                ind_empleado = ids.index(id_empleado)

                total_anual = sum(len(matriz_empleados[ind_empleado][j]) for j in range(12))

                print(f'\n --- El total anual de tickets del empleado {id_empleado} es de {total_anual}. ---')
                break

            elif opcion == 2:
                print(f'\n --- IDs de los empleados: {ids}. ---')
                id_empleado = int(input("Ingrese el ID del empleado: "))
                if id_empleado in ids:
                    archivo_salida = input("Ingrese el nombre del archivo CSV (por defecto: 'reporteEmpleado.csv'): ") or "reporteempleado.csv"
                    try:
                        exportar_tickets_empleado_csv(matriz_empleados, id_empleado, ids, archivo_salida)
                    except Exception:
                        print('Error - No se pudo generar el archivo CSV')
                else:
                    print(f"Error: No se encontró el empleado con ID {id_empleado}.")
                break

        except ValueError:
            print('Error - Por favor, ingrese un número válido.')


def reporte_mensual(matriz_empleados, ids): 
    print('\n-----------------------')
    print('1. Reporte Mensual de Todos los Empleados')
    print('2. Reporte Mensual Individual')
    print('3. Exportar Reporte Individual detallado a CSV')
    opcion = opcion_reutilizable()

    if opcion == 1:
        mes = int(input('Ingrese el mes (1-12) para el cual desea recibir el reporte de tickets: '))
        while mes < 1 or mes > 12:
            mes = int(input("Error - Mes inválido. Debe ingresar un valor entre 1 y 12: "))

        mes_ind = mes - 1
        total_mensual = 0

        for i in range(len(matriz_empleados)):
            total_mensual += len(matriz_empleados[i][mes_ind])
        print(f'\n --- El total de tickets mensual del mes {mes} es de {total_mensual}. ---')

    elif opcion == 2:
        while True:    
            try:
                print(f'\n --- IDs de empleados: {ids} ---')
                id_empleado = int(input('Ingrese el ID del empleado que desea solicitar su reporte mensual: '))
                            
                while id_empleado not in ids:
                    id_empleado = int(input('Error - ID inexistente. Ingrese un ID valido: '))

                ind_empleado = ids.index(id_empleado)
            
                while True:
                    try:
                        mes = int(input('Ingrese el mes (1-12) para el cual desea recibir el reporte de tickets: '))
                        while mes < 1 or mes > 12:
                            mes = int(input("Error - Mes inválido. Debe ingresar un valor entre 1 y 12: "))        
                            
                        mes_ind = mes - 1
                        total_mensual = 0
                                
                        total_mensual += len(matriz_empleados[ind_empleado][mes_ind])
                        print(f'\n --- El total de tickets mensual del mes {mes}, del empleado {id_empleado} es de {total_mensual}. ---')
                        break

                    except ValueError:
                        print("Error - Por favor ingrese un número válido para el mes.")
                break
            except ValueError:
                print("Error - Por favor ingrese un número válido para el ID del empleado.")  


    elif opcion == 3:
        try:  
            print(f'\n --- IDs de empleados: {ids} ---')  
            id_empleado = int(input('Ingrese el ID del empleado que desea solicitar su reporte mensual: '))
            while id_empleado not in ids:
                id_empleado = int(input('Error - ID inexistente. Ingrese un ID valido: '))

            try:
                mes = int(input('Ingrese el mes (1-12) para el cual desea recibir el reporte de tickets: '))
                while mes < 1 or mes > 12:
                    mes = int(input("Error - Mes inválido. Debe ingresar un valor entre 1 y 12: "))  

                archivo_salida = input("Ingrese el nombre del archivo CSV (por defecto: 'reporte.csv'): ") or "reporte.csv"
                exportar_tickets_mes_csv(matriz_empleados, mes, id_empleado, ids, archivo_salida)
                
            except ValueError:
                print("Error - Por favor ingrese un número válido para el mes.")
                
        except Exception:
            print('Error Inesperado')

def reporte_desemp_empleados(matriz_empleados, ids):
    print('1. Reporte del Mejor Desempeño de Tickets de Empleado')
    print('2. Reporte del Peor Desempeño de Tickets de Empleado')
    print('3. Reporte del Promedio de Tickets Total de Todos los Empleados')
    opcion = opcion_reutilizable()


    if opcion == 1:
        max_tickets = 0
        mj_desemp = []

        for i in range(len(matriz_empleados)):
            total_tickets = sum(len(matriz_empleados[i][j]) for j in range(12))
            if total_tickets > max_tickets:
                max_tickets = total_tickets
                mj_desemp = [ids[i]]
            elif total_tickets == max_tickets:
                mj_desemp.append(ids[i])
        print(f'\n --- El mejor desempeño de tickets tiene un total de {max_tickets} tickets. ---')
        print(f'\n --- ID(s) de los empleado(s) con el mejor desempeño: {mj_desemp}. ---')
    
    elif opcion == 2:
        min_tickets = float('inf')
        peor_desemp = []

        for i in range(len(matriz_empleados)):
            total_tickets = sum(len(matriz_empleados[i][j]) for j in range(12))
            if total_tickets < min_tickets:
                min_tickets = total_tickets
                peor_desemp = [ids[i]]
            elif total_tickets == min_tickets:
                peor_desemp.append(ids[i])
        print(f'\n --- El peor desempeño de tickets tiene un total de {min_tickets} tickets. ---')
        print(f'\n --- ID(s) de los empleado(s) con el peor desempeño: {peor_desemp}. ---')

    elif opcion == 3:
        total_tickets = sumaEmpleadosRecursivo(matriz_empleados)
        promedio_total = total_tickets / len(matriz_empleados) if len(matriz_empleados) > 0 else 0
        print(f'\n --- El promedio total de tickets es de: {promedio_total}. ---')
    
