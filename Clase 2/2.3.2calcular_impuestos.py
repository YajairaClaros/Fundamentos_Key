'''
Clase:        TC1001
Tema:         Bloque condicional
Ejercicio:    Cálculo de impuesto
Descripción:  Desarrollar un programa en Python que permita calcular el impuesto que debe pagar
              un usuario por el consumo de energía. El cálculo debe realizarse basado en la siguiente
              tabla.

Autor:        Yajaira Claros
Fecha:        2025-05-22
Estado:       [Terminado]
'''

consumo = int(input("Ingrese la cantidad de unidades consumidas: "))
impuesto = 0

if consumo <= 100: 
    impuesto = 0
elif consumo >= 101: 
    impuesto = consumo * 0.5
elif consumo >= 201: 
    impuesto = consumo * 0.7

print(f"Impuesto salido: ${impuesto}")





