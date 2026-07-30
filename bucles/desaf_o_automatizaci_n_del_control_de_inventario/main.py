'''
Tarea
Gestionar el inventario de una tienda de comestibles reponiendo artículos mediante un bucle while y aplicando descuentos según los niveles de stock. Se utilizarán bucles para actualizar el estado de cada artículo, pero solo se debe imprimir un mensaje simple de procesamiento para cada artículo y un resumen final.

Reglas

1.- Utilizar un bucle for para recorrer cada artículo en el diccionario inventory.
    - Para cada artículo, obtener su stock actual, el stock mínimo requerido, la cantidad de reposición y el estado de oferta.

2.- Utilizar un bucle while para reponer el artículo hasta que su stock sea igual o superior al mínimo.
    - Aumentar el stock en la cantidad de reposición en cada iteración.
    - Actualizar el valor de stock en el diccionario después de reponer.

3.- Después de reponer, si el stock supera el discount_threshold y el artículo no está en oferta, establecer su estado de oferta como True en el diccionario.

Requisitos de salida

- Antes de iniciar el bucle, imprimir una línea que contenga la palabra Processing (por ejemplo: Processing started).
- Para cada artículo, imprimir una sola línea: Processing [item name] (por ejemplo: Processing Bread).
- Después de procesar todos los artículos, imprimir una línea de resumen que contenga la palabra Processing (por ejemplo: Processing completed).

No imprimir detalles sobre la reposición ni la aplicación de descuentos. No imprimir un informe final de inventario. Solo imprimir las líneas de procesamiento requeridas.
'''

# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started: ")
for i in inventory:
    print(f"Processing {i}...")
    current_stock, minimum_stock, restock_quantity, on_sale = inventory[i]
    while current_stock < minimum_stock:
        current_stock += restock_quantity
        inventory[i][0] = current_stock
    if current_stock > discount_threshold and on_sale != True:
        inventory[i][3] = True
    print(f"Processing of {i} completed.")

print("Processing completed")