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
