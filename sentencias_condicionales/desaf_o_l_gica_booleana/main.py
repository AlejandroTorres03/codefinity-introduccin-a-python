'''
Tarea
Determinar si un artículo de supermercado debe recibir un descuento según su estatus estacional, nivel de inventario y rendimiento de ventas.

1.- Definir una variable booleana overstock_risk como True si el artículo es seasonal y su current_stock supera el high_stock_threshold.
2.- Definir otra variable booleana discount_eligible como True si el artículo not está selling_well y not está ya on_sale.
3.-Crear una variable booleana make_discount que sea True si overstock_risk o discount_eligible es True.

Requisitos de salida
Imprimir si el artículo debe recibir un descuento: Should the item be discounted? <make_discount>.
'''

seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

#1.-
overstock_risk = seasonal and (current_stock > high_stock_threshold)

#2.-
discount_eligible = not selling_well and not on_sale

#3.-
make_discount = overstock_risk or discount_eligible

#Salida
print(f"Should the item be discounted? {make_discount}")