# Задача №1:
# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

print('') #пробелы для красоты вывода
triangle_side_ab = float(input('Введите длину стороны AB треугольника ABC: '))
triangle_side_bc = float(input('Введите длину стороны BC треугольника ABC: '))
triangle_side_ac = float(input('Введите длину стороны AC треугольника ABC: '))
print('')

if triangle_side_ab == triangle_side_bc == triangle_side_ac:
    print('Треугольник ABC является равносторонним.')
elif triangle_side_ab == triangle_side_bc or triangle_side_bc == triangle_side_ac or triangle_side_ab == triangle_side_bc:
    print('Треугольник ABC является равнобедренным.')
elif triangle_side_ab + triangle_side_bc > triangle_side_ac and triangle_side_bc + triangle_side_ac > triangle_side_ab and triangle_side_ac + triangle_side_ab > triangle_side_bc:
    print('Треугольник ABC является разносторонним.')
else:
    print('Треугольник ABC с указанными сторонами не существует!')
    
print('')