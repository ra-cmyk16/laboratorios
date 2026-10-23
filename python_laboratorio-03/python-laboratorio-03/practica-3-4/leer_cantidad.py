while True:
    try:
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Debes escribir un entero.")
        print()
        continue

    if cantidad < 0:
        print("La cantidad no puede ser negativa.")
        print()
        continue

    print("Cantidad aceptada:", cantidad)
    break
