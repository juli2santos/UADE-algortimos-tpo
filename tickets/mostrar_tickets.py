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
        print(f'Empleado {ids[i]}')
        for j in range(len(matriz_empleados[0])):
            n = input(f'Ingrese la cantidad de tickets del mes {meses[j]}: ').strip()
            while not es_entero_positivo(n):
                print('Error - Ingrese un número entero positivo.')
                n = input(f'Ingrese la cantidad de tickets del mes {meses[j]}: ').strip()   
            matriz_empleados[i][j] = n

#agregar validador de ingreso de tickets, cosa de que no se pueda agregar decimales, ni numeros negativos
