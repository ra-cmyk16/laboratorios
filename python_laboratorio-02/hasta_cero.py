contador = 0
numero = int(input("Número: "))

while numero != 0:
    contador += 1
    numero = int(input("Número: "))

print("Programa terminado.")
print(f"Se ingresaron {contador} números diferentes de cero.")
