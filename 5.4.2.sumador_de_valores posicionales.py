num = int(input("Ingresa un número: "))

print(f"Proceso de reducción para {num}:")
while num >= 10:
    digitos = [int(d) for d in str(num)] # int(d) convierte cada letra en número y str(num) convierte el número en texto:
    suma = sum(digitos)
    suma_texto = " + ".join(str(d) for d in digitos)
    print(f"{num} = {suma_texto} = {suma}")
    num = suma

print(f"El resultado final es: {num}")
