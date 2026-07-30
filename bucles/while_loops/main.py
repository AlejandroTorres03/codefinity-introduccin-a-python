'''
Tarea
Crear un temporizador de cuenta regresiva de descuentos que recopile todos los valores de la cuenta regresiva en una lista utilizando un bucle while.

1.- Utilizar un bucle while para contar desde start_number hasta 1 (inclusive), decrementando en 1 en cada iteración.
2.- Durante cada iteración, agregar el valor actual de la cuenta regresiva a la lista countdown_values.
3.- Después de que el bucle termine, imprimir Discount countdown complete! y luego imprimir la lista countdown_values.
'''
start_number = 5
countdown_values = []
#1.-
while start_number >= 1:
    #2.-
    countdown_values.append(start_number)
    start_number -= 1

print(f"Discount countdown complete! {countdown_values}")