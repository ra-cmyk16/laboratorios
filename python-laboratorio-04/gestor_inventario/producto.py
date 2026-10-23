import math

CATEGORIAS = ("perifericos", "componentes", "accesorios")


class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        codigo = str(codigo).strip()
        nombre = str(nombre).strip()
        categoria = str(categoria).strip()

        if not codigo:
            raise ValueError("El código no puede estar vacío.")

        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")

        if categoria not in CATEGORIAS:
            raise ValueError("La categoría no es válida.")

        if isinstance(precio, bool) or not isinstance(precio, (int, float)):
            raise ValueError("El precio debe ser numérico.")

        if not math.isfinite(precio) or precio <= 0:
            raise ValueError("El precio debe ser positivo y finito.")

        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un número entero.")

        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self._precio = float(precio)
        self._cantidad = cantidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        if isinstance(nueva_cantidad, bool) or not isinstance(
            nueva_cantidad, int
        ):
            raise ValueError("La cantidad debe ser un número entero.")

        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self._cantidad = nueva_cantidad
        return True

    def calcular_valor(self):
        return self._precio * self._cantidad

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    @classmethod
    def desde_diccionario(cls, datos):
        campos = {
            "codigo", "nombre", "categoria", "precio", "cantidad"
        }

        if not isinstance(datos, dict):
            raise ValueError("El producto debe ser un objeto JSON.")

        if set(datos.keys()) != campos:
            raise ValueError(
                "El producto contiene campos faltantes o inesperados."
            )

        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["cantidad"]
        )

    def __str__(self):
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Cantidad: {self.cantidad}"
        )