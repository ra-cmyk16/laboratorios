import json
from pathlib import Path

# JSON corregido (se añade la coma omitida entre los dos objetos)
json_corregido_texto = """[
  {"codigo": "P001", "nombre": "Teclado"},
  {"codigo": "P002", "nombre": "Mouse"}
]"""

ruta = Path("productos_corregido.json")
with ruta.open("w", encoding="utf-8") as archivo:
    archivo.write(json_corregido_texto)

try:
    with ruta.open("r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    print("El JSON fue corregido exitosamente. Contenido cargado:")
    for prod in datos:
        print(" -", prod["codigo"], prod["nombre"])
except json.JSONDecodeError as e:
    print("Error al interpretar JSON:", e)