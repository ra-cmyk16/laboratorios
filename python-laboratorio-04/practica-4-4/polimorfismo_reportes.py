# polimorfismo_reportes.py
class ReporteTexto:
    def generar(self, datos):
        return f"Reporte en Texto - Datos incluidos: {datos}"


class ReporteResumen:
    def generar(self, datos):
        return f"Reporte Resumen - Cantidad total de registros: {len(datos)}"


if __name__ == "__main__":
    datos_prueba = ["Teclado", "Mouse", "Monitor", "Audífonos"]
    reportes = [ReporteTexto(), ReporteResumen()]

    for reporte in reportes:
        print(reporte.generar(datos_prueba))