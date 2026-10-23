# ValueError: el valor no sirve para la operación.
try:
    cantidad = int("abc")
except ValueError:
    print("El contenido no representa un entero.")

# TypeError: el tipo de dato no es compatible con la operación.
try:
    cantidad = int(None)
except TypeError:
    print("El tipo recibido no permite esa conversión.")
