'''
Tarea
Crear funciones para calcular el costo total de un producto aplicando descuento e impuesto, utilizando argumentos por palabra clave y valores predeterminados para mayor flexibilidad.

1.-Definir apply_discount(price, discount=0.05)
    → Devuelve el precio después de aplicar el descuento.

2.- Definir apply_tax(price, tax=0.07)
    → Devuelve el precio después de agregar el impuesto.

3.-Definir calculate_total(price, discount=0.05, tax=0.07)
    → Utiliza apply_discount() y apply_tax() para devolver el precio total con descuento e impuesto aplicados.

4.- Llamar a calculate_total(120) usando el descuento e impuesto predeterminados.

5.- Llamar a calculate_total(100, discount=0.10, tax=0.08) usando valores personalizados mediante argumentos por palabra clave.

Requisitos de salida
- Imprimir el resultado con valores predeterminados:
Total cost with default discount and tax: $<total_price_default>

- Imprimir el resultado con valores personalizados:
Total cost with custom discount and tax: $<total_price_custom>

Nota

Al definir funciones, colocar primero los parámetros obligatorios, seguidos de los parámetros con valores predeterminados.

Al llamar funciones con argumentos por palabra clave, los argumentos posicionales deben ir antes que los argumentos por palabra clave.
'''
#1.-
def apply_discount(price, discount=0.05):
    new_price = price * (1-discount)
    return new_price

#2.-
def apply_tax(price, tax=0.07):
    tax_price = price * (1+tax)
    return tax_price

#3.-
def calculate_total(price, discount=0.05, tax=0.07):
    total = apply_discount(price, discount)
    total = apply_tax(total, tax)
    return total

#4.-
total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price_default}")

#5.-
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")