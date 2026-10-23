def duplicar(numero):
    resultado = numero * 2
    return resultado


doble = duplicar(8)
print(doble)

# print(resultado)
# Esta línea produce NameError: "resultado" es una variable local de duplicar().
# Fuera de la función se usa el valor devuelto, guardado en "doble".
