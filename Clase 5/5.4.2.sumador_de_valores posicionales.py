'''
Clase:        TC1001
Tema:         Bloques iterativos
Ejercicio:    Sumador de valores posicionales
Descripción:  Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
              Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2.

Autor:        Yajaira Claros
Fecha:        2025-05-31
Estado:       [Terminado]
'''

num = int(input("Ingresa un número: "))

print(f"Proceso de reducción para {num}:")
while num >= 10:
    digitos = [int(d) for d in str(num)] # int(d) convierte cada letra en número y str(num) convierte el número en texto:
    suma = sum(digitos)
    suma_texto = " + ".join(str(d) for d in digitos)
    print(f"{num} = {suma_texto} = {suma}")
    num = suma

print(f"El resultado final es: {num}")
