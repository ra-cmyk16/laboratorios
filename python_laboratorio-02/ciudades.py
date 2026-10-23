ciudades = ["Bogotá", "Medellín", "Cali", "Cartagena", "Barranquilla"]

print("Primera ciudad:", ciudades[0])
print("Tercera ciudad:", ciudades[2])
print("Última ciudad:", ciudades[-1])
print("Cantidad de ciudades:", len(ciudades))

#Agregar elementos con append()
print()
productos = []

productos.append("Teclado")
productos.append("Mouse")
productos.append("Monitor")

print(productos)
print("Cantidad:", len(productos))

print()
nuevo_producto = input("Producto nuevo: ").strip()
productos.append(nuevo_producto)

print(productos)