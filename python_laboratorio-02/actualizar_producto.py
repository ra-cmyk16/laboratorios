producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000,
    "cantidad": 10
}

nuevo_precio = float(input("Ingresa el nuevo precio: "))

if nuevo_precio > 0:
    producto["precio"] = nuevo_precio
    print("Precio actualizado correctamente.")
else:
    print("El precio debe ser mayor que cero.")

for clave, valor in producto.items():
    print(clave, ":", valor)
#Una lista de diccionarios
print()
productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000.0, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000.0, "cantidad": 7},
    {"codigo": "P003", "nombre": "Monitor", "precio": 700000.0, "cantidad": 2}
]

for producto in productos:
    print(producto["codigo"], "-", producto["nombre"])

#Calcular sobre una lista de diccionarios
valor_inventario = 0

for producto in productos:
    valor_inventario += producto["precio"] * producto["cantidad"]

print("Valor del inventario:", valor_inventario)
"""Antes de ejecutar
Teclados: 85.000 × 4 = 340.000
Mouse: 45.000 × 7 = 315.000
Monitores: 700.000 × 2 = 1.400.000
total = 2.055.000
"""