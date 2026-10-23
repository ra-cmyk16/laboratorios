# Práctica 3.1 — Funciones, parámetros, retorno y alcance


## 1. ¿Para qué sirve una función? — `primeras_funciones.py`

`practica-3-1/primeras_funciones.py`

```python
def mostrar_titulo():
    print("==========================")
    print("     INVENTARIO PYTHON")
    print("==========================")


mostrar_titulo()
print("Registro de productos")
mostrar_titulo()
```

**Predicción (antes de ejecutar):** la definición de `mostrar_titulo()` no imprime nada por sí sola. Al ejecutar aparecerá el título de tres líneas, luego `Registro de productos` y después otra vez el título de tres líneas.

**Resultado real:**

```text
==========================
     INVENTARIO PYTHON
==========================
Registro de productos
==========================
     INVENTARIO PYTHON
==========================
```

**Comparación:** **Coincide.** Se imprimieron 7 líneas: el título, `Registro de productos` y el título otra vez; definir la función no imprimió nada.

### Ejercicio — Encabezado y despedida — `mensajes.py`

`practica-3-1/mensajes.py`

```python
def mostrar_encabezado():
    print("==========================")
    print("     INVENTARIO PYTHON")
    print("==========================")


def mostrar_despedida():
    print("--------------------------")
    print("  Gracias por usar el programa")
    print("--------------------------")


mostrar_encabezado()
print("Registro de productos")
mostrar_encabezado()
print("Consulta de existencias")
mostrar_despedida()
```

El encabezado se usa dos veces y sus `print()` están escritos una sola vez, dentro de la función.

**Resultado real:**

```text
==========================
     INVENTARIO PYTHON
==========================
Registro de productos
==========================
     INVENTARIO PYTHON
==========================
Consulta de existencias
--------------------------
  Gracias por usar el programa
--------------------------
```

## 2. Parámetros y argumentos — `parametros.py`

`practica-3-1/parametros.py`

```python
def saludar(nombre):
    print(f"Hola, {nombre}")


def mostrar_producto(nombre, cantidad):
    print(f"Producto: {nombre}")
    print(f"Existencias: {cantidad}")


saludar("Laura")
saludar("Andrés")

mostrar_producto("Teclado", 4)
mostrar_producto("Mouse", 7)
```

**Resultado real:**

```text
Hola, Laura
Hola, Andrés
Producto: Teclado
Existencias: 4
Producto: Mouse
Existencias: 7
```

En `saludar(nombre)`, `nombre` es el **parámetro**; `"Laura"` y `"Andrés"` son **argumentos** de dos llamadas distintas. En `mostrar_producto(nombre, cantidad)` los argumentos se asignan por posición.

### Antes de ejecutar — Predice (`presentar`)

**Predicción (antes de ejecutar):** no habrá error. La primera llamada imprime `Ana vive en Bogotá`. La segunda llamada es una frase extraña: los argumentos se asignan por posición, así que `nombre = "Cali"` y `ciudad = "Luis"`, y se imprimirá `Cali vive en Luis`.

**Código original ejecutado:**

```python
def presentar(nombre, ciudad):
    print(f"{nombre} vive en {ciudad}")


presentar("Ana", "Bogotá")
presentar("Cali", "Luis")
```

**Resultado real:**

```text
Ana vive en Bogotá
Cali vive en Luis
```

**Comparación:** **Coincide.** No hubo error: la segunda llamada imprimió `Cali vive en Luis`, una frase extraña, porque los argumentos se asignan por posición (`nombre = "Cali"`, `ciudad = "Luis"`).

**Corrección:** se cambia el orden de los argumentos de la segunda llamada. Versión corregida (`presentar.py`):

`practica-3-1/presentar.py`

```python
def presentar(nombre, ciudad):
    print(f"{nombre} vive en {ciudad}")


presentar("Ana", "Bogotá")
presentar("Luis", "Cali")
```

```text
Ana vive en Bogotá
Luis vive en Cali
```

## 3. Devolver valores con `return` — `calculos.py` y `retorno_vs_print.py`

`practica-3-1/calculos.py`

```python
def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


resultado = calcular_subtotal(85000, 3)
print("Subtotal:", resultado)
```

```text
Subtotal: 255000
```

`practica-3-1/retorno_vs_print.py`

```python
def mostrar_total(precio, cantidad):
    print(precio * cantidad)


def obtener_total(precio, cantidad):
    return precio * cantidad


mostrar_total(10000, 3)
total = obtener_total(10000, 3)
print("Resultado reutilizable:", total)
```

**Predicción (antes de ejecutar):** `mostrar_total(10000, 3)` imprime `30000` por sí misma (su efecto visible es el `print`). `obtener_total(10000, 3)` no imprime nada: entrega el valor, que se guarda en `total`; luego se imprime `Resultado reutilizable: 30000`.

**Resultado real:**

```text
30000
Resultado reutilizable: 30000
```

**Comparación:** **Coincide.** `30000` lo imprime `mostrar_total()` por sí misma y `Resultado reutilizable: 30000` sale del valor que devolvió `obtener_total()`.

## 4. Una función sin `return` explícito — `sin_return.py`

`practica-3-1/sin_return.py`

```python
def anunciar():
    print("Operación iniciada")


resultado = anunciar()
print("Valor devuelto:", resultado)
```

**Predicción (antes de ejecutar):** se imprime `Operación iniciada` (lo hace la función) y después `Valor devuelto: None`, porque una función sin `return` devuelve `None`.

**Resultado real:**

```text
Operación iniciada
Valor devuelto: None
```

**Comparación:** **Coincide.** Se imprimió `Operación iniciada` y luego `Valor devuelto: None`.

### Depuración — Faltó devolver el dato — `error_retorno.py`

**Predicción (antes de ejecutar):** el programa no produce un error de Python, pero `print(total)` mostrará `None`, porque `sumar()` calcula `resultado` pero nunca lo devuelve.

**Código original ejecutado:**

```python
def sumar(a, b):
    resultado = a + b


total = sumar(10, 20)
print(total)
```

**Resultado real:**

```text
None
```

**Comparación:** **Coincide.** No hubo error de Python, pero se imprimió `None`, porque `sumar()` no devuelve nada.

**Corrección:** se agrega `return resultado` dentro de la función (sin reemplazar el cálculo por un valor fijo). Lo que se solucionó: ahora la llamada entrega el resultado y `total` guarda 30.

`practica-3-1/error_retorno.py`

```python
def sumar(a, b):
    resultado = a + b
    return resultado


total = sumar(10, 20)
print(total)
```

**Resultado real de la versión corregida:**

```text
30
```

### Ejercicio — Cotizador con funciones — `cotizador_funciones.py`

`practica-3-1/cotizador_funciones.py`

```python
def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


def calcular_descuento(subtotal, porcentaje):
    descuento = subtotal * porcentaje / 100
    return descuento


def calcular_impuesto(base, porcentaje):
    impuesto = base * porcentaje / 100
    return impuesto


precio = 100000
cantidad = 2
porcentaje_descuento = 10
porcentaje_impuesto = 19

subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal, porcentaje_descuento)
base = subtotal - descuento
impuesto = calcular_impuesto(base, porcentaje_impuesto)
total = base + impuesto

print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Base después del descuento:", base)
print("Impuesto:", impuesto)
print("Total:", total)
```

