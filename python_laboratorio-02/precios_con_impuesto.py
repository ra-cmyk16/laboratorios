precios = [10000, 20000, 50000, 80000]

precios_con_for = []

for precio in precios:
    precios_con_for.append(precio * 1.19)

precios_con_comprension = [precio * 1.19 for precio in precios]

print("Precios con for:", precios_con_for)
print("Precios con comprensión:", precios_con_comprension)

print("¿Los resultados son equivalentes?:", precios_con_for == precios_con_comprension)