# Cotizador de compra — Laboratorio 1

## 1. Descripción del proyecto

El cotizador de compra es un programa desarrollado en Python que permite calcular el valor final de una compra a partir de los datos ingresados por el usuario.

Este proyecto integra los conocimientos básicos del Laboratorio 1, como variables, tipos de datos, entrada de información con `input()`, operaciones aritméticas y presentación de resultados.

## 2. Objetivo

Crear un programa de consola que solicite los datos de una compra, calcule el subtotal, el descuento, el impuesto y el total final, y muestre los resultados de manera organizada.

## 3. Datos solicitados

El programa solicita:

- Nombre del cliente.
- Nombre del producto.
- Precio unitario.
- Cantidad de unidades.
- Porcentaje de descuento.
- Porcentaje de impuesto.

## 4. Cálculos realizados

1. **Subtotal:** precio unitario multiplicado por la cantidad.
2. **Valor del descuento:** subtotal multiplicado por el porcentaje de descuento y dividido entre 100.
3. **Base después del descuento:** subtotal menos el valor del descuento.
4. **Valor del impuesto:** base después del descuento multiplicada por el porcentaje de impuesto y dividida entre 100.
5. **Total final:** base después del descuento más el valor del impuesto.

El impuesto se calcula después de aplicar el descuento, siguiendo las instrucciones de la práctica.

## 5. Archivo del proyecto

El archivo principal es:

`cotizador_compra.py`

Este contiene las instrucciones para solicitar los datos, realizar los cálculos y mostrar el resumen de la compra.

## 6. Requisitos

- Tener Python 3 instalado.
- Contar con Visual Studio Code o una terminal.
- No se necesitan librerías externas.

## 7. Instrucciones de ejecución

1. Guarda el archivo `cotizador_compra.py` en una carpeta de tu computador.
2. Abre la carpeta en Visual Studio Code.
3. Abre una terminal desde **Terminal > New Terminal**.
4. Ejecuta el siguiente comando:

```bash
python cotizador_compra.py
```

Si el comando anterior no funciona, prueba:

```bash
py cotizador_compra.py
```

También puedes utilizar `python3 cotizador_compra.py`, según la configuración de tu equipo.

5. Ingresa los datos solicitados por el programa.
6. Revisa el resumen y comprueba que los cálculos sean correctos.

Los porcentajes se ingresan como números enteros. Por ejemplo, escribe `10` para representar el 10 %.

## 8. Pruebas de comprobación

| Precio | Cantidad | Descuento | Impuesto | Total esperado |
|---:|---:|---:|---:|---:|
| 100000 | 2 | 10 % | 0 % | 180000 |
| 50000 | 3 | 0 % | 0 % | 150000 |
| 80000 | 5 | 25 % | 0 % | 300000 |
| 100000 | 1 | 0 % | 19 % | 119000 |

Estos resultados permiten verificar que el programa calcula correctamente el subtotal, el descuento, la base después del descuento, el impuesto y el total final.

## 9. Conceptos aprendidos

Con este proyecto se practican:

- Variables y tipos de datos.
- Entrada de datos mediante `input()`.
- Conversión de texto a valores numéricos.
- Operaciones aritméticas.
- Cálculo de porcentajes.
- Uso de `print()` para mostrar resultados.
- Organización de cálculos mediante variables.
