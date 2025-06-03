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
