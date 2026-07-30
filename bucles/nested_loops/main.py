'''
Tarea
Se te proporcionan dos listas de artículos de supermercado:

- produce, que contiene frutas y verduras
- dairy, que contiene productos lácteos

Tu tarea es combinar estas dos listas en una sola lista llamada groceries, donde cada lista original se convierte en un elemento dentro de groceries.

Luego, utiliza bucles for anidados para imprimir el nombre de cada artículo:

1.- El bucle externo debe recorrer cada categoría (llamada section) en groceries.
2.- El bucle interno debe recorrer cada item dentro de la section actual.
3.- Imprime cada artículo en su propia línea con el formato: Item name: <item>
'''
produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce , dairy]
print(groceries)
#1.-
for section in groceries:
    print(section)
    for item in section:
        print(f"Item name: {item}")