contra = input("Ingrese la contraseña: ")

longitud = len(contra) >= 8
numero = False
mayuscula = False

for n in contra:
    if n.isdigit():
        numero = True
    if n.isupper():
        mayuscula = True

if longitud and numero and mayuscula:
    print("Contraseña segura.")
else:
    print("Contraseña insegura")

    
