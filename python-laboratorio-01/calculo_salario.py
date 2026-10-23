#Ejercicio — Cálculo de salario
nombre_trabajador = "Ernesto Diaz"
horas_trabajadas = 20
valor_por_hora = 5
APORTE = 0.04
aporte = APORTE * 100
salario_bruto = horas_trabajadas * valor_por_hora
aporte_salario = salario_bruto * APORTE
salario_neto = salario_bruto - aporte_salario

print("------------------")
print("SALARIO TRABAJADOR")
print("------------------")
print(f"Nombre trabajador: {nombre_trabajador}")
print(f"Horas trabajadas {horas_trabajadas}")
print(f"Valor por hora: ${valor_por_hora}")
print(f"Aporte:  {aporte}%")
print(f"Salario bruto :${salario_bruto}\nSalario neto :${salario_neto}")
#Antes de ejecutar — Lee el cálculo
print()
unidades = 4
precio = 25000.0
descuento = 0.20

subtotal = unidades * precio
valor_descuento = subtotal * descuento
total = subtotal - valor_descuento

print(total)