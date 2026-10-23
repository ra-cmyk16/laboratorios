# composicion.py
# Nota explicativa: Un inventario *contiene* productos (composición), por lo que 
# no debe heredar de Producto (herencia). La herencia se usa cuando hay una relación 
# jerárquica de tipo "es un" (ej. Instructor es un Empleado), mientras que la composición 
# expresa una relación de tipo "tiene un" o "contiene a".

class Almacenamiento:
    def guardar(self, datos):
        print(f"Guardando {len(datos)} registros en el medio de almacenamiento.")


class ServicioInventario:
    def __init__(self, almacenamiento):
        self.almacenamiento = almacenamiento

    def guardar_inventario(self, productos):
        self.almacenamiento.guardar(productos)


if __name__ == "__main__":
    almacen = Almacenamiento()
    servicio = ServicioInventario(almacen)
    
    productos_ejemplo = ["Teclado Mecánico", "Mouse Inalámbrico", "Monitor 24 pulgadas"]
    servicio.guardar_inventario(productos_ejemplo)