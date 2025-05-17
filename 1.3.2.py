# Generador del correo de Key

name = input("Ingrese su nombre completo (dos nombres y dos apellidos): ")
psotion = name.strip().split() 
# split hace que: partes = ['pn', 'sn', 'pa', 'sa']

pnombre = psotion[0]
papellido = psotion[2]

correo = f"{pnombre.lower()}.{papellido.lower()}@keyinstitute.edu.sv"

print(f"\nEl correo asignado: {correo}")
