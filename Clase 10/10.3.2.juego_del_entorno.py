'''
Clase:        TC1001
Tema:         Manejo de matrices
Ejercicio:    Juego del entorno
Descripción:  Dada una matriz binaria ingresada por el
              usuario, verifica para cada celda de una
              matriz binaria cuántos elementos con valor
              de 1 hay en las celdas vecinas (arriba, abajo,
              izquierda, derecha, diagonales).
              
Autor:        Yajaira Claros
Fecha:        2025-06-09
Estado:       [Terminado]
'''

# Función para contar los 1 vecinos de cada celda
def contar_vecinos_unos(matriz, n, m):
    direcciones = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1),          (0, 1),
                   (1, -1),  (1, 0),  (1, 1)]
    
    resultado = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            conteo = 0
            for dx, dy in direcciones:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    if matriz[ni][nj] == 1:
                        conteo += 1
            resultado[i][j] = conteo
    
    return resultado

# Entrada del usuario
n = int(input("Ingresa el número de filas (N): "))
m = int(input("Ingresa el número de columnas (M): "))

print(f"Ahora ingresa los {n} conjuntos de {m} números (separados por comas):")

# Leer la matriz
matriz = []
for i in range(n):
    fila = list(map(int, input(f"Fila {i+1}: ").split(",")))
    if len(fila) != m:
        print("La cantidad de números no coincide con las columnas indicadas.")
        exit()
    matriz.append(fila)

# Procesar y mostrar resultado
salida = contar_vecinos_unos(matriz, n, m)

print("\nMatriz de salida:")
for fila in salida:
    print(fila)