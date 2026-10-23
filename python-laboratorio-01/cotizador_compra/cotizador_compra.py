nombre_cliente = str(input("Escribe el nombre del cliente: "))
nombre_producto = str(input("Escribe el nombre del producto: "))
nombre_vendedor = str(input("Escribe el nombre del vendedor: "))
precio_unitario = float(input("Escribe el precio unitario del producto: "))
cantidad = int(input("Escribe la cantidad del producto: "))
descuento = int(input("Escribe el porcentaje del descuento: "))
impuesto = int(input("Escribe el impuesto del producto: "))
costo_envio = float(input("Escribe el costo de envío: "))
codigo = int(input("Escribe el código de la cotización: "))

impuestazo = impuesto / 100
descuentazo = descuento / 100
subtotal = precio_unitario * cantidad
valor_descuento = descuentazo * subtotal
base = subtotal - valor_descuento
valor_impuesto = impuestazo * base
total = base + valor_impuesto + costo_envio

print ("======================")
print ("   COTIZADOR PYTHON   ")
print ("======================")
print()
print(f"Nombre del cliente: {nombre_cliente}")
print(f"Nombre del vendedor: {nombre_vendedor}")
print(f"Produto: {nombre_producto}")
print(f"Precio unitario: {precio_unitario}")
print(f"Cantidad: {cantidad}")
print(f"Descuento (%): {descuento}")
print(f"Impuesto (%): {impuesto}")
print(f"Costo de envió: {costo_envio}")
print(f"Codigo de la cotización: {codigo}")
print()
print("------------------------")
print("RESUMEN DE COMPRA    ")
print("------------------------")
print(f"Cliente: {nombre_cliente}")
print(f"Vendedor: {nombre_vendedor}")
print(f"Producto: {nombre_producto}")
print(f"Precio unitario: ${precio_unitario}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${valor_descuento}")
print(f"Base: ${base}")
print(f"Impuesto: ${valor_impuesto}")
print(f"Costo de envío: ${costo_envio}")
print(f"TOTAL: ${total}")