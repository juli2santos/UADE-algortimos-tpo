from datetime import datetime
es_entero = lambda opcion, min_valor, max_valor: opcion.isdigit() and min_valor <= int(opcion) <= max_valor

dias_de_cada_mes ={   #Diccionario local del propio modulo, unicamente para los dias de cada mes
    1: 31, 
    2: 28,  
    3: 31, 
    4: 30, 
    5: 31, 
    6: 30,  
    7: 31, 
    8: 31,  
    9: 30,  
    10: 31, 
    11: 30, 
    12: 31  
}
    
def validar_empleados():
    while True: 
        try: 
            total_empleados = int(input('Ingrese la cantidad de empleados: '))
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
    opcion = input("Elige una opción (1-6): ")
    while not validar_opcion(opcion, 1, 6):
        print("Error. Debe ser un número entre 1 y 6.")
        opcion = input("Elige una opción (1-6): ")
    return int(opcion)

def opcion_mensual():
    opcion = input('Elige una opción (1-3): ')
    while not validar_opcion(opcion, 1, 3):
        print("Error. Debe ser un número entre 1 y 3.")
        opcion = input("Elige una opción (1-3): ")
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

def obtener_dia_valido(ticket_id, mes):
    dia_mes = dias_de_cada_mes.get(mes, 31)

    while True:
        dia_input = input(f'Ingrese el día del ticket {ticket_id} (1-{dia_mes}): ')
        try:
            dia = int(dia_input)
            # Verificar si la combinación de día y mes es válida usando datetime
            validar_fecha(mes, dia)  # Verifica la fecha
            return dia
        except ValueError as mensajeError:
            if str(mensajeError) == "Día fuera del rango válido para el mes.":
                print(f'Error: El día {dia} no es válido para el mes {mes}. Intente nuevamente.')
            else:
                print('Error: Debe ingresar un número válido. Intente nuevamente.')

def validar_fecha(mes, dia):
    # Usar el año actual para crear la fecha
    try:
        año_actual = datetime.now().year
        fecha = datetime(año_actual, mes, dia)
        return fecha  # Si se crea la fecha, es válida
    except ValueError:
        raise ValueError("Día fuera del rango válido para el mes.")