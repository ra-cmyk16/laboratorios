# Gestor de Inventario Persistente

## Descripción

Aplicación de consola desarrollada en Python para administrar productos
y conservar la información mediante archivos JSON.

También permite exportar reportes de inventario en formato CSV.

## Archivos del proyecto

- `main.py`: menú e interacción con el usuario.
- `producto.py`: clase Producto y validaciones.
- `inventario.py`: administración de productos y resumen.
- `almacenamiento.py`: lectura y escritura de JSON.
- `reportes.py`: exportación de reportes CSV.
- `datos/productos.json`: archivo generado para guardar los productos.
- `reportes/inventario.csv`: archivo generado al exportar el reporte.

## Requisitos

- Python 3.
- No requiere instalar paquetes externos.

## Ejecución

Abre una terminal en la carpeta `gestor_inventario` y ejecuta:

```bash
python main.py