from pathlib import Path

# La ruta se calcula a partir de la ubicación de este archivo,
# no de la carpeta desde donde se ejecuta Python.
BASE_DIR = Path(__file__).resolve().parent
RUTA_DATOS = BASE_DIR / "datos" / "inventario.txt"

RUTA_DATOS.parent.mkdir(parents=True, exist_ok=True)
RUTA_DATOS.write_text("Datos del proyecto\n", encoding="utf-8")

print(RUTA_DATOS)
