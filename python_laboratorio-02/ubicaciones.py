categorias = ("Periféricos", "Componentes", "Accesorios")

for categoria in categorias:
    print(categoria)

elegida = input("Categoría: ").strip()

if elegida in categorias:
    print("Categoría válida.")
else:
    print("Categoría no registrada.")

#Depuración — Desempaquetado incorrecto
print()
producto = ("P001", "Teclado", 85000)

codigo, nombre, precio = producto

print("Código:", codigo)
print("Nombre:", nombre)
print("Precio:", precio)