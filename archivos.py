# crear un arcchivo csv con un header con el diccionario de cada mes, hay que poner cada ticket en una fila
#string doble

import csv

def exportar_tickets_csv(matriz_empleados, ids, archivo_salida="tickets.csv"):
    """
    Exporta los tickets de los empleados a un archivo CSV.
    
    :param matriz_empleados: Matriz que contiene los tickets de los empleados por mes.
    :param ids: Lista de IDs de empleados.
    :param archivo_salida: Nombre del archivo CSV donde se exportarán los datos.
    """
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

    try:
        with open(archivo_salida, mode='w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)

            # Escribir la cabecera
            escritor_csv.writerow(["Empleado ID", "Mes", "Ticket ID", "Descripción", "Fecha", "Prioridad"])

            # Recorrer los empleados
            for i, id_empleado in enumerate(ids):
                # Recorrer cada mes
                for j, mes in enumerate(meses):
                    # Revisar si hay tickets en ese mes
                    tickets_mes = matriz_empleados[i][j]
                    if tickets_mes:  # Si existen tickets en el mes
                        for ticket_id, ticket_info in tickets_mes.items():
                            escritor_csv.writerow([id_empleado, mes, ticket_info['id'], ticket_info['descripcion'], ticket_info['Fecha'], ticket_info['prioridad']])

        print(f"Archivo CSV '{archivo_salida}' generado exitosamente.")
    except Exception as e:
        print(f"Error al generar el archivo CSV: {e}")