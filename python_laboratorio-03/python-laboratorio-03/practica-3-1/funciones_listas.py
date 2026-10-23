def calcular_unidades(productos):
    total = 0

    for producto in productos:
        total += producto["cantidad"]

    return total


def agregar(nombre, nombres):
    nombres.append(nombre)


def agregar_en_copia(nombre, nombres):
    copia = nombres.copy()
    copia.append(nombre)
    return copia


inventario = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 7}
]

print(calcular_unidades(inventario))

productos = ["Teclado"]
agregar("Mouse", productos)

print(productos)

original = ["Teclado"]
nueva = agregar_en_copia("Mouse", original)

print("Original:", original)
print("Nueva:", nueva)
