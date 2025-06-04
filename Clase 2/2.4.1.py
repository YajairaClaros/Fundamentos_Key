'''
Clase:        TC1001
Tema:         Bloque condicional
Ejercicio:    El número mágico
Descripción:  Crea un programa en Python para determinar si un número es "mágico“.
              Un número es “mágico” si es divisible por 7 pero no por 5.

Autor:        Yajaira Claros
Fecha:        2025-05-22
Estado:       [Terminado]
'''

n = int(input("Ingrese un número entero: "))

if 1 <= n <= 10**18:
    if n % 7 == 0 and n % 5 != 0:
        print("Mágico")
    else:
        print("Normal")
else:
    print("El número está fuera del rango permitido (1 ≤ n ≤ 10^18).")
