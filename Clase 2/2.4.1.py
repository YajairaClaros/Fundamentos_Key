# Suma de cadenas de texto

n = int(input("Ingrese un número entero: "))

if 1 <= n <= 10**18:
    if n % 7 == 0 and n % 5 != 0:
        print("Mágico")
    else:
        print("Normal")
else:
    print("El número está fuera del rango permitido (1 ≤ n ≤ 10^18).")
