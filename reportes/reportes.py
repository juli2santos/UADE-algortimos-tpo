def reporte_anual(matriz_empleados):
    total_anual = 0

    for i in range (len(matriz_empleados)):
        total_anual += sum(matriz_empleados[i])

    print(f'El total anual de tickets de todos los empleados es de {total_anual}.')

def reporte_anual_individual(matriz_empleados, ids):
    print(f'IDs de los empleados: {ids}')
    id_empleado = int(input("Ingrese el ID del empleado del cual desea generar el reporte anual: "))

    if id_empleado not in ids:
        print('Error ID no encontrado. Por favor, ingrese un ID existente')

    ind_empleado = ids.index(id_empleado)

    total_anual = sum(matriz_empleados[ind_empleado])

    print(f'El total anual de tickets del empleado {id_empleado} es de {total_anual}.')


def reporte_mensual(matriz_empleados):
    # opcion_mensual = int(input(''))

    mes = int(input('Ingrese el mes (1-12) para el cual desea recibir el reporte de tickets: '))
    
    while mes < 0 or mes > 13:
            mes = int(input("Error - Mes inválido. Debe ingresar un valor entre 1 y 12: "))

    mes_ind = mes - 1
    total_mensual = 0

    for i in range(len(matriz_empleados)):
        total_mensual += matriz_empleados[i][mes_ind]
    
    print(f'El total de tickets mensual del mes {mes} es de {total_mensual}.')
