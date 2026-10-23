import math

from producto import Producto, CATEGORIAS
from inventario import Inventario
from almacenamiento import (
    cargar_inventario,
    guardar_inventario,
    ErrorInventarioArchivo
)
from reportes import exportar_csv


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto:
            return texto

        print("El campo no puede estar vacío.")


def leer_entero(mensaje):
    while True:
        texto = input(mensaje).strip()

        try:
            return int(texto)
        except ValueError:
            print("Ingresa un número entero válido.")


def leer_precio(mensaje):
    while True:
        texto = input(mensaje).strip().replace(",", ".")

        try:
            precio = float(texto)

            if not math.isfinite(precio) or precio <= 0:
                print("El precio debe ser positivo y finito.")
                continue

            return precio

        except ValueError:
            print("Ingresa un precio numérico válido.")


def leer_cantidad(mensaje):
    while True:
        cantidad = leer_entero(mensaje)

        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            continue

        return cantidad


def mostrar_menu():
    print("\n================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("8. Guardar inventario")
    print("9. Exportar reporte CSV")
    print("0. Salir")


def guardar_cambios(inventario):
    try:
        ruta = guardar_inventario(inventario)
        print(f"Inventario guardado correctamente: {ruta}")
        return True

    except OSError as error:
        print(f"ERROR: {error}")
        print(
            "Los cambios pueden permanecer en memoria, "
            "pero no se confirmó su guardado."
        )
        return False


def registrar_producto(inventario):
    codigo = leer_texto("Código: ")

    if inventario.buscar_por_codigo(codigo) is not None:
        print("Ya existe un producto con ese código.")
        return

    nombre = leer_texto("Nombre: ")

    print("\nCategorías permitidas:")
    for categoria in CATEGORIAS:
        print(f"- {categoria}")

    print("escribe la categoria en minusculas y sin tilde")

    categoria = leer_texto("Categoría: ")
    precio = leer_precio("Precio: ")
    cantidad = leer_cantidad("Cantidad: ")

    try:
        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            cantidad
        )

        inventario.registrar_producto(producto)
        print("Producto registrado.")
        guardar_cambios(inventario)

    except ValueError as error:
        print(f"No se pudo registrar el producto: {error}")


def listar_productos(inventario):
    productos = inventario.listar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    print("\n--- LISTA DE PRODUCTOS ---")

    for producto in productos:
        print(producto)


def buscar_producto(inventario):
    codigo = leer_texto("Código del producto: ")
    producto = inventario.buscar_por_codigo(codigo)

    if producto is None:
        print("No se encontró el producto.")
    else:
        print(producto)


def actualizar_existencias(inventario):
    codigo = leer_texto("Código del producto: ")
    producto = inventario.buscar_por_codigo(codigo)

    if producto is None:
        print("No se encontró el producto.")
        return

    print(f"Producto: {producto.nombre}")
    print(f"Cantidad actual: {producto.cantidad}")

    nueva_cantidad = leer_cantidad("Nueva cantidad: ")

    try:
        if inventario.actualizar_existencias(
            codigo,
            nueva_cantidad
        ):
            print("Existencias actualizadas.")
            guardar_cambios(inventario)
        else:
            print("No se pudo encontrar el producto.")

    except ValueError as error:
        print(f"No se pudo actualizar: {error}")


def eliminar_producto(inventario):
    codigo = leer_texto("Código del producto: ")
    producto = inventario.buscar_por_codigo(codigo)

    if producto is None:
        print("No se encontró el producto.")
        return

    confirmacion = input(
        f"¿Eliminar {producto.nombre}? (s/n): "
    ).strip().lower()

    if confirmacion != "s":
        print("Operación cancelada.")
        return

    if inventario.eliminar_producto(codigo):
        print("Producto eliminado.")
        guardar_cambios(inventario)
    else:
        print("No se pudo eliminar el producto.")


def consultar_sin_stock(inventario):
    productos = inventario.productos_sin_stock()

    if not productos:
        print("No hay productos sin existencias.")
        return

    print("\n--- PRODUCTOS SIN STOCK ---")

    for producto in productos:
        print(f"{producto.codigo} - {producto.nombre}")


def mostrar_resumen(inventario):
    resumen = inventario.resumen()

    print("\n--- RESUMEN DEL INVENTARIO ---")
    print(f"Productos registrados: {resumen['productos']}")
    print(f"Unidades disponibles: {resumen['unidades']}")
    print(f"Valor total: ${resumen['valor_total']:.2f}")

    categorias = sorted(resumen["categorias"])

    if categorias:
        print("Categorías utilizadas: " + ", ".join(categorias))
        print(f"Cantidad de categorías: {len(categorias)}")
    else:
        print("Categorías utilizadas: ninguna")
        print("Cantidad de categorías: 0")


def guardar_manual(inventario):
    try:
        ruta = guardar_inventario(inventario)
        print(f"Inventario guardado correctamente: {ruta}")

    except OSError as error:
        print(f"ERROR: {error}")
        print("No se confirmó el guardado.")


def exportar_reporte(inventario):
    try:
        ruta = exportar_csv(inventario)
        print(f"Reporte exportado correctamente: {ruta}")

    except OSError as error:
        print(f"No se pudo exportar el reporte: {error}")


def main():
    solo_lectura = False

    try:
        inventario = cargar_inventario()
        print("Inventario cargado correctamente.")

    except ErrorInventarioArchivo as error:
        print(f"\nADVERTENCIA: {error}")
        print("El archivo original no se modificará automáticamente.")
        print(
            "Se permite consultar el inventario vacío, "
            "pero no modificarlo."
        )
        inventario = Inventario()
        solo_lectura = True

    while True:
        mostrar_menu()

        try:
            opcion = input("Opción: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada interrumpida.")
            break

        if opcion == "0":
            if not solo_lectura:
                try:
                    guardar_inventario(inventario)
                    print("Cambios guardados.")
                except OSError as error:
                    print(f"No se confirmó el guardado: {error}")

            print("Programa finalizado.")
            break

        if opcion not in {
            "1", "2", "3", "4", "5",
            "6", "7", "8", "9"
        }:
            print("Opción inválida. Intenta nuevamente.")
            continue

        if solo_lectura and opcion in {"1", "4", "5", "8"}:
            print(
                "Operación bloqueada porque el JSON original "
                "tiene un error. Revisa o restaura el archivo."
            )
            continue

        try:
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
                guardar_manual(inventario)

            elif opcion == "9":
                exportar_reporte(inventario)

        except (EOFError, KeyboardInterrupt):
            print("\nOperación interrumpida. Regresando al menú.")

if __name__ == "__main__":
    main()