Cada resultado se guarda en una variable antes de imprimirse.

**Predicción (antes de ejecutar):** los valores deben coincidir con los del enunciado. Como la división `/` siempre devuelve un número decimal, el descuento, la base, el impuesto y el total se mostrarán con `.0` (por ejemplo `20000.0`); el valor es el mismo que `20000`. El subtotal será `200000` (entero × entero).

**Resultado real:**

```text
Subtotal: 200000
Descuento: 20000.0
Base después del descuento: 180000.0
Impuesto: 34200.0
Total: 214200.0
```

**Comparación:** **Coincide.** Subtotal `200000` (entero) y los demás valores con `.0` (`20000.0`, `180000.0`, `34200.0`, `214200.0`). Los valores numéricos son los del enunciado (`Descuento 20000`, `Base 180000`, `Impuesto 34200`, `Total 214200`).

## 5. Valores predeterminados y argumentos con nombre — `valores_predeterminados.py`

`practica-3-1/valores_predeterminados.py`

```python
def calcular_total(precio, cantidad, descuento=0):
    subtotal = precio * cantidad
    return subtotal - subtotal * descuento / 100


print(calcular_total(50000, 2))
print(calcular_total(50000, 2, 10))
print(calcular_total(precio=50000, cantidad=2, descuento=20))
```

**Predicción (antes de ejecutar):**

- `calcular_total(50000, 2)`: subtotal 100000; sin descuento (0) resta `100000 * 0 / 100 = 0.0`; como esa división da decimal, el resultado es `100000.0`.
- `calcular_total(50000, 2, 10)`: `100000 - 10000.0 = 90000.0`.
- `calcular_total(precio=50000, cantidad=2, descuento=20)`: `100000 - 20000.0 = 80000.0`.

**Resultado real:**

```text
100000.0
90000.0
80000.0
```

**Comparación:** **Coincide:** `100000.0`, `90000.0` y `80000.0`.

### Ejercicio — Costos de envío — `costos_envio.py`

`practica-3-1/costos_envio.py`

```python
def calcular_cobro(valor_compra, envio=10000):
    return valor_compra + envio


cobro_con_envio = calcular_cobro(80000)
cobro_envio_gratis = calcular_cobro(80000, envio=0)

print("Con envío predeterminado:", cobro_con_envio)
print("Con envío gratuito:", cobro_envio_gratis)
```

**Resultado real:**

```text
Con envío predeterminado: 90000
Con envío gratuito: 80000
```

La primera llamada usa el envío predeterminado (10000); la segunda lo reemplaza con un argumento con nombre (`envio=0`).

## 6. Alcance de las variables — `alcance.py`

`practica-3-1/alcance.py`

```python
def duplicar(numero):
    resultado = numero * 2
    return resultado


doble = duplicar(8)
print(doble)

# print(resultado)
# Esta línea produce NameError: "resultado" es una variable local de duplicar().
# Fuera de la función se usa el valor devuelto, guardado en "doble".
```

**Predicción (antes de ejecutar):** el programa original imprime `16`. Al agregar `print(resultado)` al final, aparecerá un `NameError`, porque `resultado` es una variable local de `duplicar()` y no existe fuera de la función.

**Código ejecutado con la línea adicional:**

```python
def duplicar(numero):
    resultado = numero * 2
    return resultado


doble = duplicar(8)
print(doble)
print(resultado)
```

**Resultado real:**

```text
16
Traceback (most recent call last):
  File "alcance_con_error.py", line 8, in <module>
    print(resultado)
          ^^^^^^^^^
NameError: name 'resultado' is not defined
```

**Comparación:** **Coincide.** Se imprimió `16` y después apareció `NameError: name 'resultado' is not defined`.

En el archivo entregado esa última línea quedó comentada para que el programa se pueda ejecutar completo. Resultado real del archivo entregado:

```text
16
```

## 7. Funciones y listas — `funciones_listas.py`

`practica-3-1/funciones_listas.py`

```python
def calcular_unidades(productos):
    total = 0

    for producto in productos:
        total += producto["cantidad"]

    return total


def agregar(nombre, nombres):
    nombres.append(nombre)


def agregar_en_copia(nombre, nombres):
    copia = nombres.copy()
    copia.append(nombre)
    return copia


inventario = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 7}
]

print(calcular_unidades(inventario))

productos = ["Teclado"]
agregar("Mouse", productos)

print(productos)

original = ["Teclado"]
nueva = agregar_en_copia("Mouse", original)

print("Original:", original)
print("Nueva:", nueva)
```

**Predicción (antes de ejecutar):** `11` (4 + 7). Luego `['Teclado', 'Mouse']`, porque `agregar()` modifica la misma lista que recibe. Por último `Original: ['Teclado']` y `Nueva: ['Teclado', 'Mouse']`, porque `agregar_en_copia()` trabaja con una copia.

**Resultado real:**

```text
11
['Teclado', 'Mouse']
Original: ['Teclado']
Nueva: ['Teclado', 'Mouse']
```

**Comparación:** **Coincide:** `11`, `['Teclado', 'Mouse']`, `Original: ['Teclado']` y `Nueva: ['Teclado', 'Mouse']`.

### Ejercicio — Consultas de inventario — `consultas_inventario.py`

`practica-3-1/consultas_inventario.py`

```python
def agotados(productos):
    nombres = []

    for producto in productos:
        if producto["cantidad"] == 0:
            nombres.append(producto["nombre"])

    return nombres


def agotados_comprension(productos):
    return [
        producto["nombre"]
        for producto in productos
        if producto["cantidad"] == 0
    ]


productos = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 0},
    {"nombre": "Monitor", "cantidad": 2},
    {"nombre": "Cámara", "cantidad": 0}
]

print("Con for y append():", agotados(productos))
print("Con comprensión:", agotados_comprension(productos))
```

Primero se resolvió con `for` y `append()` y luego con una comprensión de lista.

**Resultado real:**

```text
Con for y append(): ['Mouse', 'Cámara']
Con comprensión: ['Mouse', 'Cámara']
```

Ambas versiones devuelven los mismos nombres: `['Mouse', 'Cámara']`.

### Reto — Cuatro funciones sobre una colección — `inventario_funciones.py`

`practica-3-1/inventario_funciones.py`

```python
def mostrar_productos(productos):
    for producto in productos:
        print(
            producto["codigo"], "-",
            producto["nombre"], "-",
            "$", producto["precio"], "-",
            producto["cantidad"], "unidades"
        )


def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto

    return None


def valor_inventario(productos):
    total = 0

    for producto in productos:
        total += producto["precio"] * producto["cantidad"]

    return total


def productos_sin_stock(productos):
    return [
        producto["nombre"]
        for producto in productos
        if producto["cantidad"] == 0
    ]


productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000.0, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000.0, "cantidad": 0},
    {"codigo": "P003", "nombre": "Monitor", "precio": 700000.0, "cantidad": 2}
]

print("Productos registrados:")
mostrar_productos(productos)

print()
print("Buscar P003:", buscar_producto(productos, "P003"))
print("Buscar P999:", buscar_producto(productos, "P999"))

print()
print("Valor del inventario:", valor_inventario(productos))
print("Productos sin stock:", productos_sin_stock(productos))
```

