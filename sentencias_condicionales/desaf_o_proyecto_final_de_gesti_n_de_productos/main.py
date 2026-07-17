'''
Tarea
Implementar una serie de declaraciones condicionales para determinar el descuento de un producto según su tipo, los días hasta su vencimiento y el nivel de inventario.

#1.- Comenzar verificando si el product_type es "Perishable".
Dentro de esta declaración if:
#1.1.- imprimir "30% discount applied" si days_until_expiration es 3 o menos y stock_level es mayor que 50;
#1.2.- imprimir "20% discount applied" si days_until_expiration está entre 4 y 6, y stock_level es mayor que 50;
#1.3.- imprimir "10% discount applied" si days_until_expiration es mayor que 6 y stock_level es 50 o menos.
#1.4.- Si el product_type no es "Perishable", imprimir "No discount available for non-perishable items.".

Es posible anidar múltiples declaraciones if unas dentro de otras. Asegurarse de gestionar correctamente la indentación para cada bloque.
'''
# Input variables
days_until_expiration = 6  # Example value
stock_level = 60  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

#1.-
if product_type == "Perishable":
    #1.1.-
    if days_until_expiration <= 3 and stock_level > 50:
        print("30% discount applied")
    #1.2.-
    elif 4 <= days_until_expiration <= 6 and stock_level > 50:
        print("20% discount applied")
    #1.3.-
    elif days_until_expiration > 6 and stock_level <=50:
        print("10% discount applied")
#1.4.-
else:
    print("No discount available for non-perishable items.")

    