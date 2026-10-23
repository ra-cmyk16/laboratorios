try:
    edad = int(input("Edad: "))
except ValueError:
    print("La edad debe ser un número entero.")
else:
    if edad < 0:
        print("La edad no puede ser negativa.")
    elif edad > 120:
        print("La edad no puede ser superior a 120.")
    else:
        print("Edad aceptada:", edad)
