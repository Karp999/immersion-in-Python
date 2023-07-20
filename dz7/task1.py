# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

import random

MAX = 1000
MIN = -1000

def file_with_nums(nums, file):
    for i in range(nums):
        num_int = random.randint(MIN, MAX)
        num_float = random.uniform(MIN, MAX)
        with open(file, 'a', encoding="utf-8") as f:
            f.write(f'{num_int} | {num_float} \n')

if __name__ == '__main__':
    print('Сколько строк с числами необходимо создать в файле?')
    number_lines = int(input('-> '))
    print('Введите имя файла: ')
    file = input('-> ')
    file_with_nums(number_lines, file)