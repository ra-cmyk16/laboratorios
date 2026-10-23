import unidades

kilometros = float(input("Distancia en kilómetros: "))
celsius = float(input("Temperatura en °C: "))

metros = unidades.kilometros_a_metros(kilometros)
fahrenheit = unidades.celsius_a_fahrenheit(celsius)

print(kilometros, "km equivalen a", metros, "m")
print(celsius, "°C equivalen a", fahrenheit, "°F")