**Predicción (antes de ejecutar):** se mostrarán los tres productos; `buscar_producto(..., "P003")` devolverá el diccionario del Monitor y con `"P999"` devolverá `None`; el valor del inventario será `85000×4 + 45000×0 + 700000×2 = 1740000.0` y los productos sin stock serán `['Mouse']`.

**Resultado real:**

```text
Productos registrados:
P001 - Teclado - $ 85000.0 - 4 unidades
P002 - Mouse - $ 45000.0 - 0 unidades
P003 - Monitor - $ 700000.0 - 2 unidades

Buscar P003: {'codigo': 'P003', 'nombre': 'Monitor', 'precio': 700000.0, 'cantidad': 2}
Buscar P999: None

Valor del inventario: 1740000.0
Productos sin stock: ['Mouse']
```

**Comparación:** **Coincide:** se mostraron los tres productos, `P003` devolvió su diccionario, `P999` devolvió `None`, el valor fue `1740000.0` y los productos sin stock fueron `['Mouse']`. (En el listado aparece `$ 85000.0` con un espacio después del `$` porque `print()` separa los argumentos con espacios.)

## Comprobación de la práctica 3.1

**¿Cuál es la diferencia entre `print()` y `return`?**
`print()` muestra un texto en la pantalla, pero no le entrega ningún valor al resto del programa (por eso la llamada devuelve `None`). `return` entrega un valor a quien llamó la función, que puede guardarlo en una variable y reutilizarlo, y además termina la función.

**¿Cuál es la diferencia entre parámetro y argumento?**
El parámetro es la variable que aparece en la definición de la función (`def saludar(nombre)`). El argumento es el valor concreto que se envía al llamarla (`saludar("Laura")`).

**¿Cuál es la diferencia entre modificar una lista que recibes y devolver una lista nueva?**
Si la función recibe una lista y le hace `append()`, cambia la lista original, porque la función y el programa principal usan el mismo objeto. Si la función hace una copia con `copy()`, modifica la copia y la devuelve, la lista original queda igual y el programa recibe una lista nueva.

---

# Práctica 3.2 — Módulos, importaciones y organización del código

Archivos en `practica-3-2/`. Cada ejercicio con varios archivos tiene su propia subcarpeta, porque en cada uno hay un `main.py` distinto. Cada programa se ejecuta desde la carpeta que contiene sus archivos (`python main.py`).

## 1. Primer proyecto con dos módulos — `operaciones/`

`operaciones/operaciones.py`:

`practica-3-2/operaciones/operaciones.py`

```python
def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    return subtotal * porcentaje / 100
```

`operaciones/main.py`:

`practica-3-2/operaciones/main.py`

```python
import operaciones

subtotal = operaciones.calcular_subtotal(85000, 3)
descuento = operaciones.calcular_descuento(subtotal, 10)

print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Total:", subtotal - descuento)
```

**Resultado esperado según el laboratorio:** `Subtotal: 255000`, `Descuento: 25500.0`, `Total: 229500.0`.

**Resultado real:**

```text
Subtotal: 255000
Descuento: 25500.0
Total: 229500.0
```

## 2. Importar funciones específicas — `operaciones/main_from_import.py`

`practica-3-2/operaciones/main_from_import.py`

```python
from operaciones import calcular_subtotal, calcular_descuento

subtotal = calcular_subtotal(40000, 2)
descuento = calcular_descuento(subtotal, 5)

print(subtotal - descuento)
```

**Predicción (antes de ejecutar):** subtotal `40000 × 2 = 80000`; descuento `80000 × 5 / 100 = 4000.0`; se imprime `80000 - 4000.0 = 76000.0`.

**Resultado real:**

```text
76000.0
```

**Comparación:** **Coincide:** `76000.0`.

### Ejercicio — Módulo de conversiones — `conversiones/`

`conversiones/unidades.py` solo hace cálculos (no usa `input()` ni `print()`):

`practica-3-2/conversiones/unidades.py`

```python
def kilometros_a_metros(kilometros):
    return kilometros * 1000


def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
```

`conversiones/main.py` pide los datos y muestra los resultados:

`practica-3-2/conversiones/main.py`

```python
import unidades

kilometros = float(input("Distancia en kilómetros: "))
celsius = float(input("Temperatura en °C: "))

metros = unidades.kilometros_a_metros(kilometros)
fahrenheit = unidades.celsius_a_fahrenheit(celsius)

print(kilometros, "km equivalen a", metros, "m")
print(celsius, "°C equivalen a", fahrenheit, "°F")
```

**Resultado real (primera ejecución):**

```text
Distancia en kilómetros: 2.5
Temperatura en °C: 25
2.5 km equivalen a 2500.0 m
25.0 °C equivalen a 77.0 °F
```

**Resultado real (segunda ejecución):**

```text
Distancia en kilómetros: 0
Temperatura en °C: 100
0.0 km equivalen a 0.0 m
100.0 °C equivalen a 212.0 °F
```

## 3. Código que se ejecuta al importar

Primero se creó `saludos.py` con un `print()` fuera de la función, y `main.py` que lo importa.

**Predicción (antes de ejecutar):** al ejecutar `main.py` aparecerá primero `Se ejecutó el módulo saludos.` (porque Python ejecuta el código de nivel superior del módulo al importarlo) y después `Hola, Laura`.

`saludos.py`

```python
def saludar(nombre):
    return f"Hola, {nombre}"


print("Se ejecutó el módulo saludos.")
```

`main.py`

```python
import saludos

print(saludos.saludar("Laura"))
```

**Resultado real:**

```text
Se ejecutó el módulo saludos.
Hola, Laura
```

**Comparación:** **Coincide.** Apareció `Se ejecutó el módulo saludos.` antes de `Hola, Laura`, porque al importar el módulo Python ejecuta su código de nivel superior.

## 4. El punto de entrada — `saludos/`

Se modificó `saludos.py` con `if __name__ == "__main__":` (carpeta `saludos/`).

`practica-3-2/saludos/saludos.py`

```python
def saludar(nombre):
    return f"Hola, {nombre}"


if __name__ == "__main__":
    print(saludar("Prueba"))
```

`practica-3-2/saludos/main.py`

```python
import saludos

print(saludos.saludar("Laura"))
```

**Predicción (antes de ejecutar):** al ejecutar `saludos.py` directamente se imprimirá `Hola, Prueba` (porque `__name__` vale `"__main__"`). Al ejecutar `main.py`, que lo importa, solo se imprimirá `Hola, Laura`: dentro de `saludos.py` `__name__` vale `"saludos"` y el bloque no se ejecuta.

**Resultado real al ejecutar `saludos.py`:**

```text
Hola, Prueba
```

**Resultado real al ejecutar `main.py`:**

```text
Hola, Laura
```

**Comparación:** **Coincide.** Ejecutando `saludos.py` aparece `Hola, Prueba`; ejecutando `main.py` solo aparece `Hola, Laura`.

### Antes de ejecutar — Predice (`predice_mensajes/`)

`practica-3-2/predice_mensajes/mensajes.py`

```python
def despedir():
    return "Hasta luego"


if __name__ == "__main__":
    print("Prueba directa")
```

