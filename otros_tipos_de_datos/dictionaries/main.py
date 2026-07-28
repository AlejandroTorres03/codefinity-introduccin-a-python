'''
Tarea
Gestionar el inventario de una tienda de comestibles utilizando un diccionario, donde cada artículo es un par clave-valor con el nombre del artículo y los detalles (ID de producto y categoría).

1.- Definir un diccionario grocery_inventory para almacenar la información:

"Milk": (113, "Dairy")
"Eggs": (116, "Dairy")
"Bread": (117, "Bakery")
"Apples": (141, "Produce")

2.- Obtener los detalles del artículo "Bread" del diccionario y almacenarlos en la variable bread_details.

3.- Agregar un nuevo artículo, "Cookies", con ID de producto 143 y categoría "Bakery".

4.- Eliminar el artículo "Eggs" del diccionario.

Requisitos de salida
Imprimir los detalles de "Bread": Details of Bread: <$bread_details>.
Después de agregar "Cookies", imprimir el inventario actualizado: Inventory after adding Cookies: <$grocery_inventory>.
Después de eliminar "Eggs", imprimir el inventario actualizado: Inventory after removing Eggs: <$grocery_inventory>.
'''

#1.-
grocery_inventory = {
    "Milk": (11, "Dairy"), 
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")}

#2.-
bread_details = grocery_inventory.get("Bread")
print(f"Details of Bread: {bread_details}")

#3.- 
grocery_inventory.update({"Cookies":(143, "Bakery")})
print(f"Inventory after adding Cookies: {grocery_inventory}")

#4.-
grocery_inventory.pop("Eggs")
print(f"Inventory after removing Eggs: {grocery_inventory}")

