# División con Precisión

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
k = int(input("Ingrese la cantidad de decimales: "))

entera = a // b
resi = a % b

resultado = str(entera) + '.'

for n in range(k):
    resi = resi * 10
    digito = resi // b
    resultado = resultado + str(digito)
    resi = resi % b  

print(resultado)
