productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000, "cantidad": 10},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000, "cantidad": 15},
    {"codigo": "P003", "nombre": "Monitor", "precio": 650000, "cantidad": 5}
]

codigo = input("Ingresa el código del producto: ")
nombre = input("Ingresa el nombre del producto: ")
precio = float(input("Ingresa el precio del producto: "))
cantidad = int(input("Ingresa la cantidad del producto: "))

nuevo_producto = {
    "codigo": codigo,
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
}

productos.append(nuevo_producto)

print("\nCatálogo de productos:")

for producto in productos:
    print(producto)

#Estructuras anidadas
curso = {
    "nombre": "Fundamentos de Python",
    "aprendices": ["Ana", "Luis", "Camila"],
    "instructor": {
        "nombre": "María",
        "area": "Software"
    }
}

print(curso["nombre"])
print(curso["aprendices"][1])
print(curso["instructor"]["nombre"])