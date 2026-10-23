ventas = [
    {"producto": "Teclado", "categoria": "Periféricos", "total": 150000},
    {"producto": "Mouse", "categoria": "Periféricos", "total": 70000},
    {"producto": "Disco SSD", "categoria": "Componentes", "total": 280000},
    {"producto": "Memoria USB", "categoria": "Accesorios", "total": 45000}
]

productos_mayores_for = []

for venta in ventas:
    if venta["total"] > 100000:
        productos_mayores_for.append(venta["producto"])

productos_mayores = [
    venta["producto"]
    for venta in ventas
    if venta["total"] > 100000
]

categorias = {
    venta["categoria"]
    for venta in ventas
}

producto_valor = {
    venta["producto"]: venta["total"]
    for venta in ventas
}

valores = [
    venta["total"]
    for venta in ventas
]

total_ventas = sum(valores)

print("Productos con ventas superiores a $100.000:", productos_mayores)
print("Categorías diferentes:", categorias)
print("Producto y valor de venta:", producto_valor)
print("Total de ventas:", total_ventas)
print("¿El for y la comprensión son equivalentes?:", productos_mayores_for == productos_mayores)

"""
Comprobación

1. Una transformación modifica o calcula los elementos; un filtro selecciona los que cumplen una condición.

2. La comprensión de lista usa [], la de conjunto usa {} y la de diccionario usa {clave: valor}.

3. Una tupla almacena varios elementos y no se puede modificar. Una expresión generadora produce valores a medida que se recorren, sin crear necesariamente una lista completa.

4. Una solución breve ocupa menos código, mientras que una fácil de leer permite comprender mejor lo que hace. Si hay varios pasos o mensajes durante el recorrido, un ciclo for puede ser más claro.

5. La palabra que faltaba para expresar el filtro era if.
"""