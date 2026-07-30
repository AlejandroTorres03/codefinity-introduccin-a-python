'''
Tarea
Actualización de los niveles de inventario de productos en función de las ventas y los envíos utilizando bucles.

1.- Uso de un bucle for con iteración por índice para recorrer la lista products.
- Para cada producto, restar la cantidad de unidades vendidas (units_sold) del inventario de products.

2.- Uso de un segundo bucle for (también con iteración por índice) para recorrer nuevamente products.
- Sumar el valor correspondiente de shipment_received para actualizar el inventario.

Al final, imprimir: Final stock levels for all products: <products>
'''
# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

for i in range(len(products)):
    products[i][1] = products[i][1] - units_sold[i][1]

for i in range(len(products)):
    products[i][1] = products[i][1] + shipment_received[i][1]

print(f"Final stock levels for all products: {products}")