'''
Tarea
Siga estas instrucciones paso a paso para completar la tarea:

1.- Inicializar una lista llamada products que contenga los nombres de los productos;

2.- Inicializar una lista llamada prices que contenga el precio por unidad de cada producto;

3.- Inicializar una lista llamada quantities_sold que contenga la cantidad de unidades vendidas de cada producto;

4.- Calcular los ingresos de cada producto multiplicando el precio por la cantidad vendida, y almacenar todos los resultados en una nueva lista llamada revenue;

5.- Utilizar la función zip() para combinar las listas products y revenue en una lista de tuplas llamada revenue_per_product, donde cada tupla contiene el nombre del producto y sus ingresos correspondientes;

6.- Ordenar la lista revenue_per_product alfabéticamente por el nombre del producto;

7.- Imprimir cada producto y sus ingresos utilizando este formato: <product_name> has total revenue of $<revenue>.

Debe definir las siguientes funciones:

- calculate_revenue(prices, quantities_sold): Esta función debe multiplicar cada precio por su cantidad vendida correspondiente, almacenar los resultados en una lista y devolver esta lista de ingresos.

- formatted_output(revenues): Esta función debe tomar una lista de tuplas (product_name, revenue), ordenarlas alfabéticamente por el nombre del producto e imprimir cada una en el formato especificado.

Después de definir estas funciones, utilice las listas proporcionadas para llamarlas y mostrar los resultados como se describe arriba.
'''
# List of products, their prices, and the quantities sold
#1.-
products = ["Bread", "Apples", "Oranges", "Bananas"]
#2.- 
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
#3.-
quantities_sold = [150, 200, 100, 50]  # number of items sold

#4.-
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for a, b in zip(prices, quantities_sold):
        revenue.append(a*b)
    return revenue

# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")
#5.-
#revenue_per_product = list(zip(products, revenue))

#6.- & 7.-
def formatted_output(revenues):
    revenues= sorted(revenues)
    for product_name, revenue in revenues:
        print(f"{product_name} has total revenue of ${revenue}")

revenue = calculate_revenue(prices, quantities_sold)

revenue_per_product = list(zip(products, revenue))

formatted_output(revenue_per_product)