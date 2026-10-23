import csv
from pathlib import Path

# Ejercicio — Exportación de ventas
ventas = [
    {"codigo": "V001", "producto": "Teclado", "cantidad": 2, "total": 170000},
    {"codigo": "V002", "producto": "Mouse", "cantidad": 1, "total": 45000},
    {"codigo": "V003", "producto": "Monitor", "cantidad": 1, "total": 750000},
    {"codigo": "V004", "producto": "Audífonos", "cantidad": 3, "total": 180000}
]

ruta = Path("ventas.csv")

# Exportar CSV
with ruta.open("w", newline="", encoding="utf-8") as archivo:
    campos = ["codigo", "producto", "cantidad", "total"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(ventas)

print("Ventas exportadas exitosamente a ventas.csv.")

# Leer y calcular total
total_acumulado = 0.0
total_unidades = 0

with ruta.open("r", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    print("\n=== Detalle de Ventas Leídas ===")
    for fila in lector:
        cant = int(fila["cantidad"])
        monto = float(fila["total"])
        total_unidades += cant
        total_acumulado += monto
        print(f"Venta {fila['codigo']}: {fila['producto']} | Cantidad: {cant} | Total: ${monto:,.2f}")

print(f"\nTotal acumulado de ventas: ${total_acumulado:,.2f}")
print(f"Total unidades vendidas: {total_unidades}")