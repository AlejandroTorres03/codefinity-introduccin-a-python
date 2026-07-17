'''
Tarea
Crea un sistema sencillo de estrategia de descuentos para una tienda de comestibles que muestre descuentos según el tipo de producto y el día de la semana.

#1.-
Utilizar las variables proporcionadas

product_type
day_of_week
Aplicar expresiones condicionales

#2.-
#2.1.- Si product_type es Fruits y day_of_week es Monday, mostrar10% discount on Fruits today!
#2.2.- Si product_type es Vegetables y day_of_week es Tuesday, mostrar 15% discount on Vegetables today!
#2.3.- Si product_type es Dairy y day_of_week es Wednesday, mostrar 20% discount on Dairy today!
#2.4.- Si product_type es Other, mostrar No discount available.
#2.5.- En cualquier otro caso, mostrar No special discounts today.

#3.-
Requisitos de salida
El programa debe mostrar exactamente una línea según los valores de entrada.
Ejemplos de salidas válidas
10% discount on Fruits today!
15% discount on Vegetables today!
20% discount on Dairy today!
No discount available.
No special discounts today.
Consejo:
Utilizar sentencias if, elif y else para comparar ambas variables al mismo tiempo, por ejemplo
if product_type == "Fruits" and day_of_week == "Monday":
'''
#1.- Input variables
product_type = "Dairy"  
day_of_week = "Wednesday"

#2.-
#2.1.-
if product_type == "Fruits" and day_of_week == "Monday":
    print("10% discount on Fruits today!")
#2.2.-
elif product_type == "Vegetables" and day_of_week == "Tuesday":
    print("15% discount on Vegetables today!")
#2.3.-
elif product_type == "Dairy" and day_of_week == "Wednesday":
    print("20% discount on Dairy today!")
#2.4.-
elif product_type == "Other":
    print("No discount available.")
#2.5.-
else:
    print("No special discounts today.")