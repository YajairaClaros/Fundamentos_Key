'''
Clase:        TC1001
Tema:         Manejo de matrices
Ejercicio:    Diagonal principal y secundaria
Descripción:  Dada una matriz cuadrada ingresada por el
              usuario, crea dos listas, una con los
              elementos de la diagonal principal y la otra
              con los elementos de la diagonal secundaria.
              
Autor:        Yajaira Claros
Fecha:        2025-06-09
Estado:       [Terminado]
'''

def obtener_diagonales_desde_usuario():
    N = int(input("Ingrese la dimensión N de la matriz cuadrada (ej. 4): "))

    matriz = []
    print(f"Ahora ingrese las {N} filas de la matriz.")
    print("Para cada fila, ingrese N números enteros separados por comas (ej. 1,2,3,4):")

    for i in range(N):
        fila_str = input(f"Fila {i + 1}: ")
        fila_numeros_str = [x.strip() for x in fila_str.split(',')]
        fila_numeros = [int(num) for num in fila_numeros_str]
        matriz.append(fila_numeros)

    diagonal_principal = [matriz[i][i] for i in range(N)]
    diagonal_secundaria = [matriz[i][N - 1 - i] for i in range(N)]

    return diagonal_principal, diagonal_secundaria

principal, secundaria = obtener_diagonales_desde_usuario()

print("\n--- Resultados ---")
print(f"Diagonal Principal: {principal}")
print(f"Diagonal Secundaria: {secundaria}")