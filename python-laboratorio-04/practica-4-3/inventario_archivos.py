import json
import csv
from pathlib import Path

RUTA_JSON = Path("inventario.json")
RUTA_CSV = Path("inventario.csv")

def guardar_json(productos, ruta=RUTA_JSON):
    with ruta.open("w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)
    print(f"Inventario guardado en '{ruta}'.")

def cargar_json(ruta=RUTA_JSON):
    if not ruta.exists():
        print(f"El archivo '{ruta}' no existe. Se iniciará un inventario nuevo.")
        return []

    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            productos = json.load(archivo)
            print(f"Inventario recuperado exitosamente desde '{ruta}'.")
            return productos
    except json.JSONDecodeError as e:
        print(f"ERROR: El archivo '{ruta}' está dañado.")
        print("El programa NO reemplazará el archivo por una lista vacía.")
        return None

def exportar_csv(productos, ruta=RUTA_CSV):
    if not productos:
        print("No hay productos para exportar.")
        return

    campos = ["codigo", "nombre", "precio", "cantidad"]
    with ruta.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(productos)
    print(f"Reporte de inventario exportado a '{ruta}'.")

if __name__ == "__main__":
    print("=== Carga Inicial ===")
    inventario = cargar_json()

    if inventario is None:
        print("Por favor revise el archivo JSON manualmente.")
    else:
        if not inventario:
            print("Cargando datos iniciales...")
            inventario = [
                {"codigo": "P001", "nombre": "Teclado RGB", "precio": 120000, "cantidad": 10},
                {"codigo": "P002", "nombre": "Mouse Inalámbrico", "precio": 65000, "cantidad": 15},
                {"codigo": "P003", "nombre": "Monitor 24 pulg", "precio": 600000, "cantidad": 5}
            ]
            guardar_json(inventario)

        print(f"\nProductos en inventario: {len(inventario)}")
        for p in inventario:
            print(f" - [{p['codigo']}] {p['nombre']} | Precio: ${p['precio']} | Stock: {p['cantidad']}")

        exportar_csv(inventario)