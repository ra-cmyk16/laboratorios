from producto import Producto
from inventario import Inventario

inventario = Inventario()

print("Agregar P001 Teclado:", inventario.agregar(Producto("P001", "Teclado")))
print("Agregar P002 Mouse:", inventario.agregar(Producto("P002", "Mouse")))
print("Agregar P001 repetido:", inventario.agregar(Producto("P001", "Otro teclado")))

print()
print("Productos registrados:", len(inventario.listar()))
for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)

print()
print("Eliminar P999 (no existe):", inventario.eliminar("P999"))
print("Eliminar P002:", inventario.eliminar("P002"))

print()
print("Productos registrados:", len(inventario.listar()))
for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)

print("Buscar P002:", inventario.buscar_por_codigo("P002"))
