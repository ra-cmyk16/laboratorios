CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

productos = []
opcion = ""

while opcion != "0":
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

    opcion = input("Opción: ").strip()

    if opcion == "1":
        codigo = input("Código: ").strip().upper()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        codigo_repetido = False

        for producto in productos:
            if producto["codigo"] == codigo:
                codigo_repetido = True

        if not codigo or not nombre:
            print("El código y el nombre no pueden estar vacíos.")
        elif codigo_repetido:
            print("El código ya existe.")
        elif categoria not in CATEGORIAS:
            print("La categoría no es válida.")
        elif precio <= 0:
            print("El precio debe ser mayor que cero.")
        elif cantidad < 0:
            print("La cantidad no puede ser negativa.")
        else:
            nuevo_producto = {
                "codigo": codigo,
                "nombre": nombre,
                "categoria": categoria,
                "precio": precio,
                "cantidad": cantidad
            }

            productos.append(nuevo_producto)
            print("Producto registrado.")

    elif opcion == "2":
        if not productos:
            print("No hay productos registrados.")
        else:
            for producto in productos:
                print(
                    producto["codigo"], "-",
                    producto["nombre"], "-",
                    producto["categoria"], "- $",
                    producto["precio"], "-",
                    producto["cantidad"], "unidades"
                )

    elif opcion == "3":
        codigo_buscado = input("Código del producto: ").strip().upper()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is not None:
            print("Código:", encontrado["codigo"])
            print("Nombre:", encontrado["nombre"])
            print("Categoría:", encontrado["categoria"])
            print("Precio:", encontrado["precio"])
            print("Cantidad:", encontrado["cantidad"])
        else:
            print("El producto no existe.")

    elif opcion == "4":
        codigo_buscado = input("Código del producto: ").strip().upper()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is None:
            print("El producto no existe.")
        else:
            nueva_cantidad = int(input("Nueva cantidad: "))

            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                encontrado["cantidad"] = nueva_cantidad
                print("Existencias actualizadas.")

    elif opcion == "5":
        codigo_buscado = input("Código del producto: ").strip().upper()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is None:
            print("El producto no existe.")
        else:
            productos.remove(encontrado)
            print("Producto eliminado.")

    elif opcion == "6":
        agotados = [
            producto["nombre"]
            for producto in productos
            if producto["cantidad"] == 0
        ]

        if agotados:
            print("Sin existencias:")

            for nombre in agotados:
                print("-", nombre)
        else:
            print("No hay productos sin existencias.")

    elif opcion == "7":
        unidades_totales = sum([
            producto["cantidad"]
            for producto in productos
        ])

        valor_inventario = sum([
            producto["precio"] * producto["cantidad"]
            for producto in productos
        ])

        categorias_utilizadas = {
            producto["categoria"]
            for producto in productos
        }

        print("Productos:", len(productos))
        print("Unidades:", unidades_totales)
        print("Valor del inventario: $" + str(valor_inventario))
        print("Categorías utilizadas:", ", ".join(sorted(categorias_utilizadas)))
        print("Cantidad de categorías:", len(categorias_utilizadas))

    elif opcion == "8":
        codigo_buscado = input("Código del producto: ").strip().upper()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is None:
            print("El producto no existe.")
        else:
            print("1. Aumentar existencias")
            print("2. Disminuir existencias")
            movimiento = input("Seleccione una operación: ").strip()
            cantidad_movimiento = int(input("Cantidad del movimiento: "))

            if cantidad_movimiento < 0:
                print("La cantidad del movimiento no puede ser negativa.")
            elif movimiento == "1":
                encontrado["cantidad"] += cantidad_movimiento
                print("Existencias aumentadas.")
            elif movimiento == "2":
                if cantidad_movimiento > encontrado["cantidad"]:
                    print("No hay suficientes existencias.")
                else:
                    encontrado["cantidad"] -= cantidad_movimiento
                    print("Existencias disminuidas.")
            else:
                print("Operación no válida.")

    elif opcion == "9":
        productos_ordenados = sorted(productos, key=lambda producto: producto["nombre"].lower())

        if not productos_ordenados:
            print("No hay productos registrados.")
        else:
            for producto in productos_ordenados:
                print(
                    producto["codigo"], "-",
                    producto["nombre"], "-",
                    producto["categoria"], "- $",
                    producto["precio"], "-",
                    producto["cantidad"], "unidades"
                )

    elif opcion == "10":
        catalogo = {
            producto["codigo"]: producto["nombre"]
            for producto in productos
        }

        print(catalogo)

    elif opcion == "11":
        categoria_buscada = input("Categoría: ").strip()

        encontrados = [
            producto
            for producto in productos
            if producto["categoria"] == categoria_buscada
        ]

        if encontrados:
            for producto in encontrados:
                print(
                    producto["codigo"], "-",
                    producto["nombre"], "- $",
                    producto["precio"], "-",
                    producto["cantidad"], "unidades"
                )
        else:
            print("No hay productos registrados en esa categoría.")

    elif opcion == "12":
        if not productos:
            print("No hay productos registrados.")
        else:
            mayor_valor = productos[0]

            for producto in productos:
                if producto["precio"] * producto["cantidad"] > mayor_valor["precio"] * mayor_valor["cantidad"]:
                    mayor_valor = producto

            print("Producto con mayor valor de inventario:")
            print("Código:", mayor_valor["codigo"])
            print("Nombre:", mayor_valor["nombre"])
            print("Precio:", mayor_valor["precio"])
            print("Cantidad:", mayor_valor["cantidad"])
            print("Valor total:", mayor_valor["precio"] * mayor_valor["cantidad"])

    elif opcion == "0":
        print("Programa finalizado.")

    else:
        print("Opción no válida.")