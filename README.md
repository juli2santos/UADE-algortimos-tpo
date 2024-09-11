# UADE-algortimos-tpo - Ticketrack

# Sistema de Gestión de Tickets

## Descripción
Este es un sistema de gestión de tickets desarrollado en Python. Permite a los usuarios gestionar tickets asociados a empleados, incluyendo la adición, modificación y generación de reportes de tickets. El sistema soporta autenticación de usuarios, generación automática de IDs para empleados y diversos reportes (anuales, mensuales, y de desempeño).

## Características
- **Autenticación de Usuarios**: Permite a los usuarios iniciar sesión y registrarse.
- **Gestión de Tickets**: Añadir, modificar y mostrar tickets para cada empleado.
- **Generación de Reportes**:
  - Reporte Anual (total de tickets de todos los empleados).
  - Reporte Mensual (total de tickets por mes, total mensual individual).
  - Reporte de Desempeño (mejor y peor desempeño de tickets, promedio de tickets).

## Requisitos
- Python 3.6 o superior.
- Módulos de Python utilizados: `random` (para la generación de IDs).

## Instalación

1. **Clona el Repositorio**:
    ```bash
    git clone https://github.com/juli2santos/UADE-algortimos-tpo.git
    ```

2. **Navega al Directorio del Proyecto**:
    ```bash
    cd UADE-algortimos-tpo
    ```

3. **Ejecuta el Programa**:
    ```bash
    python main.py
    ```

## Uso

### Inicio de Sesión
1. Inicia el programa y selecciona la opción para iniciar sesión.
2. Introduce tu nombre de usuario y contraseña para acceder.

### Registro de Usuario
1. Si eres un nuevo usuario, selecciona la opción para registrarte.
2. Introduce un nombre de usuario y una contraseña para crear una cuenta.

### Gestión de Tickets
- **Añadir Tickets**:
  1. Selecciona la opción para añadir tickets.
  2. Ingresa el ID del empleado, el mes y la cantidad de tickets.

- **Modificar Tickets**:
  1. Selecciona la opción para modificar tickets.
  2. Cambia la cantidad de tickets para un empleado y mes específicos.

- **Mostrar Tickets**:
  1. Visualiza todos los tickets registrados en la matriz.

### Generación de Reportes
- **Reporte Anual**:
  1. Selecciona la opción para generar un reporte anual de tickets.

- **Reporte Mensual**:
  1. Elige entre un reporte mensual total o individual.

- **Reporte de Desempeño**:
  1. Genera reportes sobre el mejor y peor desempeño de empleados y el promedio total de tickets.

## Estructura del Código
- `main.py`: Punto de entrada del programa. Maneja la autenticación de usuarios, la gestión de tickets y la generación de reportes.
- `tickets/ticket.py`: Funciones relacionadas con la validación de empleados, generación de IDs y carga manual de tickets.
- `menu/menu.py`: Funciones para mostrar menús y obtener opciones del usuario.
- `auth.py`: Funciones para registrar usuarios, verificar credenciales y mostrar el menú de inicio de sesión.
- `validadores/validadores.py`: Funciones para validar entradas del usuario.
- `reportes/reportes.py`: Funciones para generar diferentes tipos de reportes.
- `tickets/mostrar_tickets.py`: Funciones para mostrar y modificar la matriz de tickets.

## Contribución
Para contribuir al proyecto, por favor sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad o corrección (`git checkout -b feature/mi-nueva-funcionalidad`).
3. Realiza tus cambios y haz commits (`git commit -am 'Añadida nueva funcionalidad'`).
4. Empuja los cambios a tu repositorio (`git push origin feature/mi-nueva-funcionalidad`).
5. Crea un pull request describiendo tus cambios.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.


