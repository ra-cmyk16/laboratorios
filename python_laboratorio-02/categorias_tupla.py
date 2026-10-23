categorias = ("Teclados", "Mouse", "Monitores", "Impresoras")

for i in range(len(categorias)):
    print(i + 1, "-", categorias[i])

categoria = input("Ingresa una categoría: ").strip()

if categoria in categorias:
    print("La categoría está permitida.")
else:
    print("La categoría no está permitida.")

print("Cantidad de categorías disponibles:", len(categorias))
"""
¿Por qué usar una tupla para categorías fijas y una lista
para productos que vas a registrar o eliminar?

Respuesta: una tupla es adecuada para las categorías que
no necesitamos modificar, mientras que una lista permite
agregar y eliminar productos fácilmente.
"""