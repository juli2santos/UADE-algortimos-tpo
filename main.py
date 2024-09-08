from tickets.ticket import validar_empleados
from tickets.ticket import generar_ids
from menu.menu import menu

def main():
    total_empleados = validar_empleados()
    #print("total empleados",len(lista_empleados))
    filas = total_empleados #Cantidad de empleados 
    columnas = 12 # 12 una por cada mes

    matriz_empleados = [] #lista para inicializar la matriz
    ids= [] #lista de ids para empleados

    for f in range(filas):
        matriz_empleados.append([0]*columnas) #creacion de matriz de forma dinamica 

    if not ids:
            generar_ids(len(matriz_empleados), ids) #generacion de ids automaticamente post ingresar numero de empleados
    
    """Menú principal para la gestión de tickets."""

    menu(matriz_empleados, columnas, ids)
    


if __name__ == '__main__':
    main()