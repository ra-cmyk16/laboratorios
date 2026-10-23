grupo1 = ["Ana", "Carlos", "Laura", "Ana"]
grupo2 = ["Carlos", "Pedro", "Laura", "Sofía"]

participantes = set(grupo1 + grupo2)

print("Personas diferentes:", len(participantes))
print("Participantes:", participantes)

participantes.add("Andrés")
print("Después de agregar a Andrés:", participantes)

participantes.discard("Pedro")
print("Después de eliminar a Pedro:", participantes)
#Operaciones entre conjuntos
print()
grupo_a = {"Ana", "Carlos", "Laura", "Sara"}
grupo_b = {"Laura", "Sara", "David", "Pablo"}
print("Unión:", grupo_a | grupo_b)
print("Intersección:", grupo_a & grupo_b)
print("Solo A:", grupo_a - grupo_b)
print("Diferencia simétrica:", grupo_a ^ grupo_b)
#Antes de ejecutar
"""
Antes de ejecutar — Predice

- Unión (grupo_a | grupo_b):
  Respuesta: {"Ana", "Carlos", "Laura", "Sara", "David", "Pablo"}

- Intersección (grupo_a & grupo_b):
  Respuesta: {"Laura", "Sara"}

- Solo A (grupo_a - grupo_b):
  Respuesta: {"Ana", "Carlos"}

- Diferencia simétrica (grupo_a ^ grupo_b):
  Respuesta: {"Ana", "Carlos", "David", "Pablo"}
"""