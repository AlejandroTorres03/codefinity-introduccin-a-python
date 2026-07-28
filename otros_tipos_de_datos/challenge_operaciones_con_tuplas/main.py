'''
Tarea
Gestionar una tupla que representa un estante de frutas realizando operaciones para contar, encontrar y verificar los niveles de stock.

#1.- Contar cuántas veces aparece "apples" en la tupla shelf. Almacenar este valor en apple_count e imprimir: "Number of Apples: <apple_count>".

#2.- Encontrar el índice de la primera aparición de "bananas" en la tupla shelf. Almacenar el índice en banana_index e imprimir: "First Banana Index: <banana_index>".

#3.- Verificar si la cantidad de manzanas es menor que 5. Si es cierto, imprimir: "Apples need to be restocked." De lo contrario, imprimir: "Apples are sufficiently stocked."

#4.- Contar cuántas veces aparece "grapes" en la tupla shelf. Si las uvas aparecen solo una vez, imprimir: "Grapes need to be restocked." De lo contrario, imprimir: "Grapes are sufficiently stocked."

#5.- Verificar si "oranges" existe en la tupla shelf. Si existen, imprimir su índice con: "Oranges are at index: <orange_index>". Si no existen, imprimir: "Oranges are out of stock."

Requisitos de salida
- Imprimir el número de manzanas: "Number of Apples: <apple_count>".
- Imprimir el índice de la primera aparición de bananas: "First Banana Index: <banana_index>".
- Imprimir un mensaje sobre el estado del stock de manzanas: "Apples need to be restocked." o "Apples are sufficiently stocked."
- Imprimir un mensaje sobre el estado del stock de uvas: "Grapes need to be restocked." o "Grapes are sufficiently stocked."
- Imprimir el índice de las naranjas si existen: "Oranges are at index: <orange_index>", o "Oranges are out of stock."
Se pueden utilizar los operadores in y not in tanto con tuplas como con listas.
'''
# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

#1.-
apple_count = shelf.count("apples")
print(f"Number of Apples: {apple_count}")

#2.-
banana_index = shelf.index("bananas")
print(f"First Banana Index: {banana_index}")

#3.-
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

#4.-
if "grapes" in shelf:
    if shelf.count("grapes") == 1:
        print("Grapes need to be restocked.")
    else:
        print("Grapes are sufficiently stocked.")
else:
    print("There are not grapes in the shelf.")

#5.-
if "oranges" in shelf:
    orange_index = shelf.index("oranges")
    print(f"Oranges are at index: {orange_index}")

else:
    print("Oranges are out of stock")

