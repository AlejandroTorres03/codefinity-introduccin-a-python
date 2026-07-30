'''
Tarea
Utiliza dos listas — weekdays y daily_promotions — para mostrar la promoción asignada a cada día de la semana.

1.- Emplea un bucle for con la función range() para iterar sobre los índices de las listas.

2.- En cada iteración:
- Obtén el weekday actual de la lista weekdays.
- Obtén la promoción correspondiente de daily_promotions usando el mismo índice.

3.- Muestra ambos valores en el formato especificado.

Requisitos de salida
Para cada día, imprime:
<weekday>: Promotion on <promotion>
Nota

Asegúrate de que ambas listas tengan la misma cantidad de elementos para evitar errores de índice.
'''
# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#1
for day in range(5):
    #2.-
    weekday = weekdays[day]
    promotion = daily_promotions[day]

    print(f"{weekday}: Promotion on {promotion}")
