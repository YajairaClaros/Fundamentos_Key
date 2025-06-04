'''
Clase:        TC1001
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    Automatizando el cálculo de la propina
Descripción:  Pide al usuario el total de una cuenta y el porcentaje de propina
              (por ejemplo, 10%, 15%, 20%). Calcula y muestra en pantalla el total
              a pagar.

Autor:        Yajaira Claros
Fecha:        2025-05-15
Estado:       [Terminado]
'''

#Automatizando el cálculo de la propina

cuenta_total = float(input("Ingrese el total de la cuenta: $"))
porcentaje_propina = float(input("Ingrese el porcentaje de propina (por ejemplo, 10 para 10%): "))

propina = cuenta_total * (porcentaje_propina / 100)

total_con_propina = cuenta_total + propina

# Muestra los resultados con formato
print(f"\nTotal de la cuenta: ${cuenta_total}")
print(f"Propina: ${propina}")
print(f"Total de la cuenta con propina ({int(porcentaje_propina)}%): ${total_con_propina}")
