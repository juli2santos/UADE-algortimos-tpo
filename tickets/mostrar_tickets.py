from validadores.validadores import es_entero_positivo

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

def modificar_matriz(matriz_empleados, ids):
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    for i in range (len(matriz_empleados)):
        print(f'\n --- Empleado {ids[i]} ---')
        for j in range(len(matriz_empleados[0])):
            band = False
            while not band:
                n = input(f'Ingrese la cantidad de tickets del mes {meses[j]}: ').strip()
                if es_entero_positivo(n):
                    n = int(n) 
                    if 0 <= n <= 100:
                        matriz_empleados[i][j] = n
                        band = True
                    else:
                        print('Error - Ingrese un número entre 0 y 100.')
                else:
                    print('Error - Ingrese un número positivo entre 0 y 100.')


