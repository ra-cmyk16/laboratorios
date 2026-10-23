#Reto — Factura simple
nombre_producto = "bombombun"
precio_unitario = 100000.0
cantidad = 2
descuento = 0.10
impuesto = 0.05

subtotal = cantidad * precio_unitario
valor_descuento = subtotal * descuento
total_antes = subtotal - valor_descuento
impuesto_total = total_antes * impuesto
total = impuesto_total + total_antes
print("---------------------")
print("  FACTURA ELECTRICA  ")
print("---------------------")
print(f"Producto: {nombre_producto} Precio unitario ${precio_unitario} Cantidad {cantidad}")
print()
print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${valor_descuento}")
print(f"Impuesto: ${impuesto_total}")
print(f"Total: ${total}")