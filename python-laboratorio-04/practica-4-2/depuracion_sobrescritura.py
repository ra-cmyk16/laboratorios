from pathlib import Path

# Con write_text() solo quedaba el "Registro 2", porque cada llamada
# reemplaza todo el contenido anterior.
# Corrección: abrir en modo "a" para agregar al final.
ruta = Path("historial.txt")

with open(ruta, "w", encoding="utf-8") as archivo:
    archivo.write("Registro 1\n")

with open(ruta, "a", encoding="utf-8") as archivo:
    archivo.write("Registro 2\n")

print(ruta.read_text(encoding="utf-8"))
