calificaciones = [3.5, 4.0, 2.8, 5.0, 3.5, 4.2]

print("Tres primeras:", calificaciones[:3])
print("Dos últimas:", calificaciones[-2:])
print("Cantidad total:", len(calificaciones))
print("Notas ordenadas:", sorted(calificaciones))
print("Veces que aparece 3.5:", calificaciones.count(3.5))
print("Orden original:", calificaciones)

#Depuración — Índice inexistente
print()
productos = ["Teclado", "Mouse", "Monitor"]

print("Cantidad de elementos:", len(productos))
print("Índice del último elemento:", len(productos) - 1)
print("Último elemento:", productos[2])
"""
Cantidad de elementos: 3.
Índice del último elemento: 2.
"""