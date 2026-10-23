import json
from pathlib import Path

from inventario import Inventario


BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "datos" / "productos.json"


class ErrorInventarioArchivo(Exception):
    """Indica que el archivo de inventario no se puede cargar."""


def guardar_inventario(inventario):
    RUTA_JSON.parent.mkdir(parents=True, exist_ok=True)

    datos = inventario.exportar_datos()
    ruta_temporal = RUTA_JSON.with_suffix(".tmp")

    try:
        with ruta_temporal.open("w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo,
                ensure_ascii=False,
                indent=4,
                allow_nan=False
            )

        # Reemplaza el archivo anterior solo después de escribir.
        ruta_temporal.replace(RUTA_JSON)
        return RUTA_JSON

    except (OSError, TypeError, ValueError) as error:
        try:
            if ruta_temporal.exists():
                ruta_temporal.unlink()
        except OSError:
            pass

        raise OSError(
            f"No se pudo guardar el inventario: {error}"
        ) from error


def cargar_inventario():
    inventario = Inventario()

    if not RUTA_JSON.exists():
        return inventario

    try:
        with RUTA_JSON.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        # La validación se hace antes de devolver el inventario.
        inventario.cargar_datos(datos)
        return inventario

    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        raise ErrorInventarioArchivo(
            f"No se pudo cargar el inventario: {error}"
        ) from error