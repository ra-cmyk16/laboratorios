from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_HISTORIAL = BASE_DIR / "operaciones.txt"


def registrar_operacion():
    concepto = input("Concepto: ").strip()
    if concepto == "":
        print("El concepto es obligatorio.")
        return

    try:
        valor = float(input("Valor: "))
    except ValueError:
        print("El valor debe ser un número.")
        return

    with open(RUTA_HISTORIAL, "a", encoding="utf-8") as archivo:
        archivo.write(concepto + ";" + str(valor) + "\n")
    print("Operación registrada.")


def mostrar_historial():
    try:
        with open(RUTA_HISTORIAL, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print("Todavía no hay operaciones registradas.")
        return

    if len(lineas) == 0:
        print("Todavía no hay operaciones registradas.")
        return

    print("Historial de operaciones:")
    for numero, linea in enumerate(lineas, start=1):
        concepto, valor = linea.strip().rsplit(";", 1)
        print(numero, "-", concepto, ":", valor)


while True:
    print()
    print("1. Registrar operación")
    print("2. Mostrar historial")
    print("0. Salir")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        registrar_operacion()
    elif opcion == "2":
        mostrar_historial()
    elif opcion == "0":
        print("Fin del programa.")
        break
    else:
        print("Opción no válida.")
