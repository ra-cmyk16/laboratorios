nombre = input("Nombre de la prueba: ")
resultado = input("Resultado (aprobada/fallida): ")
observacion = input("Observación breve: ")

with open("pruebas.txt", "a", encoding="utf-8") as archivo:
    archivo.write(nombre + " | " + resultado + " | " + observacion + "\n")

print("Prueba registrada en pruebas.txt")
