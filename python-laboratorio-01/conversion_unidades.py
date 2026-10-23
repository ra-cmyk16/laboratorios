#Reto — Conversión de unidades
distancia = float(input("Escribe una distancia en kilometros: "))
metros = distancia *  1000
centimetros = distancia * 100000
millas = distancia * 0.621371

print(f"Distancia: {distancia} km")
print(f"Distancia en metros: {metros} m")
print(f"Distancia en centimetros: {centimetros} cm")
print(f"Distancia en millas: {millas} mi")