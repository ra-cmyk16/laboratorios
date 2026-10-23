python = {"Ana", "Carlos", "Laura", "Sara", "Pedro"}
java = {"Laura", "Sara", "David", "Pablo", "Pedro"}

print("Inscritos en al menos uno:", python | java)
print("Inscritos en ambos:", python & java)
print("Únicamente en Python:", python - java)
print("Únicamente en Java:", java - python)
print("Inscritos en un solo taller:", python ^ java)

"""
Comprobación

- Valores únicos y valores que pueden repetirse:
  Los conjuntos almacenan valores únicos y eliminan los repetidos.
  Las listas permiten almacenar valores repetidos.

- {} y set():
  {} crea un diccionario vacío, mientras que set() crea
  un conjunto vacío.

- remove() y discard():
  remove() genera un error si el elemento no existe.
  discard() no genera un error si el elemento no existe.

- Unión e intersección:
  La unión reúne los elementos de ambos conjuntos sin repetirlos.
  La intersección devuelve únicamente los elementos compartidos.
"""