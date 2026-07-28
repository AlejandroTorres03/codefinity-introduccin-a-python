'''
Tarea
Gestionar un inventario de comestibles utilizando un diccionario en Python. Realizar operaciones básicas: actualizar un precio, agregar un nuevo artículo, ajustar el stock según una condición, opcionalmente eliminar un artículo por precio y mostrar mensajes de estado simples.

1.- Crear el diccionario
Definir grocery_inventory con los siguientes artículos y detalles:

"Milk": ("Dairy", 3.50, 8)
"Eggs": ("Dairy", 5.50, 30)
"Bread": ("Bakery", 2.99, 15)
"Apples": ("Produce", 1.50, 50)

2.-Verificar y actualizar el precio

- Obtener el precio de "Eggs".
- Si el precio es mayor que 5, mostrar
    "Eggs are too expensive, reducing the price by $1."
    y reducir el precio en 1.
- De lo contrario, mostrar
    The price of Eggs is reasonable.
    
3.- Agregar un nuevo artículo

- Agregar "Tomatoes" con los detalles: categoría "Produce", precio 1.20, stock 30.
- Luego mostrar Inventory after adding Tomatoes: <grocery_inventory>

4.- Gestionar el stock

- Verificar el stock de "Milk".
- Si es menor que 10, mostrar
    Milk needs to be restocked. Increasing stock by 20 units.
    y aumentar el stock en 20.
- De lo contrario, mostrar
    Milk has sufficient stock.

5.- Eliminar artículo según el precio

- Si el precio de "Apples" supera 2, eliminar "Apples" y mostrar
    Apples removed from inventory due to high price.

6.- Impresión final

Mostrar
Updated inventory: <grocery_inventory>
'''

#1.-
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)}

#2.-
if grocery_inventory.get("Eggs")[1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (
    grocery_inventory["Eggs"][0],
    grocery_inventory["Eggs"][1] - 1,
    grocery_inventory["Eggs"][2])
else:
    print("The price of Eggs is reasonable.")

#3.-
grocery_inventory.update({"Tomatoes":("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

#4.-
if grocery_inventory.get("Milk")[2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (
        grocery_inventory["Milk"][0],
        grocery_inventory["Milk"][1],
        grocery_inventory["Milk"][2] + 20)
else:
    print("Milk has sufficient stock.")

#5.-
if grocery_inventory.get("Apples")[1] > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

#6.-
print(f"Updated inventory: {grocery_inventory}")