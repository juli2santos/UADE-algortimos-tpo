es_entero = lambda opcion: opcion.isdigit() and 1 <= int(opcion) <= 5

def validar_opcion(opcion):
    return es_entero(opcion)

def obtener_opcion():
    opcion = input("Elige una opción (1-5): ")
    while not validar_opcion(opcion):
        print("Error. Debe ser un número entre 1 y 5.")
        opcion = input("Elige una opción (1-5): ")
    return int(opcion)