`practica-3-2/predice_mensajes/main.py`

```python
from mensajes import despedir

print(despedir())
```

**Predicción (antes de ejecutar):**

- Al ejecutar `main.py` aparece solo `Hasta luego` (`main.py` importa `despedir`, y el bloque `__main__` de `mensajes.py` no se ejecuta al importar).
- Al ejecutar `mensajes.py` aparece solo `Prueba directa` (el bloque `__main__` sí se ejecuta, pero no se llama a `despedir()`).

**Resultado real al ejecutar `main.py`:**

```text
Hasta luego
```

**Resultado real al ejecutar `mensajes.py`:**

```text
Prueba directa
```

**Comparación:** **Coincide.** `main.py` muestra solo `Hasta luego` y `mensajes.py` muestra solo `Prueba directa`.

## 5. Separar las validaciones — `validaciones/`

`validaciones/validaciones.py` (incluye también el ejercicio **Categoría válida**):

`practica-3-2/validaciones/validaciones.py`

```python
def precio_valido(precio):
    return precio > 0


def cantidad_valida(cantidad):
    return cantidad >= 0


def nombre_valido(nombre):
    return nombre.strip() != ""


def categoria_valida(categoria, categorias):
    return categoria in categorias
```

`validaciones/main.py` (incluye la tupla `CATEGORIAS` y la comprobación de la categoría):

`practica-3-2/validaciones/main.py`

```python
import validaciones

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

nombre = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))
categoria = input("Categoría: ").strip()

if (
    validaciones.nombre_valido(nombre)
    and validaciones.precio_valido(precio)
    and validaciones.cantidad_valida(cantidad)
):
    print("Datos aceptados.")
else:
    print("Revisa los datos.")

if validaciones.categoria_valida(categoria, CATEGORIAS):
    print("Categoría válida.")
else:
    print("Categoría no registrada.")
```

**Resultados esperados (según las reglas de las funciones):**

| Nombre | Precio | Cantidad | Categoría | Datos | Categoría |
|---|---:|---:|---|---|---|
| Teclado | 85000 | 3 | Periféricos | aceptados | válida |
| (solo espacios) | 100 | 2 | Accesorios | rechazados | válida |
| Mouse | -5 | 1 | Muebles | rechazados | no registrada |
| Mouse | 45000 | -1 | Componentes | rechazados | válida |
| Mouse | 45000 | 0 | periféricos | aceptados | no registrada (la comparación distingue mayúsculas) |

**Resultados reales:**

```text
Nombre: Teclado
Precio: 85000
Cantidad: 3
Categoría: Periféricos
Datos aceptados.
Categoría válida.
```

```text
Nombre:    
Precio: 100
Cantidad: 2
Categoría: Accesorios
Revisa los datos.
Categoría válida.
```

```text
Nombre: Mouse
Precio: -5
Cantidad: 1
Categoría: Muebles
Revisa los datos.
Categoría no registrada.
```

```text
Nombre: Mouse
Precio: 45000
Cantidad: -1
Categoría: Componentes
Revisa los datos.
Categoría válida.
```

```text
Nombre: Mouse
Precio: 45000
Cantidad: 0
Categoría: periféricos
Datos aceptados.
Categoría no registrada.
```

**Comparación:** **Coincide** con la tabla de resultados esperados en las cinco ejecuciones (incluyendo que `periféricos` en minúscula no se reconoce como categoría).

### Depuración — Importación incorrecta — `depuracion_importacion/`

**Predicción (antes de ejecutar):** aparecerá un `NameError`: con `import operaciones` el nombre que existe en `main.py` es `operaciones`, no `calcular_subtotal`.

**Código original ejecutado:**

`operaciones.py`

```python
def calcular_subtotal(precio, cantidad):
    return precio * cantidad
```

`main.py`

```python
import operaciones

print(calcular_subtotal(10000, 3))
```

**Resultado real:**

```text
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    print(calcular_subtotal(10000, 3))
          ^^^^^^^^^^^^^^^^^
NameError: name 'calcular_subtotal' is not defined
```

**Comparación:** **Coincide.** Apareció `NameError: name 'calcular_subtotal' is not defined`.

**¿Por qué aparece el error si la función sí existe?** Porque `import operaciones` solo trae el nombre del módulo. La función vive dentro de ese módulo, así que debe llamarse con el punto: `operaciones.calcular_subtotal(...)`. (La otra opción es `from operaciones import calcular_subtotal`.) No hace falta copiar la función a `main.py`.

Versión corregida (`depuracion_importacion/main.py`):

`practica-3-2/depuracion_importacion/main.py`

```python
import operaciones

print(operaciones.calcular_subtotal(10000, 3))
```

```text
30000
```

### Reto — Cotizador modular — `cotizador_modular/`

`calculos.py` (solo cálculos):

`practica-3-2/cotizador_modular/calculos.py`

```python
def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    return subtotal * porcentaje / 100


def calcular_impuesto(base, porcentaje):
    return base * porcentaje / 100
```

`validaciones.py` (precio, cantidad y porcentajes):

`practica-3-2/cotizador_modular/validaciones.py`

```python
def precio_valido(precio):
    return precio > 0


def cantidad_valida(cantidad):
    return cantidad > 0


def porcentaje_valido(porcentaje):
    return 0 <= porcentaje <= 100
```

`main.py` (pide los datos y muestra el resultado):

`practica-3-2/cotizador_modular/main.py`

```python
import calculos
import validaciones

print("=============================")
print("      COTIZADOR PYTHON")
print("=============================")
print()

cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = float(input("Descuento (%): "))
porcentaje_impuesto = float(input("Impuesto (%): "))

if not validaciones.precio_valido(precio) or not validaciones.cantidad_valida(cantidad):
    print("El precio y la cantidad deben ser mayores que cero.")
elif (
    not validaciones.porcentaje_valido(porcentaje_descuento)
    or not validaciones.porcentaje_valido(porcentaje_impuesto)
):
    print("Los porcentajes deben estar entre 0 y 100.")
else:
    subtotal = calculos.calcular_subtotal(precio, cantidad)
    valor_descuento = calculos.calcular_descuento(subtotal, porcentaje_descuento)
    base = subtotal - valor_descuento
    valor_impuesto = calculos.calcular_impuesto(base, porcentaje_impuesto)
    total = base + valor_impuesto

    print()
    print("-----------------------------")
    print("RESUMEN DE COMPRA")
    print("-----------------------------")
    print(f"Cliente: {cliente}")
    print(f"Producto: {producto}")
    print(f"Precio unitario: ${precio}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${subtotal}")
    print(f"Descuento: ${valor_descuento}")
    print(f"Base: ${base}")
    print(f"Impuesto: ${valor_impuesto}")
    print(f"TOTAL: ${total}")
```

**Resultado esperado:** con precio `100000`, cantidad `2`, descuento `10` e impuesto `19`, el total es `214200` (se mostrará como `214200.0`). Con los datos del cotizador del Laboratorio 1 (180000, 2, 10, 19) el total debe ser `385560.0`.

**Resultado real (datos del enunciado):**

