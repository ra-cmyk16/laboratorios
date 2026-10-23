codigos = [" p001 ", "P002", "", " p003", "  "]

codigos_normalizados = [codigo.strip().upper() for codigo in codigos if codigo.strip()]

print(codigos_normalizados)
#Una condición que produce valores diferentes
print()
notas = [2.5, 3.8, 4.1]

estados = ["Aprobado" if nota >= 3.0 else "No aprobado" for nota in notas]

print(estados)
#Comprensión de conjuntos
print()
categorias = ["Periféricos", "Accesorios", "Periféricos", "Componentes"]

unicas = {categoria for categoria in categorias}

print(unicas)
#Ejercicio — Categorías distintas
print()
productos = [
    {"nombre": "Teclado", "categoria": "Periféricos"},
    {"nombre": "Mouse", "categoria": "Periféricos"},
    {"nombre": "Disco", "categoria": "Componentes"}
]

categorias = {producto["categoria"] for producto in productos}

print(categorias)
#Comprensión de diccionarios
print()
numeros = [1, 2, 3, 4]

cuadrados = {numero: numero ** 2 for numero in numeros}

print(cuadrados)
#Ejercicio — Catálogo por código
print()
productos = [
    {"codigo": "P001", "nombre": "Teclado"},
    {"codigo": "P002", "nombre": "Mouse"},
    {"codigo": "P003", "nombre": "Monitor"}
]

catalogo = {producto["codigo"]: producto["nombre"] for producto in productos}

print(catalogo)
#Comprensión sobre una lista de diccionarios
print()
productos = [
    {"nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"nombre": "Mouse", "precio": 45000, "cantidad": 0},
    {"nombre": "Monitor", "precio": 700000, "cantidad": 2}
]

disponibles = [
    producto["nombre"]
    for producto in productos
    if producto["cantidad"] > 0
]

print(disponibles)

valores = [
    producto["precio"] * producto["cantidad"]
    for producto in productos
]

print("Valor total:", sum(valores))

sin_existencias = [
    producto["nombre"]
    for producto in productos
    if producto["cantidad"] == 0
]

precios_superiores = [
    producto["nombre"]
    for producto in productos
    if producto["precio"] > 100000
]

cantidades_diferentes = {
    producto["cantidad"]
    for producto in productos
}

nombre_precio = {
    producto["nombre"]: producto["precio"]
    for producto in productos
}

print("Productos sin existencias:", sin_existencias)
print("Productos con precio superior a $100.000:", precios_superiores)
print("Cantidades diferentes:", cantidades_diferentes)
print("Nombre y precio:", nombre_precio)
#Comprensiones anidadas y expresiones generadoras
print()
grupos = [[1, 2], [3, 4], [5, 6]]

numeros = [numero for grupo in grupos for numero in grupo]

print(numeros)
#Depuración — Sintaxis de una comprensión
print()
numeros = [1, 2, 3, 4, 5]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

