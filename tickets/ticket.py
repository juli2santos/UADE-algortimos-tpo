from random import randint
def validar_empleados():
    total_empleados = int(input('Ingrese la cantidad de empleados'))
    while total_empleados <=0:
        total_empleados = int(input('Cantidad inválida. Ingrese la cantidad de empleados'))
    return total_empleados

def generar_ids(total_empleados, ids):
    while len(ids) < total_empleados:
        id = randint(1000, 9999)
        if id not in ids:
            ids.append(id)
            print('Empleado', id)
    print("IDs generados:", ids)
