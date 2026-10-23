perfil = {
    "ficha": 1103,
    "nombre": "Rafael",
    "trimestre": 1,
    "promedio": 4.2,
    "activo": True
}

print("Nombre:", perfil["nombre"])

perfil["trimestre"] = 2

perfil["correo"] = "rafael@ejemplo.com"

print("Perfil actualizado:", perfil)
#Recorrer un diccionario
print()
producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000.0
}

for clave in producto:
    print(clave)

for valor in producto.values():
    print(valor)

for clave, valor in producto.items():
    print(clave, ":", valor)

#Eliminar y actualizar
print()
   producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000.0,
    "cantidad": 4
}

producto.update({"precio": 80000.0, "cantidad": 5})
cantidad_eliminada = producto.pop("cantidad")

print(producto)
print("Cantidad eliminada:", cantidad_eliminada) 