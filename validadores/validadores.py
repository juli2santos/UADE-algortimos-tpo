es_entero = lambda opcion, min_valor, max_valor: opcion.isdigit() and min_valor <= int(opcion) <= max_valor

def validar_empleados():
    while True: 
        try: 
            total_empleados = int(input('Ingrese la cantidad de empleados'))
            if total_empleados <= 0:
                print('Cantidad inválida. Ingrese un número mayor a 0')
            else: 
                return total_empleados
        except ValueError:
            print('Entrada inválida. Debe ingresar un número entero')
    # total_empleados = int(input("Ingrese la cantidad de empleados "))
    # while total_empleados <= 0:
    #     total_empleados = int(
    #         input("Cantidad inválida. Ingrese la cantidad de empleados ")
    #     )
    # return total_empleados

es_entero_positivo = lambda valor: valor.isdigit() and int(valor) >= 0

def validar_opcion(opcion, min_valor, max_valor):
    return es_entero(opcion, min_valor, max_valor)

def obtener_opcion():
    opcion = input("Elige una opción (1-5): ")
    while not validar_opcion(opcion, 1, 5):
        print("Error. Debe ser un número entre 1 y 5.")
        opcion = input("Elige una opción (1-5): ")
    return int(opcion)

def opcion_mensual():
    opcion = input('Elige una opción (1-2): ')
    while not validar_opcion(opcion, 1, 2):
        print("Error. Debe ser un número entre 1 y 2.")
        opcion = input("Elige una opción (1-2): ")
    return int(opcion)


def opcion_desemp():
    opcion = input('Elige una opción (1-3): ')
    while not validar_opcion(opcion, 1, 3):
        print("Error. Debe ser un número entre 1 y 3.")
        opcion = input("Elige una opción (1-3): ")
    return int(opcion)

def obtener_prioridad_valida(ticket_id):
    # Validar que la prioridad ingresada esté en la lista permitida
    prioridades_permitidas = ['baja', 'media', 'alta']
    while True:
        prioridad = input(f'Ingrese la prioridad del ticket {ticket_id} ({prioridades_permitidas}): ').strip().lower()
        try:
            if prioridad not in prioridades_permitidas:
                raise ValueError(f'Error: "{prioridad}" no es una prioridad válida.')
            return prioridad
        except ValueError as mensajeError:
            print(mensajeError)