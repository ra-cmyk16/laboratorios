# Versión original (con error): el dato se cambiaba ANTES de validarlo,
# así que una cantidad inválida quedaba guardada de todos modos.
#
#   producto._cantidad = nueva_cantidad
#   if nueva_cantidad < 0:
#       print("Cantidad inválida.")
#
# Corrección: validar primero y modificar solo si el dato es aceptable.
class Producto:
    def __init__(self):
        self._cantidad = 10


producto = Producto()
nueva_cantidad = -4

if nueva_cantidad < 0:
    print("Cantidad inválida.")
else:
    producto._cantidad = nueva_cantidad

print("Cantidad actual:", producto._cantidad)
