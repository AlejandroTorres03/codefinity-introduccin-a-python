'''
Tarea
Procesar datos de productos a partir de un diccionario donde los precios y las cantidades se almacenan como cadenas de texto. El objetivo es calcular las ventas totales de cada producto y generar estadísticas resumidas.

1.- Utilizar un bucle for para iterar a través del diccionario products. En cada iteración, acceder tanto al nombre del producto (la clave) como a sus valores asociados (la lista que contiene el precio y la cantidad). Esto permite trabajar con cada producto y sus datos individualmente;

2.- Para cada producto:
    - Convertir el precio a float;
    - Convertir la cantidad vendida a int;
    - Multiplicarlos para obtener las ventas totales de ese producto;
    - Añadir las ventas totales a total_sales_list.

3.- Utilizar sum() para calcular la suma total de todas las ventas.

4.- Asignar la suma total a la variable total_sum.

5.- Utilizar min() y max() para obtener los valores de ventas mínimas y máximas.

6.- Asignar el valor mínimo a la variable min_sales.

7.- Asignar el valor máximo a la variable max_sales.

Requisitos de salida
Para cada producto, imprimir:
Total sales for <product>: $<total_sales>
Después de procesar todos los productos, imprimir:
Total sum of all sales: $<total_sum>
Minimum sales: $<min_sales>
Maximum sales: $<max_sales>
'''
# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []
print(products.items())
#1.-
for key, value in products.items():
    price, sold = value
    #2.-
    price = float(price)
    sold = int(sold)
    total_sales = price * sold
    total_sales_list.append(total_sales)
    #3 & 4.-
    total_sum = sum(total_sales_list)
    #5, 6, 7.-
    min_sales = min(total_sales_list)
    max_sales = max(total_sales_list)
    print(f"Total sales for {key}: ${total_sales}")

print(f"Total sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")
    