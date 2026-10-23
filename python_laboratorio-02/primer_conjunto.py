categorias = {"Periféricos", "Accesorios", "Componentes", "Periféricos"}

print(categorias)
print("Cantidad:", len(categorias))
#Crear un conjunto vacío
print()
vacio = set()
otro = {}

print(type(vacio))
print(type(otro))
#Eliminar duplicados de una lista
print()
ciudades = ["Bogotá", "Cali", "Bogotá", "Medellín", "Cali"]
unicas = set(ciudades)

print("Total de registros:", len(ciudades))
print("Ciudades diferentes:", len(unicas))
print(unicas)
print()
lista_unicas = list(unicas)
print(lista_unicas)