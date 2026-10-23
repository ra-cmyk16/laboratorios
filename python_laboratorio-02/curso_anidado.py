curso = {
    "nombre": "Programación en Python",
    "codigo": "PY101",
    "temas": ["Variables", "Listas", "Diccionarios"],
    "instructor": {
        "nombre": "Carlos",
        "correo": "carlos@ejemplo.com"
    }
}

print("Nombre del curso:", curso["nombre"])
print("Segundo tema:", curso["temas"][1])
print("Nombre del instructor:", curso["instructor"]["nombre"])
print("Cantidad de temas:", len(curso["temas"]))
#Buscar un producto por código
print()
codigo_buscado = input("Código: ").strip()
encontrado = False

for producto in productos:
    if producto["codigo"] == codigo_buscado:
        print("Encontrado:", producto["nombre"])
        encontrado = True
        break

if not encontrado:
    print("No se encontró el producto.")

#Depuración — Clave inexistente
print()
producto = {"codigo": "P001", "nombre": "Teclado"}

print("Precio:", producto.get("precio", "No registrado"))