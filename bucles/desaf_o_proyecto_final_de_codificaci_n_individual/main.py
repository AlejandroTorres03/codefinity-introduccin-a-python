'''
Tarea
Evalúa los elementos en un diccionario inventory e imprime mensajes apropiados según sus niveles de stock y precios.

- Recorre cada elemento en el diccionario inventory.
- Para cada elemento:
    - Si el stock es inferior a 30, imprime que necesita reabastecimiento.
    - Si el stock es superior a 100, imprime que debe venderse al precio con descuento.
    - Si el stock está entre 30 y 100, imprime que debe venderse al precio regular.

Requisitos de salida
Utiliza exactamente las siguientes plantillas de impresión:

- Para reabastecimiento:
    -f"{item} need restocking."

- Para precio con descuento:
    - f"{item} should be sold at the discounted price of {discounted_price}."

- Para precio regular:
    - f"{item} should be sold at the regular price of {regular_price}."

Nota

Sigue exactamente los formatos de impresión para asegurar que tu solución sea aceptada.
'''
# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

for i in inventory:
    print(f"Processing {i}")
    current_stock, regular_price, discounted_price = inventory[i]
    if current_stock < 30:
        print(f"{i} need restocking.")
    elif current_stock > 100:
        print(f"{i} should be sold at the discounted price of {discounted_price}.")
    elif 30 <= current_stock <= 100:
        print(f"{i} should be sold at the regular price of {regular_price}.")