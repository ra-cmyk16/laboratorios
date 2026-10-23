edad = int(input("Escribe tu edad: "))

if edad >= 18:
    print("Puede ingresar")
else:
    autorizacion = input("Escribe Si o No si tienes autorizacion: ").strip().lower()
    if autorizacion == "si":
        print("Puede ingresar")
    else:
        print("No puede ingresar")
