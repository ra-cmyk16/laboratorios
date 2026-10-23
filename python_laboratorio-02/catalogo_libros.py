libros = [
    {"codigo": "L001", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"codigo": "L002", "titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "anio": 1943},
    {"codigo": "L003", "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "anio": 1605}
]

codigo_buscar = input("Ingrese el código del libro que desea buscar: ")
encontrado = False

for libro in libros:
    if libro["codigo"] == codigo_buscar:
        print("Libro encontrado:")
        print("Código:", libro["codigo"])
        print("Título:", libro["titulo"])
        print("Autor:", libro["autor"])
        print("Año:", libro["anio"])
        encontrado = True

if not encontrado:
    print("El libro no fue localizado.")

nuevo_codigo = input("Ingrese el código del nuevo libro: ")

codigo_repetido = False

for libro in libros:
    if libro["codigo"] == nuevo_codigo:
        codigo_repetido = True

if codigo_repetido:
    print("No se puede agregar el libro porque el código ya existe.")
else:
    nuevo_titulo = input("Ingrese el título: ")
    nuevo_autor = input("Ingrese el autor: ")
    nuevo_anio = int(input("Ingrese el año de publicación: "))

    nuevo_libro = {
        "codigo": nuevo_codigo,
        "titulo": nuevo_titulo,
        "autor": nuevo_autor,
        "anio": nuevo_anio
    }

    libros.append(nuevo_libro)
    print("Libro agregado correctamente.")

print("Catálogo de libros:")

for libro in libros:
    print(libro)

"""
Comprobación

1. ¿Cuándo necesitas una lista?
Cuando necesitas guardar varios elementos en una sola variable y recorrerlos o modificarlos.

2. ¿Cuándo necesitas un diccionario?
Cuando necesitas guardar datos relacionados mediante claves y valores, por ejemplo, el título y el autor de un libro.

3. ¿Por qué una lista de diccionarios permite manejar varios registros con estructura similar?
Porque la lista almacena varios libros y cada diccionario guarda los datos de un libro usando las mismas claves.
"""