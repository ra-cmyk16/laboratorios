edad = int(input("Escribe tu edad: "))
edad = int(input("Ingresa tu edad: "))
respuesta_inscrito = input("¿Estás inscrito? (SI/NO): ").strip().lower()
num_doc = int(input("Ingresa el número de documentos entregados: "))

esta_inscrito = (respuesta_inscrito == "si")
errores = []

if edad < 16:
    errores.append("- Debes tener al menos 16 años.")

if not esta_inscrito:
    errores.append("- Debes estar inscrito en el sistema.")

if num_doc < 3:
    errores.append("- Se requieren al menos 3 documentos entregados.")

print("\n--- RESULTADO DE LA EVALUACIÓN ---")
if len(errores) == 0:
    print("¡Felicidades! La solicitud cumple todos los requisitos.")
else:
    print("La solicitud NO cumple con los requisitos. Faltan las siguientes observaciones:")
    for error in errores:
        print(error)

"""La diferencia entre and y or es que and requiere que las dos condiciones se cumpla
y or necesita que solo una se cumpla, y se necesita validar datos para evitar errores"""