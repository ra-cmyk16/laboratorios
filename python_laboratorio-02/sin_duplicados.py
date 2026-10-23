productos = ["Teclado", "Mouse"]

nombre = input("Ingresa el nombre del producto nuevo: ")

if nombre == "":
    print("El producto no puede estar vacío.")
elif nombre in productos:
    print("El producto ya está registrado.")
else:
    productos.append(nombre)
    print("Producto agregado correctamente.")

print("Lista de productos:", productos)

#Eliminar un elemento
print()
productos = ["Teclado", "Mouse", "Monitor"]

productos.remove("Mouse")

print(productos)
nombre = input("Producto a eliminar: ").strip()

if nombre in productos:
    productos.remove(nombre)
    print("Producto eliminado.")
else:
    print("No se encontró el producto.")