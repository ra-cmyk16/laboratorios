try:
    dividendo = float(input("Dividendo: "))
    divisor = float(input("Divisor: "))
except ValueError:
    print("Debes escribir números.")
else:
    if divisor == 0:
        print("No se puede dividir entre cero.")
    else:
        print("Resultado:", dividendo / divisor)
