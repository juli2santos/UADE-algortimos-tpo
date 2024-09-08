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

    while not salir:

        empleado = int(input("ingrese el empleado al que desea agregarle un ticket: "))
        while empleado not in ids <= 0:
            empleado = int(input("empleado invalido, intente con uno existente: "))

        mes = int(input("ingrese el mes para el que desea cargar el valor: "))
        while mes <= 0 or mes >= 12:
            mes = int(input("Mes invalido, debe intgresar un valor entre 1 y 12: "))

        cantidad = int(input("Ingrese la cantidad total de tickets"))
        while cantidad <= 0:
            cantidad = int(input("Cantidad invalida, ingrese un valor mayor a 0"))

        matriz[ids.index(empleado)][
            mes - 1
        ] = cantidad  # mes -1 para ir al mes ingresado por el usuario por q la lista empieza de 0 sino da mal
        salida = int(input("Si desea continuar con otra carga ingrese 1"))
        if salida != 1:
            salir = True
