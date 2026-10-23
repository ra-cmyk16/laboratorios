esta_inscrito = False
tiene_documento = True

if esta_inscrito and tiene_documento:
    print("Puede ingresar.")
else:
    print("No cumple todos los requisitos.")

tiene_carnet = False
tiene_autorizacion = False

if tiene_carnet or tiene_autorizacion:
    print("Puede ingresar.")
else:
    print("No puede ingresar.")    

bloqueado = True

if not bloqueado:
    print("La cuenta está habilitada.")
else:
    print("La cuenta está bloqueada.")

"""
ANTES DE EJECUTAR
FALSE
TRUE
FALSE 
FALSE
"""        
edad = 17
acompanado = True

print(edad >= 18)
print(edad >= 18 or acompanado)
print(edad >= 18 and acompanado)
print(not acompanado)