numeros = [1, 2, 3, 4, 5]
cuadrados = []

for numero in numeros:
    cuadrados.append(numero ** 2)

print(cuadrados)
#La misma operación con una comprensión
print()
numeros = [1, 2, 3, 4, 5]
cuadrados = [numero ** 2 for numero in numeros]

print(cuadrados)
#Forma general
#nueva_lista = [expresion for elemento in coleccion]