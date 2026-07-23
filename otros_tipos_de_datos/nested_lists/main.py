'''
Tarea
Actualización de una lista de inventario para la sección de verduras de una tienda de comestibles eliminando un artículo, agregando dos nuevos artículos y ordenando la lista alfabéticamente sin duplicados.

#1.- Crear una variable vegetables con la lista ["tomatoes", "potatoes", "onions"].
#2.-Eliminar "onions" de la lista.
#3.-Agregar "carrots" a la lista si aún no está presente.
#4.-Agregar "cucumbers" a la lista si aún no está presente.
#5.-Ordenar la lista alfabéticamente.

Requisitos de salida
Imprimir la lista de verduras actualizada: "Updated Vegetable Inventory: <vegetables>".
Si "carrots" ya está en la lista, imprimir: "Carrots are already in the list."
Si "cucumbers" ya está en la lista, imprimir: "Cucumbers are already in the list."
'''
#1.-
vegetables = ["tomatoes", "potatoes", "onions"]

#2.-
vegetables.remove("onions")

#3.-
vegetables.append("carrots")

#4.-
vegetables.append("cucumbers")

#5.- 
vegetables.sort()

#resultados
print(f"Updated Vegetable Inventory: {vegetables}")

if "carrots" in vegetables:
    print("Carrots are already in the list")
else:
    print("Carrots are not already in the list")

if "cucumbers" in vegetables:
    print("Cucumbers are already in the list")
else:
    print("Cucumbers are not already in the list")