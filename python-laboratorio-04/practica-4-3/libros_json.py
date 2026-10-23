import json
from pathlib import Path

# Ejercicio — Catálogo de libros
libros = [
    {"codigo": "L001", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"codigo": "L002", "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "anio": 1605},
    {"codigo": "L003", "titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "anio": 1943}
]

ruta = Path("libros.json")

# Escritura de catálogo
with ruta.open("w", encoding="utf-8") as archivo:
    json.dump(libros, archivo, ensure_ascii=False, indent=4)

print("Catálogo de libros guardado en libros.json.")

# Lectura de catálogo
with ruta.open("r", encoding="utf-8") as archivo:
    libros_cargados = json.load(archivo)

print("\nLibros cargados desde el archivo:")
for libro in libros_cargados:
    print(f"[{libro['codigo']}] {libro['titulo']} - {libro['autor']} ({libro['anio']})")