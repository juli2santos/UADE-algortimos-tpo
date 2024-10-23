from validadores.validadores import opcion_mensual, opcion_desemp


def sumaEmpleadosRecursivo(matriz_empleados, i=0):
    if i == len(matriz_empleados):
        return 0
    else:
        return sum(matriz_empleados[i]) + sumaEmpleadosRecursivo(matriz_empleados, i+1)

def reporte_anual(matriz_empleados):
    total = sumaEmpleadosRecursivo(matriz_empleados)
    
    print(f'\n --- El total anual de tickets de todos los empleados es de {total}. ---')

def reporte_anual_individual(matriz_empleados, ids):
    print(f'\n --- IDs de los empleados: {ids}. ---')
    id_empleado = int(input("Ingrese el ID del empleado del cual desea generar el reporte anual: "))

    while id_empleado not in ids:
        id_empleado = int(input('Error - ID inexistente. Ingrese un ID valido: '))

    ind_empleado = ids.index(id_empleado)

    total_anual = sum(matriz_empleados[ind_empleado])

    print(f'\n --- El total anual de tickets del empleado {id_empleado} es de {total_anual}. ---')


def reporte_mensual(matriz_empleados, ids): 
    print('\n-----------------------')
    print('1. Reporte Mensual de Todos los Empleados')
    print('2. Reporte Mensual Individual')
    opcion = opcion_mensual()

    if opcion == 1:
        mes = int(input('Ingrese el mes (1-12) para el cual desea recibir el reporte de tickets: '))
        while mes < 1 or mes > 12:
            mes = int(input("Error - Mes inválido. Debe ingresar un valor entre 1 y 12: "))

        mes_ind = mes - 1
        total_mensual = 0

        for i in range(len(matriz_empleados)):
            total_mensual += matriz_empleados[i][mes_ind]
        print(f'\n --- El total de tickets mensual del mes {mes} es de {total_mensual}. ---')

    elif opcion == 2:
        print(f'\n --- IDs de empleados: {ids} ---')
        id_empleado = int(input('Ingrese el ID del empleado que desea solicitar su reporte mensual: '))
        
        while id_empleado not in ids:
            id_empleado = int(input('Error - ID inexistente. Ingrese un ID valido: '))

        ind_empleado = ids.index(id_empleado)

        mes = int(input('Ingrese el mes (1-12) para el cual desea recibir el reporte de tickets: '))
        while mes < 1 or mes > 12:
            mes = int(input("Error - Mes inválido. Debe ingresar un valor entre 1 y 12: "))        

        mes_ind = mes - 1
        total_mensual = 0
        
        total_mensual += matriz_empleados[ind_empleado][mes_ind]
        print(f'\n --- El total de tickets mensual del mes {mes}, del empleado {id_empleado} es de {total_mensual}. ---')



def reporte_desemp_empleados(matriz_empleados, ids):
    print('1. Reporte del Mejor Desempeño de Tickets de Empleado')
    print('2. Reporte del Peor Desempeño de Tickets de Empleado')
    print('3. Reporte del Promedio de Tickets Total de Todos los Empleados')
    opcion = opcion_desemp()

    if opcion == 1:
        max_tickets = 0
        mj_desemp = []

        for i in range(len(matriz_empleados)):
            total_tickets = sum(matriz_empleados[i])
            if total_tickets > max_tickets:
                max_tickets = total_tickets
                mj_desemp = [ids[i]]
            elif total_tickets == max_tickets:
                mj_desemp.append(ids[i])
        print(f'\n --- El mejor desempeño de tickets tiene un total de {max_tickets} tickets. ---')
        print(f'\n --- ID(s) de los empleado(s) con el mejor desempeño: {mj_desemp}. ---')
    
    elif opcion == 2:
        min_tickets = sum(matriz_empleados[0])
        peor_desemp = []

        for i in range(len(matriz_empleados)):
            total_tickets = sum(matriz_empleados[i])
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
        # total = 0
        # total_empleados = len(matriz_empleados)

        # for i in range(total_empleados):
        #     total += sum(matriz_empleados[i])
        
        # promedio_total = total / total_empleados if total_empleados > 0 else 0
        # print(f'\n --- El promedio total de tickets es de: {promedio_total}. ---')
    

