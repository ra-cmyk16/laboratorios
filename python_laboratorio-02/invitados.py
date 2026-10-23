invitados = []

for i in range(5):
    nombre = input("Ingresa el nombre del invitado: ")
    invitados.append(nombre)

print("Cantidad de invitados:", len(invitados))
print("Lista de invitados:", invitados)

#Recorrer una lista
print()
productos = ["Teclado", "Mouse", "Monitor"]

for producto in productos:
    print("Producto:", producto)
for posicion, producto in enumerate(productos, start=1):
    print(posicion, "-", producto)