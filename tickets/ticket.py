from random import randint, choice
from validadores.validadores import es_entero_positivo,obtener_prioridad_valida,obtener_dia_valido


def generar_ids(total_empleados, ids):
    while len(ids) < total_empleados:
        id = randint(1000, 9999)
        if id not in ids:
            ids.append(id)
            print("Empleado", id)
    print("\n --- IDs generados:", ids, "---")


def actualizar_tickets(matriz, ids):

    salir = False
    print(f"\n --- IDs de los empleados: {ids} ---")

    while not salir:

        while True:
            try:
                empleado = int(input("Ingrese el ID del empleado al que desea modificarle un ticket: "))
                if empleado not in ids:
                    raise ValueError("Error - ID de empleado inválido.")
                break  # Salir del bucle si el ID es válido
            except ValueError:
                print('"Error - ID de empleado inválido."')


        while True:
            try:
                mes = int(input("Ingrese el mes (1-12) para el cual desea cargar el valor: "))           
                if mes < 1 or mes > 12:
                    mes = int(
                        input("Error - Mes inválido. Debe ingresar un valor entre 1 y 12: ")
                )
                break
            except ValueError:
                print('Error - Mes inválido. Debe ingresar un valor entre 1 y 12: ')

        # Me fijo si hay ticktes para ese empleado para ese mes
        if len(matriz[ids.index(empleado)][mes - 1]) == 0:
            print(f"No hay tickets registrados para el empleado {empleado} en el mes {mes}.")
            continue
        try:
            # muestro los tickets disponibles
            print(f"Tickets para el empleado {empleado} en el mes {mes}:")
            for ticket_id, ticket in matriz[ids.index(empleado)][mes - 1].items():
                print(f"ID: {ticket_id}, Descripción: {ticket['descripcion']},Prioridad: {ticket["prioridad"]}")

            # pido el ID del ticket a modificar
            ticket_id = int(input("Ingrese el ID del ticket que desea modificar: "))
            while ticket_id not in matriz[ids.index(empleado)][mes - 1]:
                ticket_id = int(input("Error - ID de ticket inválido. Ingrese un ID de ticket existente: "))
            
            opcion = int(input("ingrese 1 si quiere modificar la descripcion o 2 si quiere modificar la prioridad"))
            # Modificar los datos del ticket
            if opcion == 1:
                nuevaDesc = input("Nueva descripción: ")
                matriz[ids.index(empleado)][mes - 1][ticket_id]['descripcion'] = nuevaDesc.strip()
            else:
                nuevaPrioridad = obtener_prioridad_valida(ticket_id)
                matriz[ids.index(empleado)][mes - 1][ticket_id]['prioridad'] = nuevaPrioridad
                
        except ValueError:
            print('Error - Ingrese un número válido')   
        
        print(f"Ticket {ticket_id} actualizado correctamente.")
        print(f"\n --- IDs de los empleados: {ids} ---")

        salida = int(input("Ingrese 1 para continuar con otra carga, o ingrese cualquier otro número para regresar al menú: "))

        if salida != 1:
            salir = True


def mostrar_tickets(matriz_empleados, columnas, ids):

    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    header = ' ' * 15 + ''.join([f"{mes:5}|" for mes in meses])
    print(header)
    print('-' * len(header))
    
    for i in range(len(matriz_empleados)):
        print(f'Empleado {ids[i]:<6}', end='')
        for j in range(columnas):
            print(f"{len(matriz_empleados[i][j]):^6}", end="")
        print()

def cargar_tickets(matriz_empleados, ids, tickets):
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    for i in range (len(matriz_empleados)):
        print(f'\n --- Empleado {ids[i]} ---')

        for j in range(len(matriz_empleados[0])):
            band = False
            while not band:
                n = input(f'Ingrese la cantidad de tickets del mes {meses[j]}: ').strip()
                if es_entero_positivo(n):
                    n = int(n) 
                    if 0 <= n <= 100:
                        if not matriz_empleados[i][j]:  # Solo genero el nuevo diccionario si está vacio ese index
                            matriz_empleados[i][j] = {}
                        for _ in range(n):
                            ticket = crearTicket(tickets,j+1) # j + 1 para obtener el mes correcto
                            # agrego el ticket usando su id como clave
                            matriz_empleados[i][j][ticket['id']] = ticket
                        band = True
                    else:
                        print('Error - Ingrese un número entre 0 y 100.')
                else:
                    print('Error - Ingrese un número positivo entre 0 y 100.')
        
            siguienteMes = input("¿Quiere cargar tickets para el siguiente mes? (s/n): ").strip().lower() # valido si quiere cargar ticktes para otro mes
            if siguienteMes != 's':
                break
        
        siguienteEmpleado = input("¿Quiere continuar con otro empleado? (s/n): ").strip().lower() # valido si quiere cargar ticktes para otro empleado
        if siguienteEmpleado != 's':
            break




def crearTicket(tickets,mes):
    while True:
        ticket_id = randint(10000, 99999)
        if not any(ticket['id'] == ticket_id for ticket in tickets):
            break

    while True:
        try:
            descripcion = input(f'Ingrese la descripción del ticket {ticket_id}: ')
            if not descripcion.strip(): 
                raise ValueError('La descripción no puede estar vacía.')
            break
        except ValueError as error:
            print(error)

    ticket = {
        'id': ticket_id,
        'descripcion': descripcion,
        'fecha': obtener_dia_valido(ticket_id,mes),
        "prioridad": obtener_prioridad_valida(ticket_id)
    }

    tickets.append(ticket) 
    return ticket
    


def generarCargaInicial (matriz_empleados, ids, tickets):
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    for i in range (len(matriz_empleados)):
        for j in range(len(matriz_empleados[0])):
            band = False
            while not band:
                n = 5
                matriz_empleados[i][j] = {}
                for k in range(n):
                    while True:
                        ticket_id = randint(10000, 99999)
                        if not any(ticket['id'] == ticket_id for ticket in tickets):
                            break
                    ticket = {
                        'id': ticket_id,
                        'descripcion': f'TEST - {ticket_id}',
                        'fecha': f'2024-{j}-{k+1}',
                        "prioridad": choice(['baja','media','alta'])
                        }
                    tickets.append(ticket) 
                    matriz_empleados[i][j][ticket['id']] = ticket
                    band = True
    print("Carga incial finalizada")
                
    
def generarCargaInicial (matriz_empleados, ids, tickets):
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    for i in range (len(matriz_empleados)):
        for j in range(len(matriz_empleados[0])):
            band = False
            while not band:
                n = 5
                matriz_empleados[i][j] = {}
                for k in range(n):
                    while True:
                        ticket_id = randint(10000, 99999)
                        if not any(ticket['id'] == ticket_id for ticket in tickets):
                            break
                    ticket = {
                        'id': ticket_id,
                        'descripcion': f'TEST - {ticket_id}',
                        'fecha': f'2024-{j}-{k+1}',
                        "prioridad": choice(['baja','media','alta'])
                        }
                    tickets.append(ticket) 
                    matriz_empleados[i][j][ticket['id']] = ticket
                    band = True
    print("Carga incial finalizada")
                
