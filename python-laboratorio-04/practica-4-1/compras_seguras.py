cantidad_compras = 0
total = 0

while True:
    try:
        importe = float(input("Importe de la compra (0 para terminar): "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if importe == 0:
        break

    if importe < 0:
        print("El importe no puede ser negativo.")
        continue

    cantidad_compras += 1
    total += importe

print("Compras aceptadas:", cantidad_compras)
print("Suma acumulada:", total)
