# Задача №1:
# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

print('')
repeating_elements = [2, 9, 7, 3, 9, 7, 3, 8, 8, 8, 3, 7, 9, 3, 7, 9, 2]
print(f'Исходный список повторяющихся элементов: {repeating_elements}')
print('')

no_duplicates = []

for i in repeating_elements:
    if repeating_elements.count(i) > 1 : 
        no_duplicates.append(i)
        
no_duplicates = list(set(no_duplicates))

print(f'Список повторяющихся элементов из исходного списка без дублей: {no_duplicates}')
print('')