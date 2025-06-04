'''
Clase:        TC1001
Tema:         Bloques iterativos
Ejercicio:    ¡Adivina el número!
Descripción:  Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
              El programa debe seguir pidiendo números hasta que acierte. En cada
              intento fallido el programa notificará al usuario si el número secreto es
              mayor o menor al último valor ingresado.

Autor:        Yajaira Claros
Fecha:        2025-05-31
Estado:       [Terminado]
'''

import random
ns = random.randint(1, 100)

while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    if intento == ns:
        print("¡Felicidades! Has adivinado el número secreto")
        break  
    elif intento < ns:
        print("El número secreto es mayor")
    else:
        print("El número secreto es menor")
