# Задача 3:
# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

num = randint(0, 1000)
count = 1
print('') #пробелы для красоты вывода

while count < 10:
    user_num = int(input('Какое число я загадал? Введите ваше предположение: '))
    if user_num == num:
        print('Ура! Вы отгадали!')
        print('') 
        break
    elif user_num > num:
        print('Неверно! Мое число меньше!', count + 1, 'попытка!')
        print('') 
    else: 
        print('Неверно! Мое число больше!', count + 1, 'попытка!')
        print('') 
    count += 1
print('Вы истратили все попытки! Мое число: ', num)
print('')