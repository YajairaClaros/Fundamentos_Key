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
