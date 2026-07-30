'''
Tarea
Tienes tres listas: nombres de productos, precios y cantidades vendidas. El objetivo es organizar, ordenar y mostrar estos datos en un formato específico.

Instrucciones del código
1.- Utilizar zip() para combinar las tres listas en una lista de tuplas en el orden: (product_name, price, quantity_sold). Asignar el resultado a combined_list.

2.-Utilizar sorted() para ordenar combined_list por el nombre del producto en orden ascendente. Asignar el resultado ordenado a sorted_products.

3.-Recorrer sorted_products e imprimir el nombre del producto, el precio y la cantidad vendida utilizando el formato especificado.

Requisitos de salida
Para cada producto, imprimir:
Product: <product_name>, Price: <product_price>, Quantity Sold: <quantity_sold>
'''

# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

#1.-
combined_list = list(zip(products, prices, quantities_sold))

#2.-
sorted_products = sorted(combined_list)

#3.-
for product_name, product_price, quantity_sold in sorted_products:
    print(f"Product: {product_name}, Price: {product_price}, Quantity Sold: {quantity_sold}")
