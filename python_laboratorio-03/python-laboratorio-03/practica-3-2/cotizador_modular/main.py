import calculos
import validaciones

print("=============================")
print("      COTIZADOR PYTHON")
print("=============================")
print()

cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = float(input("Descuento (%): "))
porcentaje_impuesto = float(input("Impuesto (%): "))

if not validaciones.precio_valido(precio) or not validaciones.cantidad_valida(cantidad):
    print("El precio y la cantidad deben ser mayores que cero.")
elif (
    not validaciones.porcentaje_valido(porcentaje_descuento)
    or not validaciones.porcentaje_valido(porcentaje_impuesto)
):
    print("Los porcentajes deben estar entre 0 y 100.")
else:
    subtotal = calculos.calcular_subtotal(precio, cantidad)
    valor_descuento = calculos.calcular_descuento(subtotal, porcentaje_descuento)
    base = subtotal - valor_descuento
    valor_impuesto = calculos.calcular_impuesto(base, porcentaje_impuesto)
    total = base + valor_impuesto

    print()
    print("-----------------------------")
    print("RESUMEN DE COMPRA")
    print("-----------------------------")
    print(f"Cliente: {cliente}")
    print(f"Producto: {producto}")
    print(f"Precio unitario: ${precio}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${subtotal}")
    print(f"Descuento: ${valor_descuento}")
    print(f"Base: ${base}")
    print(f"Impuesto: ${valor_impuesto}")
    print(f"TOTAL: ${total}")
