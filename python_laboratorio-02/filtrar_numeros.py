numeros = [3, 8, 12, 5, 20, 7]

mayores = [numero for numero in numeros if numero >= 10]

print(mayores)
#Ejercicio — Notas aprobadas
print()
notas = [2.5, 3.0, 4.8, 1.9, 3.7, 5.0]

notas_aprobadas = [nota for nota in notas if nota >= 3.0]

notas_inferiores = [nota for nota in notas if nota < 3.0]

notas_multiplicadas = [nota * 2 for nota in notas]

print("Notas aprobadas:", notas_aprobadas)
print("Notas inferiores a 3.0:", notas_inferiores)
print("Notas multiplicadas por 2:", notas_multiplicadas)
#Transformar y filtrar al mismo tiempo
print()
nombres = ["  ana ", "CARLOS", " Laura ", ""]

normalizados = [
    nombre.strip().title()
    for nombre in nombres
    if nombre.strip() != ""
]

print(normalizados)