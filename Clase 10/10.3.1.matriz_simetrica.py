'''
Clase:        TC1001
Tema:         Manejo de matrices
Ejercicio:    Matriz simétrica
Descripción:  Dada una matriz cuadrada ingresada por el
              usuario, comprueba si la matriz cuadrada es
              simétrica respecto a su diagonal principal.
              
Autor:        Yajaira Claros
Fecha:        2025-06-09
Estado:       [Terminado]
'''
def comprobar_simetria_matriz():
    dimension_n = int(input("Ingrese la dimensión N de la matriz cuadrada: "))

    matriz_cuadrada = []
    print(f"Ingrese las {dimension_n} filas de la matriz.")
    print("Para cada fila, ingrese N números enteros separados por comas (ej. 1,2,3):")
    for i in range(dimension_n):
        elementos_fila = [int(elemento_str) for elemento_str in input(f"Fila {i + 1}: ").split(',')]
        matriz_cuadrada.append(elementos_fila)

    es_simetrica = True
    for i in range(dimension_n):
        for j in range(dimension_n):
            if matriz_cuadrada[i][j] != matriz_cuadrada[j][i]:
                es_simetrica = False
                break
        if es_simetrica == False:
            break

    if es_simetrica:
        print("La matriz es simétrica")
    else:
        print("La matriz no es simétrica")

comprobar_simetria_matriz()