```text
=============================
      COTIZADOR PYTHON
=============================

Nombre del cliente: Laura
Producto: Silla
Precio unitario: 100000
Cantidad: 2
Descuento (%): 10
Impuesto (%): 19

-----------------------------
RESUMEN DE COMPRA
-----------------------------
Cliente: Laura
Producto: Silla
Precio unitario: $100000.0
Cantidad: 2
Subtotal: $200000.0
Descuento: $20000.0
Base: $180000.0
Impuesto: $34200.0
TOTAL: $214200.0
```

**Resultado real (ejemplo del Laboratorio 1):**

```text
=============================
      COTIZADOR PYTHON
=============================

Nombre del cliente: Laura
Producto: Teclado mecánico
Precio unitario: 180000
Cantidad: 2
Descuento (%): 10
Impuesto (%): 19

-----------------------------
RESUMEN DE COMPRA
-----------------------------
Cliente: Laura
Producto: Teclado mecánico
Precio unitario: $180000.0
Cantidad: 2
Subtotal: $360000.0
Descuento: $36000.0
Base: $324000.0
Impuesto: $61560.0
TOTAL: $385560.0
```

**Resultado real con un precio inválido:**

```text
=============================
      COTIZADOR PYTHON
=============================

Nombre del cliente: Laura
Producto: Silla
Precio unitario: -100000
Cantidad: 2
Descuento (%): 10
Impuesto (%): 19
El precio y la cantidad deben ser mayores que cero.
```

**Resultado real con un descuento inválido (150 %):**

```text
=============================
      COTIZADOR PYTHON
=============================

Nombre del cliente: Laura
Producto: Silla
Precio unitario: 100000
Cantidad: 2
Descuento (%): 150
Impuesto (%): 19
Los porcentajes deben estar entre 0 y 100.
```

**Comprobación de que importar `calculos.py` no pide datos ni ejecuta el cotizador** (se ejecuta `import calculos` desde la carpeta):

`python3 -c "import calculos"`

```text
(sin salida)
```

El resultado vacío indica que no se imprimió nada ni se solicitó ninguna entrada. Lo mismo para `validaciones.py`:

`python3 -c "import validaciones"`

```text
(sin salida)
```

**Comparación:** **Coincide.** Con los datos del enunciado el total fue `214200.0`; con los datos del Laboratorio 1 fue `385560.0`; el precio negativo y el descuento de 150 % se rechazaron con su mensaje; y `import calculos` e `import validaciones` no imprimieron nada ni pidieron datos.

## Comprobación de la práctica 3.2

**¿Qué archivo se ejecuta?**
El que se escribe en el comando (`python main.py`). Es el programa principal. Los demás archivos solo se ejecutan cuando el principal los importa.

**¿Qué significa importar?**
Traer a un archivo los nombres (funciones, variables) definidos en otro módulo para poder usarlos. Al importar, Python ejecuta el módulo una vez (su código de nivel superior) y deja disponibles sus nombres.

**¿Cuándo elegir `import modulo` y cuándo `from modulo import funcion`?**
`import modulo` obliga a escribir `modulo.funcion()`, lo que deja claro de dónde viene cada nombre; es útil cuando se usan varias funciones del módulo o para evitar choques de nombres. `from modulo import funcion` permite llamar `funcion()` directamente y es cómodo cuando solo se necesitan una o dos funciones concretas. En ambos casos se evita `from modulo import *`.

**¿Para qué sirve `if __name__ == "__main__"`?**
Para que un bloque de código (pruebas, demostraciones) se ejecute solo cuando el archivo se ejecuta directamente, y no cuando otro archivo lo importa.

---

# Práctica 3.3 — Clases, objetos, `__init__` y `self`

Archivos en `practica-3-3/`.

## 2. Primera clase

**Predicción (antes de ejecutar):** se imprimirá `<class '__main__.Producto'>`: el objeto `teclado` es de tipo `Producto`, y `__main__` indica que la clase se definió en el archivo que se está ejecutando.

```python
class Producto:
    pass


teclado = Producto()
print(type(teclado))
```

**Resultado real:**

```text
<class '__main__.Producto'>
```

**Comparación:** **Coincide:** `<class '__main__.Producto'>`.

## 3, 4 y 5. Atributos, métodos y dos objetos — `primer_producto.py`

El archivo final reúne los pasos 3, 4 y 5 del laboratorio (se reemplazó el ejemplo inicial, como se indica).

`practica-3-3/primer_producto.py`

```python
class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalle(self):
        print("Código:", self.codigo)
        print("Producto:", self.nombre)
        print("Precio:", self.precio)
        print("Cantidad:", self.cantidad)

    def calcular_valor(self):
        return self.precio * self.cantidad


teclado = Producto("P001", "Teclado", 85000, 4)

print(type(teclado))
print(teclado.codigo)
print(teclado.nombre)
print(teclado.precio)
print(teclado.cantidad)

teclado.mostrar_detalle()
print("Valor:", teclado.calcular_valor())

mouse = Producto("P002", "Mouse", 45000, 7)

print("Valor del teclado:", teclado.calcular_valor())
print("Valor del mouse:", mouse.calcular_valor())

mouse.cantidad = 2

print("Cantidad del teclado:", teclado.cantidad)
print("Cantidad del mouse:", mouse.cantidad)
```

**Predicción (antes de ejecutar):**

- Importe del teclado: `85000 × 4 = 340000`.
- Importe del mouse: `45000 × 7 = 315000`.
- Después de `mouse.cantidad = 2`, la cantidad del teclado **no cambia** (sigue en 4), porque cada objeto guarda sus propios atributos; la del mouse pasa a 2.

Salida completa esperada:

```text
<class '__main__.Producto'>
P001
Teclado
85000
4
Código: P001
Producto: Teclado
Precio: 85000
Cantidad: 4
Valor: 340000
Valor del teclado: 340000
Valor del mouse: 315000
Cantidad del teclado: 4
Cantidad del mouse: 2
```

**Resultado real:**

```text
<class '__main__.Producto'>
P001
Teclado
85000
4
Código: P001
Producto: Teclado
Precio: 85000
Cantidad: 4
Valor: 340000
Valor del teclado: 340000
Valor del mouse: 315000
Cantidad del teclado: 4
Cantidad del mouse: 2
```

**Comparación:** **Coincide línea por línea** con la salida esperada: valor del teclado `340000`, valor del mouse `315000`, y la cantidad del teclado siguió en `4` mientras la del mouse pasó a `2`.

### Ejercicio — Clase Estudiante — `estudiante.py`

`practica-3-3/estudiante.py`

```python
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
```

**Predicción (antes de ejecutar):** con promedio 2.8, `aprobo()` devuelve `False`; con 4.1 devuelve `True`.

**Resultado real:**

```text
Nombre: Laura
Ficha: 2900001
Promedio: 2.8
¿Aprobó? False

Nombre: Andrés
Ficha: 2900002
Promedio: 4.1
¿Aprobó? True
```

**Comparación:** **Coincide.** `2.8` → `False` y `4.1` → `True`.

## 6. Función o método

Una **función** como `calcular_valor(precio, cantidad)` recibe todos los datos como argumentos. Un **método** como `calcular_valor(self)` trabaja con los datos (atributos) del objeto que lo llama. Se usa un método cuando la tarea pertenece naturalmente al objeto (el valor de *este* producto) y se conserva una función cuando la tarea no depende de un objeto concreto.

