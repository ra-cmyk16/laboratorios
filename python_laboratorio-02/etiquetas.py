etiquetas = ["Python", "HTML", "CSS", "Python", "Java", "CSS", "Python"]

print("Registros originales:", len(etiquetas))
print("Etiquetas diferentes:", len(set(etiquetas)))
#Agregar y eliminar elementos
print()
categorias = {"Periféricos", "Accesorios"}

categorias.add("Componentes")
categorias.update(["Papelería", "Accesorios"])

print(categorias)

categorias.discard("Papelería")
print(categorias)