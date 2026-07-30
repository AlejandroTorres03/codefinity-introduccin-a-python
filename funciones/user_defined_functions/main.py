'''
Tarea
Definir una función para calcular el costo total de un producto multiplicando su precio y la cantidad vendida.

1.- Crear una función llamada calculate_total_cost() que reciba dos parámetros: price y quantity.
2.- Dentro de la función, multiplicar price por quantity para obtener el costo total.
3.- Devolver el resultado desde la función.

Requisitos de salida
- Llamar a calculate_total_cost() con price = 1.50 y quantity = 10.
- Imprimir el resultado como:
    The total cost for apples is $<apples_total_cost>
'''
#1.-
def calculate_total_cost(price, quantity):
    #2.-
    total = price * quantity
    #3.-
    return total
    
# Call the function and print the result
apples_total_cost = calculate_total_cost(1.50, 10)

print(f"The total cost for apples is ${apples_total_cost}")