## 7. Atributo de clase y atributo de instancia

### Versión con lista de clase — `registro_atributo_clase.py`

`practica-3-3/registro_atributo_clase.py`

```python
class Registro:
    elementos = []


primero = Registro()
segundo = Registro()

primero.elementos.append("Teclado")
print(segundo.elementos)
```

**Predicción (antes de ejecutar):** se imprimirá `['Teclado']`. La lista `elementos` está escrita en el cuerpo de la clase, por lo que es una sola lista compartida por todas las instancias; al agregar `"Teclado"` desde `primero`, también se ve desde `segundo`.

**Resultado real:**

```text
['Teclado']
```

**Comparación:** **Coincide.** Se imprimió `['Teclado']`.

**¿Por qué aparece `Teclado` en el segundo objeto?** Porque `elementos` es un atributo de **clase** con una lista mutable. Ni `primero` ni `segundo` tienen un atributo propio llamado `elementos`, así que ambos usan la misma lista de la clase.

### Corrección — `registro_instancia.py`

`practica-3-3/registro_instancia.py`

```python
class Registro:
    def __init__(self):
        self.elementos = []


primero = Registro()
segundo = Registro()

primero.elementos.append("Teclado")

print("Primero:", primero.elementos)
print("Segundo:", segundo.elementos)
```

**Resultado real:**

```text
Primero: ['Teclado']
Segundo: []
```

Al crear la lista con `self.elementos = []` dentro de `__init__`, cada objeto tiene la suya. El segundo queda vacío.

## Depuración — Falta `self` — `depuracion_falta_self.py`

**Predicción (antes de ejecutar):** aparecerá un `TypeError`. Python envía automáticamente el objeto como primer argumento al llamar `saludo.mostrar()`, pero `mostrar()` está definido sin parámetros, así que se queja de que recibió un argumento que no esperaba.

**Código original ejecutado:**

```python
class Saludo:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar():
        print("Hola")


saludo = Saludo("Ana")
saludo.mostrar()
```

**Resultado real:**

```text
Traceback (most recent call last):
  File "depuracion_falta_self_original.py", line 10, in <module>
    saludo.mostrar()
    ~~~~~~~~~~~~~~^^
TypeError: Saludo.mostrar() takes 0 positional arguments but 1 was given
```

**Comparación:** **Coincide.** Apareció `TypeError: Saludo.mostrar() takes 0 positional arguments but 1 was given`.

**Corrección:** se agrega `self` a la firma (`def mostrar(self):`) y, para mostrar el nombre, se usa `self.nombre`.

`practica-3-3/depuracion_falta_self.py`

```python
class Saludo:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print("Hola,", self.nombre)


saludo = Saludo("Ana")
saludo.mostrar()
```

```text
Hola, Ana
```

## Depuración — Atributo inexistente — `depuracion_atributo.py`

**Predicción (antes de ejecutar):** el código original, al llamar `mostrar()`, producirá un `AttributeError`: el objeto tiene `nombre` (con una sola "e") pero el método intenta leer `nombree`. (El código original del laboratorio solo define la clase; para ver el error se crea un objeto y se llama al método.)

**Código original ejecutado:**

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(self.nombree)


persona = Persona("Ana")
persona.mostrar()
```

**Resultado real:**

```text
Traceback (most recent call last):
  File "depuracion_atributo_original.py", line 10, in <module>
    persona.mostrar()
    ~~~~~~~~~~~~~~~^^
  File "depuracion_atributo_original.py", line 6, in mostrar
    print(self.nombree)
          ^^^^^^^^^^^^
AttributeError: 'Persona' object has no attribute 'nombree'. Did you mean: 'nombre'?
```

**Comparación:** **Coincide.** Apareció `AttributeError: 'Persona' object has no attribute 'nombree'` (Python además sugiere `nombre`).

**Corrección:** solo se cambia el nombre del atributo (`self.nombre`).

`practica-3-3/depuracion_atributo.py`

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(self.nombre)


persona = Persona("Ana")
persona.mostrar()
```

```text
Ana
```

### Reto — Billetera orientada a objetos — `billetera.py`

`practica-3-3/billetera.py`

```python
class Billetera:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def registrar_ingreso(self, monto):
        if monto <= 0:
            return False

        self.saldo += monto
        return True

    def registrar_gasto(self, monto):
        if monto <= 0:
            return False

        if monto > self.saldo:
            return False

        self.saldo -= monto
        return True

    def consultar_saldo(self):
        return self.saldo


billetera_ana = Billetera("Ana")
billetera_luis = Billetera("Luis")

print("Ingreso de Ana 50000:", billetera_ana.registrar_ingreso(50000))
print("Ingreso de Luis 20000:", billetera_luis.registrar_ingreso(20000))
print("Gasto de Ana 15000:", billetera_ana.registrar_gasto(15000))
print("Gasto de Luis 30000:", billetera_luis.registrar_gasto(30000))
print("Ingreso de Ana -100:", billetera_ana.registrar_ingreso(-100))
print("Gasto de Ana 0:", billetera_ana.registrar_gasto(0))

print()
print("Saldo de", billetera_ana.titular + ":", billetera_ana.consultar_saldo())
print("Saldo de", billetera_luis.titular + ":", billetera_luis.consultar_saldo())
```

**Predicción (antes de ejecutar):** Ana ingresa 50000 (`True`); Luis ingresa 20000 (`True`); Ana gasta 15000 (`True`); Luis intenta gastar 30000 pero solo tiene 20000 (`False`); ingresar -100 y gastar 0 se rechazan (`False`, `False`). Saldos finales: Ana 35000 y Luis 20000, lo que demuestra que cada billetera tiene un estado independiente.

**Resultado real:**

```text
Ingreso de Ana 50000: True
Ingreso de Luis 20000: True
Gasto de Ana 15000: True
Gasto de Luis 30000: False
Ingreso de Ana -100: False
Gasto de Ana 0: False

Saldo de Ana: 35000
Saldo de Luis: 20000
```

**Comparación:** **Coincide:** `True`, `True`, `True`, `False`, `False`, `False`; saldos finales Ana `35000` y Luis `20000`.

## Comprobación de la práctica 3.3

**¿Qué representa `self`?**
El objeto concreto que está ejecutando el método. Gracias a `self`, el método puede leer y cambiar los atributos de ese objeto (`self.precio`, `self.cantidad`) y no los de otro.

**¿Para qué se utiliza `__init__`?**
Es el método que Python ejecuta automáticamente al crear un objeto. Sirve para darle sus valores iniciales, es decir, para crear y asignar sus atributos.

**¿Por qué `self.elementos = []` evita que dos objetos compartan una lista?**
Porque esa instrucción se ejecuta cada vez que se crea un objeto y crea una lista nueva guardada en ese objeto. Cada objeto tiene entonces su propia lista. En cambio, una lista escrita en el cuerpo de la clase se crea una sola vez y todos los objetos la comparten.

---

# Práctica 3.4 — Métodos, encapsulamiento, propiedades y colaboración

Archivos en `practica-3-4/`.

## 1. ¿Qué ocurre con los cambios sin control?

