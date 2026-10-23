valor_compra = float(input("Escribe el valor de la compra: "))
if valor_compra >= 200000:
    costo_envio = 0
elif valor_compra >= 100000:
    costo_envio = 10000
else:
    costo_envio = 18000

mostrar_costo = "gratis" if costo_envio == 0 else f"{costo_envio}"

total = valor_compra + costo_envio

print("======================")
print("    COSTO DE ENVIO    ")
print("======================")
print()
print(f"Valor de la compra: ${valor_compra}")
print(f"Costo de envio: ${costo_envio}")
print(f"Total a pagar: ${total}")

"""El = asigna valores, el == los compara, 
la indentación estructura los bloques de código, 
el elif evalúa una nueva condición si las 
anteriores fallan, y el orden importa 
porque el programa ejecuta la primera condición 
verdadera que encuentra de arriba hacia abajo y 
descarta las demás."""