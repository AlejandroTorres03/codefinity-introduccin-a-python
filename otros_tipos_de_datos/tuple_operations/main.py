'''
Tarea
Estás gestionando el contenido de un estante de supermercado utilizando tuplas. Tu objetivo es actualizar el estante con nuevos artículos y realizar un análisis básico, manteniendo la integridad de los datos (las tuplas deben permanecer inmutables).

Dado
- Una tupla existente shelf1 que representa los artículos actuales en el estante.
- Una lista shelf1_update que contiene nuevos artículos para agregar al estante.

Pasos a completar

#1.- Convertir la lista shelf1_update en una tupla llamada shelf1_update_tuple.
#2.- Concatenar shelf1_update_tuple con la tupla existente shelf1 para crear una nueva tupla llamada shelf1_concat.
#3.- Contar cuántas veces aparece la cadena "celery" en shelf1_concat y almacenar este número en una variable llamada celery_count.
#4.- Encontrar el índice de la primera aparición de "celery" en shelf1_concat y almacenarlo en una variable llamada celery_index.

Requisitos de salida
Imprime las siguientes líneas exactamente en este formato:

1 Updated Shelf #1: <shelf1_concat>
2 Number of Celery: <celery_count>
3 Celery Index: <celery_index>

Sustituye <shelf1_concat> por la tupla resultante.
Sustituye <celery_count> por el número de apariciones de "celery".
Sustituye <celery_index> por el índice de la primera aparición de "celery" en la tupla.
'''

# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

#1.-
shelf1_update_tuple = tuple(shelf1_update)

#2.-
shelf1_concat = shelf1 + shelf1_update_tuple

#3.-
celery_count = shelf1_concat.count("celery")

#4.-
celery_index = shelf1_concat.index("celery")

print(f"Updated Shelf #1: {shelf1_concat}")
print(f"Number of Celery: {celery_count}")
print(f"Celery Index: {celery_index}")