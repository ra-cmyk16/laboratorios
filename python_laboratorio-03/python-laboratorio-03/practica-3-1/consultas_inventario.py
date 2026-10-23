def agotados(productos):
    nombres = []

    for producto in productos:
        if producto["cantidad"] == 0:
            nombres.append(producto["nombre"])

    return nombres


def agotados_comprension(productos):
    return [
        producto["nombre"]
        for producto in productos
        if producto["cantidad"] == 0
    ]


productos = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 0},
    {"nombre": "Monitor", "cantidad": 2},
    {"nombre": "Cámara", "cantidad": 0}
]

print("Con for y append():", agotados(productos))
print("Con comprensión:", agotados_comprension(productos))
