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
                        print("Error - ID de empleado inválido.")
                        continue
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

        # Me fijo si hay tickets para ese empleado para ese mes
        if len(matriz[ids.index(empleado)][mes - 1]) == 0:
            print(f"No hay tickets registrados para el empleado {empleado} en el mes {mes}.")
            break

        try:
            # muestro los tickets disponibles
            print(f"Tickets para el empleado {empleado} en el mes {mes}:")
            for ticket_id, ticket in matriz[ids.index(empleado)][mes - 1].items():
                print(f"ID: {ticket_id}, Descripción: {ticket['descripcion']}, Prioridad: {ticket['prioridad']}")

            # pido el ID del ticket a modificar
            ticket_id = int(input("Ingrese el ID del ticket que desea modificar: "))
            while ticket_id not in matriz[ids.index(empleado)][mes - 1]:
                ticket_id = int(input("Error - ID de ticket inválido. Ingrese un ID de ticket existente: "))
            
            opcion = int(input("Ingrese 1 si quiere modificar la descripción o 2 si quiere modificar la prioridad"))
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
                print('La descripción no puede estar vacía.')
            break
        except ValueError:
            print('La descripción no puede estar vacía.')

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
    print("Carga inicial finalizada.")

def eliminar_ticket(matriz_empleados, ids):
    print(f"\n--- IDs de los empleados: {ids} ---")

    #Empleado
    while True:
        try:
            empleado_id = int(input("Ingrese el ID del empleado: "))
            if empleado_id not in ids:
                print("Error - ID de empleado inválido.")
                continue
            break
        except ValueError:
            print("Error - ID de empleado inválido.")

    #Mes
    while True:
        try:
            mes = int(input("Ingrese el mes (1-12) en el cual desea eliminar un ticket: "))
            if mes < 1 or mes > 12:
                print("Error - Mes inválido. Debe ingresar un valor entre 1 y 12")
                continue
            break
        except ValueError:
            print("Error - Mes inválido. Debe ingresar un valor entre 1 y 12")

    #Validar si hay existencia de tickets del empleado en dicho mes 
    tickets_mes = matriz_empleados[ids.index(empleado_id)][mes - 1]
    if not tickets_mes:
        print(f"No hay tickets registrados para el empleado {empleado_id} en el mes {mes}.")
        return

    #Mostrar los tickets disponibles
    print(f"\nTickets del empleado {empleado_id} en el mes {mes}:")
    ticket_ids = list(tickets_mes.keys())
    for i, ticket_id in enumerate(ticket_ids):
        ticket = tickets_mes[ticket_id]
        print(f"{i + 1}. ID: {ticket_id}, Descripción: {ticket['descripcion']}, Prioridad: {ticket['prioridad']}")

    #Input del ticket a eliminar
    while True:
        try:
            id_muestra_input = ticket_ids[0]
            ticket_elegido = int(input(f"Ingrese el número del ticket que desea eliminar (por ejemplo, 1 para ID {id_muestra_input}): "))
            if ticket_elegido < 1 or ticket_elegido > len(ticket_ids):
                print(f"Error - Ingrese el número del ticket que desea eliminar (por ejemplo, 1 para ID {id_muestra_input}): ")
                continue
            break
        except ValueError:
            print(f"Error - Ingrese el número del ticket que desea eliminar (por ejemplo, 1 para ID {id_muestra_input}): ")

    #Elimino el ticket y actualizacion de la matriz
    while True:
        try:
            ticket_id_a_eliminar = ticket_ids[ticket_elegido - 1]
            tickets_mes.pop(ticket_id_a_eliminar, None)  # Elimino el ticket si existe
            matriz_empleados[ids.index(empleado_id)][mes - 1] = tickets_mes # Actualizo la matriz
            break
        except IndexError:
            print('Error - Ingrese un número de ID de ticket válido.')

    print(f"\nTicket {ticket_id_a_eliminar} eliminado correctamente")
