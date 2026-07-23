'''
Tarea
Gestionar una lista de productos de charcutería inicializándolos, actualizándolos y organizándolos en diferentes categorías como carnes, quesos y condimentos.

1.- Inicializar listas:

Crear una lista meat con los valores: "Ham", 3.99, 50, "Sliced";
Crear una lista cheese con los valores: "Cheddar", 5.49, 100, "Sharp";
Crear una lista condiment con los valores: "Mustard", 1.99, 75, "Spicy".

2.- Crear lista principal:

Combinar las listas meat, cheese y condiment en una sola lista llamada deli_dept.

3.- Reabastecer artículo:

Si "Ham" está en la lista meat y su cantidad es menor que 100, actualizar su cantidad a 100.

4.- Agregar carne de temporada:

Crear una lista seasonal_meat con los valores: "Turkey", 4.50, 100, "Sliced";
Añadir seasonal_meat a deli_dept.

5.- Eliminar condimento:

Eliminar la lista condiment de deli_dept.

6.- Ordenar lista:

Ordenar deli_dept alfabéticamente según el primer elemento de cada sublista utilizando el método sort().

Requisitos de salida
Imprimir el estado inicial de deli_dept con el mensaje: "Initial Deli List: <$deli_dept>".
Después de todas las operaciones, imprimir el estado actualizado de deli_dept con el mensaje: "Updated Deli List: <$deli_dept>".
Nota

El ordenamiento de la lista se realizará en función del primer valor de cada sublista (por ejemplo, "Ham", "Cheddar", "Turkey").'''

#1.-
meat = ["Ham", 3.99, 50,"Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

#2.-
deli_dept = [meat, cheese, condiment]
print(f"Initial Deli List: {deli_dept}")

#3.-
if "Ham" in meat and meat[2] < 100:
    meat[2] = 100
    print(meat)

#4.-
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)
print(deli_dept)

#5.- 
deli_dept.remove(condiment)
print(deli_dept)

#6.-
deli_dept.sort()
print(f"Updated Deli List: {deli_dept}")