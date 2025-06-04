'''
Clase:        TC1001
Tema:         Manejo de listas
Ejercicio:    Números líderes
Descripción:  Un número en una lista es "líder" si es
              estrictamente mayor que todos los
              elementos a su derecha. Dada una lista de
              números ingresada por el usuario, imprime
              todos los números líderes.
              
Autor:        Yajaira Claros
Fecha:        2025-06-02
Estado:       [Terminado]
'''

num = input("Ingresa los números separados por espacios: ").split()

numeros = []
for e in num:
    if e.isdigit(): 
        numeros.append(int(e))

lideres = []
mayor = -1

for numero in reversed(numeros):
    if numero > mayor:
        lideres.insert(0, numero)
        mayor = numero
print(lideres)
