class Inventario:
    def __init__(self):
        self._productos = []

    def registrar_producto(self, producto):
        if self.buscar_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def listar_productos(self):
        return self._productos.copy()

    def buscar_por_codigo(self, codigo):
        codigo = codigo.strip().upper()
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_existencias(self, codigo, nueva_cantidad):
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        return producto.actualizar_existencias(nueva_cantidad)

    def eliminar_producto(self, codigo):
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        return True

    def productos_sin_stock(self):
        return [producto for producto in self._productos if producto.cantidad == 0]

    def resumen(self):
        unidades = sum(producto.cantidad for producto in self._productos)
        valor = sum(producto.calcular_valor() for producto in self._productos)
        categorias = {producto.categoria for producto in self._productos}
        return {
            "productos": len(self._productos),
            "unidades": unidades,
            "valor": valor,
            "categorias": categorias
        }

    def buscar_por_categoria(self, categoria):
        return [producto for producto in self._productos if producto.categoria == categoria]

    def productos_ordenados_por_nombre(self):
        return sorted(self._productos, key=lambda producto: producto.nombre.lower())

    def catalogo_codigos_nombres(self):
        return {producto.codigo: producto.nombre for producto in self._productos}

    def producto_mayor_valor(self):
        if not self._productos:
            return None
        mayor = self._productos[0]
        for producto in self._productos:
            if producto.calcular_valor() > mayor.calcular_valor():
                mayor = producto
        return mayor
