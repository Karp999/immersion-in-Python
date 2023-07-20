# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# полученные имена сохраните в файл.

import random

def create_random_name():
    length = random.randint(4, 7)
    low_letters = 'абвгдежзийклмнопрстуфхцчшщьэюя'
    up_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЭЮЯ'
    random_name = ''.join(random.sample(up_letters, 1)) + ''.join(random.sample(low_letters, length))
    return random_name

def filling_file_with_names(nums, file):
    for i in range(nums):
        with open(file, 'a', encoding='utf-8') as f:
            f.write(f'{create_random_name()} \n')

if __name__ == '__main__':
    print('Сколько псевдоимен необходимо создать?')
    number_lines = int(input('-> '))
    print('Введите имя файла: ')
    file = input('-> ')
    filling_file_with_names(number_lines, file)