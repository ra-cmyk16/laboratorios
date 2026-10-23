total_ahorrado = 0
cantidad_depositos = 0

deposito = int(input("Depósito (0 para terminar): "))

while deposito != 0:
    if deposito > 0:
        total_ahorrado = total_ahorrado + deposito
        cantidad_depositos = cantidad_depositos + 1

        print("Ahorro acumulado:", total_ahorrado)
    else:
        print("El depósito debe ser positivo.")

    deposito = int(input("Depósito (0 para terminar): "))

print()
print("Depósitos válidos:", cantidad_depositos)
print("Total ahorrado:", total_ahorrado)
"""
¿Cuándo usar for?
Cuando conocemos de antemano cuántas veces queremos repetir
una operación, por ejemplo, recorrer diez números.

¿Cuándo usar while?
Cuando la repetición depende de una condición, como registrar
depósitos hasta ingresar cero.

¿Cómo se termina el ciclo?
La variable deposito se actualiza en cada repetición mediante
input(). Cuando su valor es 0, la condición deposito != 0
deja de cumplirse.
"""