**Predicción (antes de ejecutar):** con la clase `Producto` de la práctica 3.3 (atributos públicos), las asignaciones `teclado.precio = -5000` y `teclado.cantidad = -10` se aceptan sin error, porque Python no revisa lo que se asigna a un atributo público. Incluso `calcular_valor()` devolvería `50000` (negativo × negativo).

```python
# (aquí va la clase Producto de practica-3-3/primer_producto.py, sin cambios)
teclado = Producto("P001", "Teclado", 85000, 4)

teclado.precio = -5000
teclado.cantidad = -10

print(teclado.precio, teclado.cantidad)
print(teclado.calcular_valor())
```

**Resultado real:**

```text
-5000 -10
50000
```

**Comparación:** **Coincide.** No hubo error: el precio quedó en `-5000`, la cantidad en `-10` y el valor calculado fue `50000`.

## 2 a 5. Atributos internos, propiedades, existencias y setter — `producto_seguro.py`

`practica-3-4/producto_seguro.py`

```python
class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def calcular_valor(self):
        return self._precio * self._cantidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        if nueva_cantidad < 0:
            return False

        self._cantidad = nueva_cantidad
        return True

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self._precio = nuevo_precio


producto = Producto("P001", "Teclado", 85000, 4)
print(producto.calcular_valor())

print(producto.codigo)
print(producto.nombre)
print(producto.cantidad)

try:
    producto.codigo = "P999"
except AttributeError:
    print("El código no se puede cambiar.")

print(producto.actualizar_existencias(10))
print(producto.cantidad)

print(producto.actualizar_existencias(-5))
print(producto.cantidad)

producto.precio = 90000
print(producto.precio)

try:
    producto.precio = -5000
except ValueError:
    print("Precio rechazado: debe ser mayor que cero.")

print(producto.precio)
```

**Predicción (antes de ejecutar):**

- `calcular_valor()` → `340000`.
- Se imprimen `P001`, `Teclado` y `4` (propiedades, se consultan sin paréntesis).
- `producto.codigo = "P999"` no se puede hacer porque la propiedad no tiene setter (`AttributeError`; en el archivo se captura para mostrar un mensaje).
- `actualizar_existencias(10)` → `True` y la cantidad pasa a `10`.
- `actualizar_existencias(-5)` → `False` y la cantidad sigue en `10`.
- `producto.precio = 90000` funciona y se imprime `90000`.
- `producto.precio = -5000` produce `ValueError` (en el archivo se captura) y el precio sigue en `90000`.

**Resultado real:**

```text
340000
P001
Teclado
4
El código no se puede cambiar.
True
10
False
10
90000
Precio rechazado: debe ser mayor que cero.
90000
```

**Comparación:** **Coincide línea por línea** con la predicción (`340000`, `P001`, `Teclado`, `4`, mensaje del código, `True`/`10`, `False`/`10`, `90000`, mensaje del precio y `90000`).

Para ver los errores reales de Python sin capturarlos (se reutiliza la clase `Producto` de `producto_seguro.py`):

```python
# (aquí va la clase Producto de practica-3-4/producto_seguro.py, sin cambios)
producto = Producto("P001", "Teclado", 85000, 4)
producto.codigo = "P999"
```

**Resultado real:**

```text
Traceback (most recent call last):
  File "error_sin_setter.py", line 43, in <module>
    producto.codigo = "P999"
    ^^^^^^^^^^^^^^^
AttributeError: property 'codigo' of 'Producto' object has no setter
```

```python
# (aquí va la clase Producto de practica-3-4/producto_seguro.py, sin cambios)
producto = Producto("P001", "Teclado", 85000, 4)
producto.precio = -5000
```

**Resultado real:**

```text
Traceback (most recent call last):
  File "error_precio_negativo.py", line 43, in <module>
    producto.precio = -5000
    ^^^^^^^^^^^^^^^
  File "error_precio_negativo.py", line 37, in precio
    raise ValueError("El precio debe ser mayor que cero.")
ValueError: El precio debe ser mayor que cero.
```

(Los números de línea de los mensajes cuentan también las líneas de la clase `Producto`, que en estos fragmentos se resumió con un comentario.)

La asignación al código se rechaza porque no existe un setter y la del precio negativo se rechaza con `ValueError` porque el setter valida el valor. Observación del laboratorio: el constructor de este ejemplo asigna `self._precio` directamente, por lo que un producto podría *nacer* con un precio inválido. Esa corrección se hace en el proyecto final (`gestor_inventario/producto.py`), donde el constructor valida todos los datos.

### Ejercicio — Cuenta de puntos — `cuenta_puntos.py`

`practica-3-4/cuenta_puntos.py`

```python
class CuentaPuntos:
    def __init__(self, titular):
        self._titular = titular
        self._puntos = 0

    @property
    def titular(self):
        return self._titular

    @property
    def puntos(self):
        return self._puntos

    def sumar(self, cantidad):
        if cantidad <= 0:
            return False

        self._puntos += cantidad
        return True

    def canjear(self, cantidad):
        if cantidad <= 0:
            return False

        if cantidad > self._puntos:
            return False

        self._puntos -= cantidad
        return True


cuenta = CuentaPuntos("Laura")

print("Sumar: 80    ->", "aceptado" if cuenta.sumar(80) else "rechazado")
print("Canjear: 30  ->", "aceptado" if cuenta.canjear(30) else "rechazado")
print("Canjear: 100 ->", "aceptado" if cuenta.canjear(100) else "rechazado")
print("Total:", cuenta.puntos)
```

**Predicción (antes de ejecutar):** sumar 80 → aceptado; canjear 30 → aceptado (quedan 50); canjear 100 → rechazado (solo hay 50); total final 50.

**Resultado real:**

```text
Sumar: 80    -> aceptado
Canjear: 30  -> aceptado
Canjear: 100 -> rechazado
Total: 50
```

**Comparación:** **Coincide:** aceptado, aceptado, rechazado y total `50`.

## 6 y 7. Dos clases que colaboran — `relacion_objetos/`

`producto.py`:

`practica-3-4/relacion_objetos/producto.py`

```python
class Producto:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
```

`inventario.py` (con `buscar_por_codigo` del punto 7):

`practica-3-4/relacion_objetos/inventario.py`

```python
class Inventario:
    def __init__(self):
        self._productos = []

    def agregar(self, producto):
        self._productos.append(producto)

    def listar(self):
        return self._productos.copy()

    def buscar_por_codigo(self, codigo):
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None
```

`main.py`:

`practica-3-4/relacion_objetos/main.py`

```python
from producto import Producto
from inventario import Inventario

inventario = Inventario()

inventario.agregar(Producto("P001", "Teclado"))
inventario.agregar(Producto("P002", "Mouse"))

for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)

encontrado = inventario.buscar_por_codigo("P002")

if encontrado is not None:
    print("Encontrado:", encontrado.nombre)
else:
    print("Producto no registrado.")
```

**Resultado esperado:** `P001 - Teclado`, `P002 - Mouse` y `Encontrado: Mouse`.

**Resultado real:**

```text
P001 - Teclado
P002 - Mouse
Encontrado: Mouse
```

`Inventario` conserva objetos `Producto` (no diccionarios); la copia de `listar()` evita que se cambie directamente la lista interna.

