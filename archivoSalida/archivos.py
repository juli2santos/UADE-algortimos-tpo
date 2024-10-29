# crear un arcchivo csv con un header con el diccionario de cada mes, hay que poner cada ticket en una fila
#string doble

import csv
def exportar_tickets_csv(matriz_empleados, ids, archivo_salida="tickets.csv"):
    """
    Exporta los tickets de los empleados a un archivo CSV con encabezado estructurado.
    
    :param matriz_empleados: Matriz que contiene los tickets de los empleados por mes.
    :param ids: Lista de IDs de empleados.
    :param archivo_salida: Nombre del archivo CSV donde se exportarán los datos.
    """
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    columnas = len(meses)

    try:
        with open(archivo_salida, mode='w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)

            #Encabezado al igual que la matriz de empleados
            header = ['Empleado ID'] + [f"{mes:>5}" for mes in meses]
            escritor_csv.writerow(header)

            escritor_csv.writerow(['-' * 15] + ['-' * 5 for _ in range(columnas)])

            # Agregar la cantidad de tickets por mes para cada empleado
            for i, id_empleado in enumerate(ids):
                fila = [f"Empleado {id_empleado:<6}"] 
                for j in range(columnas):
                    fila.append(f"{len(matriz_empleados[i][j]):^5}") 
                escritor_csv.writerow(fila)

            escritor_csv.writerow([])

            # Encabezado de los tickets detallados
            escritor_csv.writerow(["Empleado ID", "Mes", "Ticket ID", "Descripción", "Fecha", "Prioridad"])

            for i, id_empleado in enumerate(ids):
                for j, mes in enumerate(meses):
                    tickets_mes = matriz_empleados[i][j]
                    if tickets_mes:
                        for ticket_id, ticket_info in tickets_mes.items():
                            escritor_csv.writerow([
                                f"{id_empleado:<10}",  # Alineación a la izquierda
                                f"{mes:<5}",          # Alineación a la izquierda
                                f"{ticket_info['id']:<10}",  # Alineación a la izquierda
                                f"{ticket_info['descripcion']:<20}",  # Alineación a la izquierda
                                f"{ticket_info['fecha']:<10}",  # Alineación a la izquierda
                                f"{ticket_info['prioridad']:<10}"  # Alineación a la izquierda
                            ])

        print(f"Archivo CSV '{archivo_salida}' generado exitosamente.")
    except Exception:
        print("Error al generar el archivo CSV")
