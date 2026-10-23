from producto import Producto


class Inventario:
    def __init__(self):
        self._productos = []

    def registrar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise ValueError("Debe registrar un objeto Producto.")

        if self.buscar_por_codigo(producto.codigo) is not None:
            raise ValueError("Ya existe un producto con ese código.")

        self._productos.append(producto)
        return True

    def listar_productos(self):
        # Devuelve una copia para proteger la lista interna.
        return list(self._productos)

    def buscar_por_codigo(self, codigo):
        codigo = str(codigo).strip()

        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_existencias(self, codigo, nueva_cantidad):
        producto = self.buscar_por_codigo(codigo)

        if producto is None:
            return False

        producto.actualizar_existencias(nueva_cantidad)
        return True

    def eliminar_producto(self, codigo):
        producto = self.buscar_por_codigo(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)
        return True

    def productos_sin_stock(self):
        return [
            producto
            for producto in self._productos
            if producto.cantidad == 0
        ]

    def resumen(self):
        productos = self.listar_productos()

        return {
            "productos": len(productos),
            "unidades": sum(p.cantidad for p in productos),
            "valor_total": sum(
                p.calcular_valor() for p in productos
            ),
            "categorias": {
                p.categoria for p in productos
            }
        }

    def exportar_datos(self):
        return [
            producto.a_diccionario()
            for producto in self._productos
        ]

    def cargar_datos(self, registros):
        # Primero se valida todo en un inventario temporal.
        temporal = Inventario()

        if not isinstance(registros, list):
            raise ValueError(
                "El archivo debe contener una lista de productos."
            )

        for registro in registros:
            producto = Producto.desde_diccionario(registro)
            temporal.registrar_producto(producto)

        # Solo reemplaza los datos cuando todos son válidos.
        self._productos = temporal._productos