import json

class Producto:
    def __init__(self, codigo, nombre, categoria="General", precio=0.0, cantidad=0):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

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
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos.get("categoria", "General"),
            datos.get("precio", 0.0),
            datos.get("cantidad", 0)
        )

# Demostración de serialización a JSON
p1 = Producto("P001", "Teclado Mechanical", "Periféricos", 85000.0, 4)
diccionario = p1.a_diccionario()
json_str = json.dumps(diccionario, ensure_ascii=False, indent=2)
print("Objeto convertido a JSON:")
print(json_str)

# Demostración de reconstrucción desde diccionario
datos_recuperados = json.loads(json_str)
p2 = Producto.desde_diccionario(datos_recuperados)
print("\nObjeto reconstruido:")
print(f"Tipo: {type(p2)}")
print(f"Código: {p2.codigo}, Nombre: {p2.nombre}, Precio: {p2.precio}")