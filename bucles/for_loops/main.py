'''
Tarea
Suma de precios de productos
Cálculo del costo total de productos utilizando un bucle for para iterar sobre una lista de precios.

1.- Crear una variable total y establecerla en 0.
2.- Utilizar un bucle for para iterar sobre cada price en la lista prices.
3.- Sumar cada price a la variable total dentro del bucle.
4.- Imprimir el valor final de total después de que el bucle termine.
'''
prices = [12.99, 8.50, 15.75, 23.00, 7.25]

# Write your code here
#1.-
total = 0

#2.-
for price in prices:
    print(price)
    #3.-
    total = total + price

#4.-
print(f"Total: {total}")