# Laboratorios de Python

## Laboratorio 01 — Cotizador de compra

### Objetivo
Desarrollar un programa que permita calcular el valor final de una compra aplicando descuentos e impuestos.

### Funcionalidades
- Solicitar los datos del cliente.
- Registrar el producto, su precio y la cantidad.
- Solicitar el descuento y el impuesto correspondientes.
- Calcular el subtotal de la compra.
- Calcular el valor descontado y el impuesto.
- Obtener y mostrar el total que debe pagar el cliente.

### Conceptos aplicados
- Variables y tipos de datos.
- Entrada y salida de información.
- Operaciones aritméticas.
- Conversión de tipos de datos.
- Cálculos con porcentajes.

## Laboratorio 02 — Decisiones, ciclos y colecciones en Python

### Objetivo
Aplicar estructuras de control y colecciones mediante un programa de gestión de inventario.

### Archivo principal
`gestor_inventario.py`

### Funcionalidades
- Registrar y consultar productos.
- Organizar la información utilizando colecciones.
- Utilizar condiciones para controlar las opciones del programa.
- Emplear ciclos para repetir operaciones y mostrar información.
- Aplicar validaciones básicas a los datos ingresados.

### Conceptos aplicados
- Condicionales `if`, `elif` y `else`.
- Ciclos `for` y `while`.
- Listas y otras colecciones.
- Funciones y organización del código.
- Validación de entradas del usuario.

## Laboratorio 03 — Gestor de inventario con programación orientada a objetos

### Objetivo
Transformar la gestión del inventario mediante clases y objetos, separando los datos de los productos de las operaciones del inventario.

### Funcionalidades
- Representar los productos mediante objetos.
- Registrar, listar y buscar productos.
- Actualizar las existencias.
- Eliminar productos.
- Validar los datos de los productos.
- Consultar las existencias y el valor del inventario.

### Conceptos aplicados
- Clases y objetos.
- Atributos y métodos.
- Encapsulamiento.
- Constructores.
- Validaciones y excepciones.
- Separación de responsabilidades.

## Laboratorio 04 — Gestor de inventario persistente

### Objetivo
Ampliar el gestor de inventario para conservar los datos entre ejecuciones, generar reportes y mejorar la organización del programa.

### Funcionalidades
- Registrar productos con código, nombre, categoría, precio y cantidad.
- Evitar códigos duplicados.
- Consultar y actualizar productos.
- Eliminar productos registrados.
- Identificar productos sin existencias.
- Calcular el valor total del inventario.
- Guardar los datos en un archivo JSON.
- Cargar automáticamente los datos guardados al iniciar el programa.
- Exportar los productos a un archivo CSV.
- Manejar errores relacionados con la lectura y escritura de archivos.
- Separar las responsabilidades en diferentes módulos de Python.

### Conceptos aplicados
- Persistencia de datos.
- Lectura y escritura de archivos JSON.
- Exportación de información CSV.
- Programación orientada a objetos.
- Validación de datos.
- Manejo de excepciones.
- Modularización del código.
- Uso de rutas de archivos con `pathlib`.

### Estructura del proyecto

```text
gestor_inventario/
├── main.py
├── producto.py
├── inventario.py
├── almacenamiento.py
├── reportes.py
├── datos/
│   └── productos.json
├── reportes/
│   └── inventario.csv
└── README.md
```

**Responsabilidad de cada archivo:**

| Archivo | Descripción |
|---|---|
| `main.py` | Controla el menú y la interacción con el usuario. |
| `producto.py` | Define la clase Producto y valida sus datos. |
| `inventario.py` | Gestiona el registro, la búsqueda, la actualización y la eliminación de productos. |
| `almacenamiento.py` | Guarda y carga el inventario en formato JSON. |
| `reportes.py` | Genera el reporte del inventario en formato CSV. |
| `datos/productos.json` | Almacena los productos para conservarlos entre ejecuciones. |
| `reportes/inventario.csv` | Contiene el reporte exportado para consultarlo en una hoja de cálculo. |

Los archivos JSON y CSV se generan automáticamente cuando se ejecutan las operaciones correspondientes.

## Requisitos

- Python 3 instalado.
- Editor de código, como Visual Studio Code.
- Terminal o consola de comandos.

El proyecto utiliza módulos de la biblioteca estándar de Python, por lo que no requiere instalar paquetes externos.

## Cómo ejecutar el laboratorio 04

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar el siguiente comando:

   ```bash
   python main.py
   ```

   En Windows también se puede utilizar:

   ```bash
   py main.py
   ```

