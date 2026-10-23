# depuracion_super.py
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, group_id):
        # Explicación del error original:
        # El código original fallaba porque el inicializador (__init__) de Student sobrescribía
        # al de Person sin invocar a super().__init__(name). Por lo tanto, el atributo 'name'
        # nunca llegaba a inicializarse en la instancia, generando un AttributeError al intentar consultarlo.
        super().__init__(name)
        self.group_id = group_id


if __name__ == "__main__":
    student = Student("Carlos", "G-101")
    print(f"Nombre del estudiante: {student.name}")
    print(f"Grupo: {student.group_id}")