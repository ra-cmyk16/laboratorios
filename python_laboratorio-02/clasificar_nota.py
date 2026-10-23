nota = float(input("Nota: "))

if nota >= 4.5:
    print("Desempeño sobresaliente")
elif nota >= 4.0:
    print("Desempeño alto")
elif nota >= 3.0:
    print("Aprobado")
else:
    print("No aprobado")
"""Comparar texto(Para normalizar el texto 
se utiliza strip(elimina espacios al inicio y 
final) y lower(convierte el texto en minusculas))"""
print()
respuesta = input("Escribe SI para continuar: ").strip().lower()

if respuesta == "si":
    print("Continuando...")
else:
    print("Respuesta diferente de SI.")