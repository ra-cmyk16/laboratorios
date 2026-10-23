#Todo lo que entra con input() comienza como texto
edad = input("Edad: ")

print(edad)
print(type(edad))
#Convertir la entrada
print()
edad = int(input("Edad:"))
año_siguiente = edad + 1

print(f"El proximo año tendras {año_siguiente} años")
