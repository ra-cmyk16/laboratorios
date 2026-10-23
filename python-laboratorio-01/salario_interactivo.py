#Ejercicio — Salario interactivo
nombre = str(input("Escribe tu nombre: "))
horas_trabajadas = int(input("Escribe las horas trabajadas: "))
valor_horas = int(input("Escribe el valor de tus horas en dolares: "))
total = horas_trabajadas * valor_horas
print("------------------------")
print("RESUMEN DE PAGO")
print("------------------------")
print(f"Trabajador/a {nombre}")
print(f"Horas: {horas_trabajadas}")
print(f"Valor por hora: {valor_horas}")
print(f"Pago total: ${total}")