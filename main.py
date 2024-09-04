#Lista para almacenar los tickets en memoria
tickets = []

def main():
    """Menú principal para la gestión de tickets."""
    running = True
    while running:
        print("\n--- Menú Ticketrack ---")
        print("1. Añadir Ticket")
        print("2. Actualizar Ticket")
        print("3. Generar Reporte")
        print("4. Mostrar Tickets")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            desc = input("Descripción del ticket: ")
            categoria = input("Categoría del ticket: ")
            prioridad = input("Prioridad del ticket (Alta/Media/Baja): ")
            agregar_ticket(desc, categoria, prioridad)
        elif opcion == '2':
            ticket_id = int(input("ID del ticket a actualizar: "))
            estado = input("Nuevo estado del ticket (Abierto/Cerrado): ")
            asignadoAEmpleado = input("Asignar a (nombre): ")
            actualizar_ticket(ticket_id, estado=estado, asignadoAUsuario=asignadoAEmpleado)
        elif opcion == '3':
          pass ## actaulizar con el reporte
        elif opcion == '4':
            pass ## actualizar con el reporte
        elif opcion == '5':
            print("Saliendo...")
            running = False
        else:
            print("Opción inválida. Por favor, elige una opción del menú.")

if _name_ == '_main_':
    main()