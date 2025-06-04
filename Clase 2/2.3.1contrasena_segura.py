'''
Clase:        TC1001
Tema:         Bloque condicional
Ejercicio:    Contraseña segura
Descripción:  Solicita una cadena de texto que representa una contraseña, y verifica si la contraseña
              cumple con las siguientes condiciones: tener al menos 8 caracteres, un número y una
              mayúscula.

Autor:        Yajaira Claros
Fecha:        2025-05-22
Estado:       [Terminado]
'''

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

    
