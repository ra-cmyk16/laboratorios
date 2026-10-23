opcion = ""

while opcion != "0":
    print()
    print("1. Saludar")
    print("2. Mostrar mensaje")
    print("0. Salir")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        print("Hola.")
    elif opcion == "2":
        print("El programa sigue ejecutándose.")
    elif opcion == "0":
        print("Programa terminado.")
    else:
        print("Opción no válida.")

#Depuracion
numero = 1

while numero <= 5:
    print(numero)
    numero += 1

"""La variable que controla el ciclo es numero;
no la variable no cambia, no la condicion no dejara de cumplirse"""
