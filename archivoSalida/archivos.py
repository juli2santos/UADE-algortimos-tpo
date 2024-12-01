def exportar_tickets_csv(matriz_empleados, ids, archivo_salida="reporteTickets.csv"):
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    try:
        with open(archivo_salida, mode='w') as archivo:
            # Encabezado de los tickets detallados
            archivo.write("Empleado ID,Mes,Ticket ID,Descripción,Fecha,Prioridad\n")

            for i, id_empleado in enumerate(ids):
                for j, mes in enumerate(meses):
                    tickets_mes = matriz_empleados[i][j]
                    if tickets_mes:
                        for ticket_id, ticket_info in tickets_mes.items():
                            archivo.write(
                                f"{id_empleado},{mes},{ticket_info['id']},{ticket_info['descripcion']},{ticket_info['fecha']},{ticket_info['prioridad']}\n"
                            )
        print(f"Archivo CSV '{archivo_salida}' generado exitosamente.")
    except Exception:
        print("Error al generar el archivo CSV")

def exportar_matriz_empleados_csv(matriz_empleados, ids, archivo_salida="reporteAnual.csv"):
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    columnas = len(meses)
    try:
        with open(archivo_salida, mode='w') as archivo:
            # Encabezado al igual que la matriz de empleados
            header = 'Empleado ID,' + ','.join(meses) + '\n'
            archivo.write(header)

            # Agregar la cantidad de tickets por mes para cada empleado
            for i, id_empleado in enumerate(ids):
                fila = [f"Empleado {id_empleado}"]
                for j in range(columnas):
                    fila.append(str(len(matriz_empleados[i][j])))
                archivo.write(','.join(fila) + '\n')

        print(f"Archivo CSV '{archivo_salida}' generado exitosamente.")
    except Exception:
        print("Error al generar el archivo CSV")

def exportar_tickets_empleado_csv(matriz_empleados, id_empleado, ids, archivo_salida="reporteAnualEmpleado.csv"):
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    if id_empleado not in ids:
        print(f"Error - No se encontró el empleado con ID {id_empleado}.")
        return
    ind_empleado = ids.index(id_empleado)
    try:
        with open(archivo_salida, mode='w') as archivo:
            # Encabezado general
            archivo.write("Empleado ID,Mes,Ticket ID,Descripción,Fecha,Prioridad\n")

            # Exportar los tickets del empleado por cada mes
            for j, mes in enumerate(meses):
                tickets_mes = matriz_empleados[ind_empleado][j]
                if tickets_mes:
                    for ticket_id, ticket_info in tickets_mes.items():
                        archivo.write(
                            f"{id_empleado},{mes},{ticket_id},{ticket_info.get('descripcion', '')},{ticket_info.get('fecha', '')},{ticket_info.get('prioridad', '')}\n"
                        )
        print(f"Archivo CSV '{archivo_salida}' para el empleado {id_empleado} generado exitosamente.")
    except Exception:
        print(f"Error - No se pudo generar el archivo CSV para el empleado {id_empleado}")

def exportar_tickets_mes_csv(matriz_empleados, mes, id_empleado, ids, archivo_salida="reporteMensualEmpleado.csv"):
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    if mes < 1 or mes > 12:
        print("Error - Mes inválido. Debe ser un valor entre 1 y 12.")
        return
    mes_ind = mes - 1
    try:
        with open(archivo_salida, mode='w') as archivo:
            # Encabezado general
            archivo.write("Empleado ID,Mes,Ticket ID,Descripción,Fecha,Prioridad\n")

            if id_empleado in ids:
                i = ids.index(id_empleado)
                tickets_mes = matriz_empleados[i][mes_ind]

                if tickets_mes:
                    for ticket_id, ticket_info in tickets_mes.items():
                        archivo.write(
                            f"{id_empleado},{meses[mes_ind]},{ticket_id},{ticket_info.get('descripcion', '')},{ticket_info.get('fecha', '')},{ticket_info.get('prioridad', '')}\n"
                        )
                print(f"Archivo CSV '{archivo_salida}' para el mes {mes} generado exitosamente.")
            else:
                print(f"Error - No se pudo encontrar el empleado {id_empleado}")
    except Exception:
        print(f"Error - No se pudo generar el archivo CSV para el mes {mes}.")
