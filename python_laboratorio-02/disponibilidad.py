#Ejercicio — Disponibilidad de un producto
unidades_disponibles = 12
unidades_solicitadas = 15

print(f"Hay unidades suficiente? {unidades_disponibles >= unidades_solicitadas}")
print(f"Las cantidades son iguales? {unidades_solicitadas == unidades_disponibles}")
print(f"Se solicitaron mas unidades de las disponibles? {unidades_solicitadas > unidades_disponibles}")