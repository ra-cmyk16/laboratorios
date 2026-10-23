from producto import Producto
from inventario import Inventario


def mostrar_menu():
    print()
    print("================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("8. Aumentar o disminuir existencias")
    print("9. Mostrar productos ordenados por nombre")
    print("10. Catálogo de códigos y nombres")
    print("11. Buscar productos por categoría")
    print("12. Producto con mayor valor de inventario")
    print("0. Salir")


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes escribir un número entero.")


def leer_cantidad():
    while True:
        cantidad = leer_entero("Cantidad: ")
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
        else:
            return cantidad


def leer_precio():
    while True:
        try:
            precio = float(input("Precio: "))
        except ValueError:
            print("Debes escribir un número válido.")
            continue
        if precio <= 0:
            print("El precio debe ser mayor que cero.")
        else:
            return precio


def mostrar_producto(producto):
    print(producto.codigo, "-", producto.nombre, "-", producto.categoria,
          "- $", producto.precio, "-", producto.cantidad, "unidades")


def registrar_producto(inventario):
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría (Periféricos, Componentes, Accesorios): ").strip()
    precio = leer_precio()
    cantidad = leer_cantidad()
    try:
        producto = Producto(codigo, nombre, categoria, precio, cantidad)
    except ValueError as error:
        print("No se pudo registrar el producto:", error)
        return
    if inventario.registrar_producto(producto):
        print("Producto registrado.")
    else:
        print("El código ya existe.")


def listar_productos(inventario):
    productos = inventario.listar_productos()
    if not productos:
        print("No hay productos registrados.")
    else:
        for producto in productos:
            mostrar_producto(producto)


def buscar_producto(inventario):
    producto = inventario.buscar_por_codigo(input("Código del producto: "))
    if producto is None:
        print("El producto no existe.")
    else:
        mostrar_producto(producto)


def actualizar_existencias(inventario):
    codigo = input("Código del producto: ").strip()
    if inventario.buscar_por_codigo(codigo) is None:
        print("El producto no existe.")
        return
    cantidad = leer_cantidad()
    if inventario.actualizar_existencias(codigo, cantidad):
        print("Existencias actualizadas.")
    else:
        print("No se pudieron actualizar las existencias.")


def eliminar_producto(inventario):
    codigo = input("Código del producto: ").strip()
    if inventario.eliminar_producto(codigo):
        print("Producto eliminado.")
    else:
        print("El producto no existe.")


def consultar_sin_stock(inventario):
    agotados = inventario.productos_sin_stock()
    if not agotados:
        print("No hay productos sin existencias.")
    else:
        print("Sin existencias:")
        for producto in agotados:
            print("-", producto.nombre)


def mostrar_resumen(inventario):
    resumen = inventario.resumen()
    print("Productos registrados:", resumen["productos"])
    print("Unidades disponibles:", resumen["unidades"])
    print("Valor del inventario: $" + str(resumen["valor"]))
    print("Categorías utilizadas:", ", ".join(sorted(resumen["categorias"])))
    print("Cantidad de categorías:", len(resumen["categorias"]))


def mover_existencias(inventario):
    codigo = input("Código del producto: ").strip()
    producto = inventario.buscar_por_codigo(codigo)
    if producto is None:
        print("El producto no existe.")
        return
    print("1. Aumentar existencias")
    print("2. Disminuir existencias")
    movimiento = input("Seleccione una operación: ").strip()
    if movimiento not in ("1", "2"):
        print("Operación no válida.")
        return
    cantidad = leer_cantidad()
    if movimiento == "1":
        nueva_cantidad = producto.cantidad + cantidad
    else:
        nueva_cantidad = producto.cantidad - cantidad
        if nueva_cantidad < 0:
            print("No hay suficientes existencias.")
            return
    inventario.actualizar_existencias(codigo, nueva_cantidad)
    print("Existencias actualizadas.")


def mostrar_ordenados(inventario):
    productos = inventario.productos_ordenados_por_nombre()
    if not productos:
        print("No hay productos registrados.")
    else:
        for producto in productos:
            mostrar_producto(producto)


def mostrar_catalogo(inventario):
    print(inventario.catalogo_codigos_nombres())


def buscar_categoria(inventario):
    categoria = input("Categoría: ").strip()
    productos = inventario.buscar_por_categoria(categoria)
    if not productos:
        print("No hay productos registrados en esa categoría.")
    else:
        for producto in productos:
            mostrar_producto(producto)


def mostrar_mayor_valor(inventario):
    producto = inventario.producto_mayor_valor()
    if producto is None:
        print("No hay productos registrados.")
    else:
        print("Producto con mayor valor de inventario:")
        mostrar_producto(producto)
        print("Valor total:", producto.calcular_valor())


def main():
    inventario = Inventario()
    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()
        if opcion == "1":
            registrar_producto(inventario)
        elif opcion == "2":
            listar_productos(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            actualizar_existencias(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            consultar_sin_stock(inventario)
        elif opcion == "7":
            mostrar_resumen(inventario)
        elif opcion == "8":
            mover_existencias(inventario)
        elif opcion == "9":
            mostrar_ordenados(inventario)
        elif opcion == "10":
            mostrar_catalogo(inventario)
        elif opcion == "11":
            buscar_categoria(inventario)
        elif opcion == "12":
            mostrar_mayor_valor(inventario)
        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
