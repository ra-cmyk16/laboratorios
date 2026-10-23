import json
from pathlib import Path

def cargar_productos_protegido(ruta_path: Path):
    """
    Carga productos desde un archivo JSON respetando los 3 escenarios:
    1. Si el archivo no existe: devuelve lista vacía.
    2. Si el archivo es válido: devuelve los datos.
    3. Si el archivo está dañado: captura JSONDecodeError y evita sobrescribir.
    """
    if not ruta_path.exists():
        print(f"El archivo '{ruta_path}' no existe aún. Iniciando lista vacía.")
        return []

    try:
        with ruta_path.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            print(f"Archivo '{ruta_path}' cargado correctamente.")
            return datos
    except json.JSONDecodeError as e:
        print(f"ERROR: El archivo '{ruta_path}' está dañado o no tiene formato JSON válido.")
        print(f"Detalle: {e}")
        print("PROTECCIÓN: No se sobrescribirá el archivo para prevenir pérdida de datos.")
        return None

if __name__ == "__main__":
    ruta_normal = Path("productos.json")
    print("=== Escenario 1: Archivo normal ===")
    prods = cargar_productos_protegido(ruta_normal)
    
    ruta_inexistente = Path("no_existe.json")
    print("\n=== Escenario 2: Archivo inexistente ===")
    prods_inex = cargar_productos_protegido(ruta_inexistente)

    ruta_danada = Path("productos_danado.json")
    with ruta_danada.open("w", encoding="utf-8") as f:
        f.write('[{"codigo": "P001", "nombre": "Teclado"}\n {"codigo": "P002"}]') # Falta coma

    print("\n=== Escenario 3: Archivo dañado ===")
    prods_danados = cargar_productos_protegido(ruta_danada)