def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


def calcular_descuento(subtotal, porcentaje):
    descuento = subtotal * porcentaje / 100
    return descuento


def calcular_impuesto(base, porcentaje):
    impuesto = base * porcentaje / 100
    return impuesto


precio = 100000
cantidad = 2
porcentaje_descuento = 10
porcentaje_impuesto = 19

subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal, porcentaje_descuento)
base = subtotal - descuento
impuesto = calcular_impuesto(base, porcentaje_impuesto)
total = base + impuesto

print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Base después del descuento:", base)
print("Impuesto:", impuesto)
print("Total:", total)
