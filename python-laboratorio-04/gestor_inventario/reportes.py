import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "reportes" / "inventario.csv"


def exportar_csv(inventario):
    RUTA_CSV.parent.mkdir(parents=True, exist_ok=True)

    campos = [
        "codigo",
        "nombre",
        "categoria",
        "precio",
        "cantidad",
        "valor_inventario"
    ]

    ruta_temporal = RUTA_CSV.with_suffix(".tmp")

    try:
        with ruta_temporal.open(
            "w",
            newline="",
            encoding="utf-8"
        ) as archivo:
            escritor = csv.DictWriter(
                archivo,
                fieldnames=campos
            )

            escritor.writeheader()

            for producto in inventario.listar_productos():
                escritor.writerow({
                    "codigo": producto.codigo,
                    "nombre": producto.nombre,
                    "categoria": producto.categoria,
                    "precio": producto.precio,
                    "cantidad": producto.cantidad,
                    "valor_inventario": producto.calcular_valor()
                })

        ruta_temporal.replace(RUTA_CSV)
        return RUTA_CSV

    except OSError as error:
        try:
            if ruta_temporal.exists():
                ruta_temporal.unlink()
        except OSError:
            pass

        raise OSError(
            f"No se pudo exportar el reporte: {error}"
        ) from error