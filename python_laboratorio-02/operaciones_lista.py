productos = ["Teclado", "Mouse", "Monitor"]

productos[1] = "Mouse inalámbrico"
productos.insert(1, "Cámara web")

eliminado = productos.pop()

print("Elementos:", productos)
print("Extraído:", eliminado)

#Ejercicio — Cambios de inventario
print()
productos = ["Teclado", "Mouse", "Monitor"]
nuevos = ["Impresora", "Cámara"]

productos[1] = "Mouse inalámbrico"
print("Paso 1:", productos)

productos.insert(0, "Parlantes")
print("Paso 2:", productos)

productos.extend(nuevos)
print("Paso 3:", productos)

productos.remove("Monitor")
print("Paso 4:", productos)

eliminado = productos.pop()
print("Elemento extraído:", eliminado)
print("Paso 5:", productos)

print("Lista final:", productos)

#Obtener partes de una lista y ordenar
print()
productos = ["Teclado", "Mouse", "Monitor", "Cámara", "Parlantes"]

print(productos[0:2])
print(productos[2:])
print(productos[:3])
print(productos[-2:])

print()
productos = ["Monitor", "Cámara", "Teclado"]

ordenados = sorted(productos)

print("Original:", productos)
print("Ordenados:", ordenados)
#Copiar no es lo mismo que compartir la lista
print()
original = ["Teclado", "Mouse"]
copia = original.copy()

copia.append("Monitor")

print("Original:", original)
print("Copia:", copia)