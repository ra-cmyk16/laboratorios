tareas = []

opcion = ""

while opcion != "0":
    print("\n1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Consultar cantidad")
    print("0. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tarea = input("Escribe la tarea: ")

        if tarea == "":
            print("La tarea no puede estar vacía.")
        else:
            tareas.append(tarea)
            print("Tarea agregada correctamente.")

    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas registradas.")
        else:
            print("Lista de tareas:")
            for i in range(len(tareas)):
                print(i + 1, "-", tareas[i])

    elif opcion == "3":
        print("Cantidad de tareas:", len(tareas))

    elif opcion == "0":
        print("Saliendo del programa.")

    else:
        print("Opción desconocida. Intenta nuevamente.")

"""
Comprobación

- ¿Por qué una lista resulta más útil que varias variables separadas?
  Porque permite almacenar y administrar varios elementos en una sola variable.

- ¿Qué hace append()?
  Agrega un elemento al final de una lista.

- ¿Qué devuelve len()?
  Devuelve la cantidad de elementos de una lista.

- ¿Cómo se recorre una lista con for?
  Utilizando un ciclo for que permite acceder a cada elemento de la lista.

- ¿Qué comprueba in?
  Comprueba si un elemento existe dentro de una lista.

- ¿Por qué conviene verificar un elemento antes de aplicar remove()?
  Porque remove() genera un error si el elemento no existe en la lista.
"""