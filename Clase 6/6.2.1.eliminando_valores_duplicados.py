'''
Clase:        TC1001
Tema:         Manejo de listas
Ejercicio:    Eliminando valores duplicados
Descripción:  Dada una lista ingresada por el usuario,
              elimina los elementos duplicados
              manteniendo la primera aparición de cada número.
              
Autor:        Yajaira Claros
Fecha:        2025-06-02
Estado:       [Terminado]
'''

li = input("Ingresa los números separados por espacio: ")

numdup = []
for x in li.split():
    numdup.append(int(x))

seen = set()
res = []

for dupli in numdup:
    if dupli not in seen:
        res.append(dupli)
        seen.add(dupli)

for i in range(len(res)):
    if i != len(res) - 1:
        print(res[i], end=" ")
    else:
        print(res[i])