## 8. Manejo básico de una entrada incorrecta — `leer_precio.py`

`practica-3-4/leer_precio.py`

```python
try:
    precio = float(input("Precio: "))
    print("Precio ingresado:", precio)
except ValueError:
    print("Debes escribir un número válido.")
```

**Predicción (antes de ejecutar):** con `85000` se imprime `Precio ingresado: 85000.0`; con `abc`, `float()` falla con `ValueError` y se imprime el mensaje `Debes escribir un número válido.`

**Resultado real con `85000`:**

```text
Precio: 85000
Precio ingresado: 85000.0
```

**Resultado real con `abc`:**

```text
Precio: abc
Debes escribir un número válido.
```

**Comparación:** **Coincide.** Con `85000` se imprimió `Precio ingresado: 85000.0` y con `abc` el mensaje `Debes escribir un número válido.`

### Ejercicio — Reintentar una cantidad — `leer_cantidad.py`

`practica-3-4/leer_cantidad.py`

```python
while True:
    try:
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Debes escribir un entero.")
        print()
        continue

    if cantidad < 0:
        print("La cantidad no puede ser negativa.")
        print()
        continue

    print("Cantidad aceptada:", cantidad)
    break
```

**Resultado esperado** (entradas `abc`, `-2`, `5`): mensaje de entero inválido, luego mensaje de cantidad negativa y finalmente `Cantidad aceptada: 5`.

**Resultado real:**

```text
Cantidad: abc
Debes escribir un entero.

Cantidad: -2
La cantidad no puede ser negativa.

Cantidad: 5
Cantidad aceptada: 5
```

## Depuración — Lista compartida — `depuracion_lista_compartida.py`

**Predicción (antes de ejecutar):** el código original imprimirá `['Teclado']` en lugar de una lista vacía, porque `productos = []` está en el cuerpo de la clase y es compartida por los dos inventarios.

**Código original ejecutado:**

```python
class Inventario:
    productos = []

    def agregar(self, producto):
        self.productos.append(producto)


primero = Inventario()
segundo = Inventario()

primero.agregar("Teclado")
print(segundo.productos)
```

**Resultado real:**

```text
['Teclado']
```

**Comparación:** **Coincide.** El código original imprimió `['Teclado']`; con la corrección se imprime `[]`.

**Corrección:** la lista se crea dentro de `__init__` con `self.productos = []`, para que cada inventario tenga la suya.

`practica-3-4/depuracion_lista_compartida.py`

```python
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)


primero = Inventario()
segundo = Inventario()

primero.agregar("Teclado")
print(segundo.productos)
```

```text
[]
```

### Reto — Inventario con reglas — `inventario_reglas/`

`producto.py`:

`practica-3-4/inventario_reglas/producto.py`

```python
class Producto:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
```

`inventario.py` (`agregar` sin duplicados, `buscar_por_codigo` y `eliminar`):

`practica-3-4/inventario_reglas/inventario.py`

```python
class Inventario:
    def __init__(self):
        self._productos = []

    def agregar(self, producto):
        if self.buscar_por_codigo(producto.codigo) is not None:
            return False

        self._productos.append(producto)
        return True

    def listar(self):
        return self._productos.copy()

    def buscar_por_codigo(self, codigo):
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def eliminar(self, codigo):
        producto = self.buscar_por_codigo(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)
        return True
```

`main.py` (prueba dos productos válidos, uno con código repetido y una eliminación de un código inexistente):

`practica-3-4/inventario_reglas/main.py`

```python
from producto import Producto
from inventario import Inventario

inventario = Inventario()

print("Agregar P001 Teclado:", inventario.agregar(Producto("P001", "Teclado")))
print("Agregar P002 Mouse:", inventario.agregar(Producto("P002", "Mouse")))
print("Agregar P001 repetido:", inventario.agregar(Producto("P001", "Otro teclado")))

print()
print("Productos registrados:", len(inventario.listar()))
for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)

print()
print("Eliminar P999 (no existe):", inventario.eliminar("P999"))
print("Eliminar P002:", inventario.eliminar("P002"))

print()
print("Productos registrados:", len(inventario.listar()))
for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)

print("Buscar P002:", inventario.buscar_por_codigo("P002"))
```

**Resultado esperado:** `True`, `True` y `False` al agregar; 2 productos registrados; eliminar `P999` → `False`; eliminar `P002` → `True`; queda solo `P001`.

**Resultado real:**

```text
Agregar P001 Teclado: True
Agregar P002 Mouse: True
Agregar P001 repetido: False

Productos registrados: 2
P001 - Teclado
P002 - Mouse

Eliminar P999 (no existe): False
Eliminar P002: True

Productos registrados: 1
P001 - Teclado
Buscar P002: None
```

**Comparación:** **Coincide** con el resultado esperado (`True`, `True`, `False`; 2 productos; `False` y `True` al eliminar; queda solo `P001`; buscar `P002` devuelve `None`).

## Comprobación de la práctica 3.4

**¿Por qué `Inventario` conserva una colección de objetos?**
Porque su responsabilidad es administrar varios productos: registrar, buscar, eliminar y consultar. Cada `Producto` guarda los datos de un solo artículo. Como `Inventario` conoce todo el conjunto, es la clase que puede aplicar reglas que dependen de la colección, como evitar códigos repetidos.

**¿Por qué `_productos` se considera interno?**
Porque el guion bajo inicial es una convención que indica que ese atributo no debe usarse desde fuera de la clase. Las demás partes del programa deben usar los métodos de `Inventario` (`agregar`, `eliminar`, `listar`), que respetan las reglas, y no manipular la lista directamente.

**¿Cuál es la diferencia entre asignar libremente un atributo y usar un método que comprueba reglas?**
Al asignar libremente (`producto.cantidad = -10`) el valor cambia sin ninguna revisión, aunque no tenga sentido. Un método como `actualizar_existencias(-10)` revisa la regla, rechaza el valor inválido (devuelve `False`) y conserva el dato anterior.

---

# Práctica 3.5 — Reto integrador: gestor de inventario orientado a objetos

## Antes de programar — Responde

(Los comentarios de roles pedidos por el laboratorio están al comienzo de `producto.py`, `inventario.py` y `main.py`.)

**¿Qué clase debe evitar los códigos repetidos?**
`Inventario`, porque es la clase que conoce toda la colección. Un `Producto` solo conoce sus propios datos y no puede saber si otro producto ya usa su código.

**¿Qué clase debe comprobar que la cantidad sea válida?**
`Producto`, porque cada producto controla sus propios valores: lo hace en `__init__` (al crearse) y en `actualizar_existencias()`. `main.py` además vuelve a pedir el dato cuando el usuario escribe algo inválido, pero la regla vive en `Producto`.

**¿Qué clase calcula el valor de un producto?**
`Producto`, con el método `calcular_valor()` (`precio * cantidad`). `Inventario` solo suma esos valores en `resumen()`.

**¿Dónde debe utilizarse `input()`?**
Solo en `main.py`. `Producto` e `Inventario` no leen datos ni imprimen el menú.

**¿Quién debe decidir qué mensaje se muestra después de una operación?**
`main.py`. Las clases solo devuelven resultados (`True`, `False`, un objeto, `None` o datos) y `main.py` decide qué texto mostrar.

