'''
Clase:        TC1001
Tema:         Bloques iterativos
Ejercicio:    Suma de valores
Descripción:  Dada una lista de longitud variable de números enteros ingresada por el usuario,
              calcula e imprime la suma de todos los números usando un bucle for.

Autor:        Yajaira Claros
Fecha:        2025-05-31
Estado:       [Terminado]
'''

n = input("Ingresa una lista de números enteros separados por espacios: ")
cadenas = n.split()

numeros = []
for i in cadenas:
    numeros.append(int(i))

print("Lista de números:", numeros)
suma_total = 0
for num in numeros:
    suma_total += num

print("La suma de todos los números es:", suma_total)
