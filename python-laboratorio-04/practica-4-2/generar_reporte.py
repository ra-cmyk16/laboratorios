from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
carpeta = BASE_DIR / "reportes"
carpeta.mkdir(parents=True, exist_ok=True)

ruta = carpeta / "resumen.txt"
ruta.write_text(
    "Resumen del inventario\n"
    "Total de productos: 3\n"
    "Reporte generado desde Python\n",
    encoding="utf-8",
)

print("Contenido del reporte:")
print(ruta.read_text(encoding="utf-8"))
print("Ruta del archivo:", ruta)
