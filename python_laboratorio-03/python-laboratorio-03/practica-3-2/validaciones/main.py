import validaciones

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

nombre = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
categoria = input("Categoría: ").strip()

if (
    validaciones.nombre_valido(nombre)
    and validaciones.precio_valido(precio)
    and validaciones.cantidad_valida(cantidad)
):
    print("Datos aceptados.")
else:
    print("Revisa los datos.")

if validaciones.categoria_valida(categoria, CATEGORIAS):
    print("Categoría válida.")
else:
    print("Categoría no registrada.")
