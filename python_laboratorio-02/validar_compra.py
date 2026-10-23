precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
descuento = float(input("Descuento (%): "))

if precio <= 0 or cantidad <= 0:
    print("El precio y la cantidad deben ser mayores que cero.")
elif descuento < 0 or descuento > 100:
    print("El descuento debe estar entre 0 y 100.")
else:
    subtotal = precio * cantidad
    valor_descuento = subtotal * descuento / 100
    total = subtotal - valor_descuento

    print("Subtotal:", subtotal)
    print("Descuento:", valor_descuento)
    print("Total:", total)

#Depuración — Una condición equivocada
membresia = False
valor_compra = 200000
#se cambia el or por and para que requiera las dos condiciones
if membresia and valor_compra >= 150000:
    print("Aplica descuento.")
else:
    print("No aplica descuento.")    