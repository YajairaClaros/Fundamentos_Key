'''
Clase:        TC1001
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    Generador del correo de Key
Descripción:  Solicita al usuario su nombre completo (asume dos nombres y
              dos apellidos). Luego, el programa generará, su correo con el formato:
              primer_nombre.primer_apellido@keyinstitute.edu.sv

Autor:        Yajaira Claros
Fecha:        2025-05-15
Estado:       [Terminado]
'''

# Generador del correo de Key
name = input("Ingrese su nombre completo (dos nombres y dos apellidos): ")
psotion = name.strip().split() 
# split hace que: partes = ['pn', 'sn', 'pa', 'sa']

pnombre = psotion[0]
papellido = psotion[2]

correo = f"{pnombre.lower()}.{papellido.lower()}@keyinstitute.edu.sv"

print(f"\nEl correo asignado: {correo}")
