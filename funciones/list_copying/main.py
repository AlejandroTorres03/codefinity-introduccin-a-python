'''
Tarea
Crear una función para aplicar un 10% de descuento a los precios de productos superiores a $2.00, sin modificar la lista original.

1.- Definir una función apply_discount(prices) que reciba una lista de precios.

2.- Dentro de la función, hacer una copia de prices y asignarla a prices_copy.

3.- Utilizar un bucle for con iteración por índice (range(len(prices_copy))) para recorrer la lista copiada.

4.- Si un precio es mayor que 2.00, aplicar un descuento del 10%.

5.- Devolver la lista actualizada prices_copy.

Requisitos de salida
- La función debe devolver la nueva lista con los precios descontados.
- Imprimir el resultado usando:
    Updated product prices: <$updated_prices>
Nota

Utilizar iteración basada en índices para asegurar que la lista se modifique correctamente: for index in range(len(prices)): modifica los elementos directamente, a diferencia de for price in prices:.
'''
#1.-
def apply_discount(prices):
    #2.-
    prices_copy = prices.copy()
    #3.-
    for i in range(len(prices_copy)):
        #4.-
        if prices_copy[i] > 2:
            prices_copy[i] = prices_copy[i] * 0.90
    #5.-
    return prices_copy
    
# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

print(f"Updated product prices: ${updated_prices}")