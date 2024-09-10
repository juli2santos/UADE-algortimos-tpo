from random import randint


def validar_empleados():
    total_empleados = int(input("Ingrese la cantidad de empleados "))
    while total_empleados <= 0:
        total_empleados = int(
            input("Cantidad inválida. Ingrese la cantidad de empleados ")
        )
    return total_empleados


def generar_ids(total_empleados, ids):
    while len(ids) < total_empleados:
        id = randint(1000, 9999)
        if id not in ids:
            ids.append(id)
            print("Empleado", id)
    print("IDs generados:", ids)


def cargar_ticket_manual(matriz, ids):

    salir = False
    print(f'IDs de los empleados: {ids}')

    while not salir:

        empleado = int(input("Ingrese el ID del empleado al que desea modificarle un ticket: "))
        while empleado not in ids <= 0:
            empleado = int(input("Error - ID de empleado inválido. Intente con un ID existente: "))

        mes = int(input("Ingrese el mes (1-12) para el cual desea cargar el valor: "))
        while mes < 0 or mes > 13:
            mes = int(input("Error - Mes inválido. Debe ingresar un valor entre 1 y 12: "))

        cantidad = int(input("Ingrese la cantidad total de tickets: "))
        while cantidad <= 0:
            cantidad = int(input("Error - Cantidad inválida. Ingrese un valor mayor a 0"))

        matriz[ids.index(empleado)][
            mes - 1
        ] = cantidad  # mes -1 para ir al mes ingresado por el usuario por q la lista empieza de 0 sino da mal
        
        salida = int(input("Ingrese 1 para continuar con otra carga, o ingrese cualquier otro número para regresar al menú: "))

        if salida != 1:
            salir = True
