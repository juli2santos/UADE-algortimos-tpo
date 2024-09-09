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

