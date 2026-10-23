# Gestor de inventario — Laboratorio 3.5

## Archivos
- `main.py`: menú e interacción con el usuario.
- `producto.py`: clase `Producto`, categorías, validaciones, propiedades y cálculo del valor.
- `inventario.py`: clase `Inventario`, registro, búsqueda, actualización, eliminación e informes.
- `pruebas_independencia.py`: comprueba que dos inventarios mantengan colecciones independientes.

## Ejecución
Abre una terminal en esta carpeta y ejecuta `python main.py`.
Para la prueba de independencia, ejecuta `python pruebas_independencia.py`.
No se necesitan bibliotecas externas.

## Preguntas: antes de programar
1. **¿Qué clase debe evitar los códigos repetidos?** `Inventario`, porque administra la colección y comprueba si el código ya existe.
2. **¿Qué clase debe comprobar que la cantidad sea válida?** `Producto`, porque controla las reglas de cada artículo y rechaza cantidades negativas.
3. **¿Qué clase calcula el valor de un producto?** `Producto`, mediante `calcular_valor()`, que multiplica el precio por la cantidad.
4. **¿Dónde debe utilizarse `input()`?** En `main.py`, porque es el archivo que interactúa con el usuario.
5. **¿Quién decide qué mensaje se muestra después de una operación?** `main.py`, porque interpreta el resultado y presenta el mensaje correspondiente.

## Responsabilidades
- `Producto` representa un artículo y valida sus datos.
- `Inventario` administra objetos `Producto`.
- `main.py` solicita datos, muestra el menú y presenta los resultados.

## Comprobación numérica del laboratorio
Registra estos productos:
- P001: Teclado, Periféricos, precio 85000, cantidad 4.
- P002: Mouse, Periféricos, precio 45000, cantidad 0.
- P003: Componente, Componentes, precio 700000, cantidad 2.

Resultados esperados:
- Productos registrados: 3.
- Unidades disponibles: 6.
- Valor del inventario: 1740000.
- Categorías utilizadas: 2.
- Producto sin stock: Mouse.

Después de actualizar P002 a 5 unidades:
- Productos registrados: 3.
- Unidades disponibles: 11.
- Valor del inventario: 1965000.


