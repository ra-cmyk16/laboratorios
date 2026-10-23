asignaturas = ["Matemáticas", "Programación", "Inglés", "Física", "Filosofía"]

for i in range(len(asignaturas)):
    print(i + 1, asignaturas[i])

asignaturas.append("Base de datos")

print("\nLista actualizada:")

for i in range(len(asignaturas)):
    print(i + 1, asignaturas[i])
    
#Buscar un valor con in
print()
productos = ["Teclado", "Mouse", "Monitor"]

buscado = input("Buscar producto: ").strip()

if buscado in productos:
    print("Producto encontrado.")
else:
    print("Producto no registrado.")