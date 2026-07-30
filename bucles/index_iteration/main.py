'''
Tarea
En esta tarea, se aplicarán diferentes porcentajes de descuento a los precios de productos según su posición (índice) en una lista.

Se proporciona una lista de precios de productos. Cada precio debe actualizarse de acuerdo con su índice en la lista.

Pasos
Comenzar con la lista de precios proporcionada

1.- Utilizar un bucle for junto con range() y len() para iterar sobre los índices de la lista prices (desde el índice 0 hasta el último índice).

2.- Dentro del bucle, comprobar el índice actual y aplicar el descuento correspondiente:

- Índice 0 → aplicar un 10% de descuento
- Índice 1 → aplicar un 20% de descuento
- Índice 2 → aplicar un 15% de descuento
- Índice 3 → aplicar un 5% de descuento

3.- Actualizar cada precio directamente en la lista prices después de aplicar el descuento.

4.- Después de actualizar el precio, imprimir el resultado en el siguiente formato:
Updated price for item {index}: ${updated_price:.2f}

Nota

.2f formatea un número a dos decimales (por ejemplo, 5 se convierte en 5.00). Utilizarlo dentro de un f-string de la siguiente manera: {price:.2f}.
'''
prices = [29.99, 45.50, 12.75, 38.20]
discount = [0.10, 0.20, 0.15, 0.05]
updated_price = []
#1.-
for i in range(len(prices)):
    #2.- & #3.-
    prices[i] -= prices[i] * discount[i]
    updated_price.append(prices[i])
    print(f"Updated price for item {i}: ${updated_price[i]:.2f}")
    
    