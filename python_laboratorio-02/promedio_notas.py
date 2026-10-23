cantidad = int(input("Cantidad de notas: "))

if cantidad > 0:
    suma = 0
    for i in range(1, cantidad + 1):
        nota = float(input(f"Nota {i}: "))
        suma = suma + nota

    promedio = suma / cantidad
    print(f"\nPromedio: {promedio}")
else:
    print("La cantidad de notas debe ser mayor que cero.")
