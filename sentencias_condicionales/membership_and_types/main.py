'''
Tarea
Está gestionando datos para un nuevo producto que acaba de ser añadido al sistema de una tienda de comestibles. Su tarea es analizar la información del producto utilizando operadores de pertenencia y comparaciones de tipo.

1.- Verificar si la subcadena 'raw' existe en description. Almacene el resultado en contains_raw.

2.- Verificar si la subcadena 'Imported' existe en description. Almacene el resultado en contains_Imported.

3.- Verificar si price es de tipo float. Almacene el resultado en price_is_float.

4.- Verificar si count es de tipo int. Almacene el resultado en count_is_int.

Imprima los resultados exactamente en el formato proporcionado en el código.

Recuerde que Python distingue entre mayúsculas y minúsculas, por lo que 'imported' y 'Imported' se consideran cadenas diferentes.
'''
# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120

# Write your code here
#1.-
contains_raw = "raw" in description
#2.-
contains_Imported = "Imported" in description
#3.-
price_is_float = type(price) == float
#4.-
count_is_int = type(count) == int


print("Contains 'raw':", contains_raw)
print("Contains 'Imported':", contains_Imported)
print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)