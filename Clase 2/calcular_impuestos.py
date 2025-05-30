consumo = int(input("Ingrese la cantidad de unidades consumidas: "))
impuesto = 0

if consumo <= 100: 
    impuesto = 0
elif consumo >= 101: 
    impuesto = consumo * 0.5
elif consumo >= 201: 
    impuesto = consumo * 0.7

print(f"Impuesto salido: ${impuesto}")





