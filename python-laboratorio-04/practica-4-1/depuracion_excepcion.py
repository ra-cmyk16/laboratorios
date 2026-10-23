# Versión original (con error): la excepción no se atendía porque
# int("hola") produce ValueError, no ZeroDivisionError.
#
#   try:
#       numero = int("hola")
#   except ZeroDivisionError:
#       print("No se pudo convertir.")
#
# Corrección: capturar el tipo de excepción que realmente ocurre.
try:
    numero = int("hola")
except ValueError:
    print("No se pudo convertir.")
