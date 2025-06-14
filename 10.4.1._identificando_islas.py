'''
Clase:        TC1001
Tema:         Manejo de matrices
Ejercicio:    Identificando islas
Descripción:  Dada una matriz binaria ingresada por el
              usuario (0 = agua, 1 = tierra), cuenta la
              cantidad de islas disponibles. Una isla está
              formada por elementos con valor de 1
              conectados horizontal o verticalmente.
              
Autor:        Yajaira Claros
Fecha:        2025-06-09
Estado:       [Proceso]
'''
def contar_islas():
    dimensiones_str = input("Ingrese las dimensiones n,m de la matriz (ej. 4,5): ")
    dimension_filas, dimension_columnas = map(int, dimensiones_str.split(','))

    grid_mapa = []
    print(f"Ingrese las {dimension_filas} filas de la matriz binaria.")
    print("Para cada fila, ingrese m números (0s o 1s) separados por comas (ej. 1,1,0,1,1):")
    for fila_num in range(dimension_filas):
        # INICIO: Parte desglosada
        fila_str = input(f"Fila {fila_num + 1}: ")
        elementos_str_lista = fila_str.split(',')
        
        elementos_fila = []
        for val_str in elementos_str_lista:
            numero_entero = int(val_str.strip())
            elementos_fila.append(numero_entero)
        
        grid_mapa.append(elementos_fila)

    numero_islas = 0

    def explorar_isla(fila_actual, columna_actual):
        if fila_actual < 0 or fila_actual >= dimension_filas or \
           columna_actual < 0 or columna_actual >= dimension_columnas or \
           grid_mapa[fila_actual][columna_actual] == 0:
            return
        grid_mapa[fila_actual][columna_actual] = 0
        explorar_isla(fila_actual + 1, columna_actual)
        explorar_isla(fila_actual - 1, columna_actual)
        explorar_isla(fila_actual, columna_actual + 1)
        explorar_isla(fila_actual, columna_actual - 1)

    for r_idx in range(dimension_filas):
        for c_idx in range(dimension_columnas):
            if grid_mapa[r_idx][c_idx] == 1:
                numero_islas += 1
                explorar_isla(r_idx, c_idx)
    
    print(numero_islas)

contar_islas()
