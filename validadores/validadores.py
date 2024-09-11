es_entero = lambda opcion, min_valor, max_valor: opcion.isdigit() and min_valor <= int(opcion) <= max_valor

def es_entero_positivo(valor):
    return valor.isdigit() and int(valor) >=0

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
