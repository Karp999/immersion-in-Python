# Задача3:
# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя,
# записанное строчными буквами и произведение по модулю,
# если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# При достижении конца более короткого файла,
# возвращайтесь в его начало.

from random import randint, choice

DIC1 = "AIEYUO"
DIC2 = "QWRTPSDFHGKL"


def multiply():
    with (
        open('hulu.txt', 'r', encoding='utf-8') as numbers,
        open('hdori.txt', 'r', encoding='utf-8') as liter,
        open('both_files', 'a', encoding='utf-8') as r
    ):
        while res_n := numbers.readline():
            a = res_n.replace(' \n', '').split(" | ")

            if a == ['\n']:
                continue
            print(a)
            mult_ = int(a[0]) * float(a[1])
            res_l = ''
            if mult_ < 0:
                res_l = liter.readline().replace(' \n', '')
                r.write(f'{res_l.lower(), abs(mult_)} \n')
            elif mult_ >= 0:
                r.write(f'{res_l.upper(), round(mult_)} \n')


multiply()