def validar_empleados():
    total_empleados = int(input('Ingrese la cantidad de empleados'))
    while total_empleados <=0:
        total_empleados = int(input('Ingrese la cantidad de empleados'))
    return total_empleados