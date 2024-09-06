def mostrar_tickets(matriz_empleados, columnas, ids):
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    header = ' ' * 15 + ''.join([f"{mes:5}|" for mes in meses])
    print(header)
    print('-' * len(header))
    
    for i in range(len(matriz_empleados)):
        print(f'Empleado {ids[i]:<6}', end='')
        for j in range(columnas):
            print(f"{matriz_empleados[i][j]:^6}", end="")
        print()