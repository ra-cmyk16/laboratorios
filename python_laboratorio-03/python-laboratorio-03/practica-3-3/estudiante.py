class Estudiante:
    def __init__(self, nombre, ficha, promedio):
        self.nombre = nombre
        self.ficha = ficha
        self.promedio = promedio

    def mostrar_perfil(self):
        print("Nombre:", self.nombre)
        print("Ficha:", self.ficha)
        print("Promedio:", self.promedio)

    def aprobo(self):
        return self.promedio >= 3.0


estudiante_1 = Estudiante("Laura", "2900001", 2.8)
estudiante_2 = Estudiante("Andrés", "2900002", 4.1)

estudiante_1.mostrar_perfil()
print("¿Aprobó?", estudiante_1.aprobo())

print()

estudiante_2.mostrar_perfil()
print("¿Aprobó?", estudiante_2.aprobo())
