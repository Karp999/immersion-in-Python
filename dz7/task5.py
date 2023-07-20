# Задача 5:
# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи

from random import *

DIC1 = 'abcdefghijklm'
DIC2 = 'nopqrstuvwxyz'

def function(dic, a=5, b=30, c=7, d=256):
    for key in dic:
        for _ in range(dic[key]):         # формируем файлы в количестве, указанном в словаре для каждого расширения
            name = ""
            for i in range(randint(6, 30)):
                name += choice(DIC1)
                if len(name) >= 30: break
                name += choice(DIC2)
            name = name + '.' + key
            with open(name, 'w', encoding='utf-8') as new_f:
                g = bytes(randint(0, 255) for i in range(randint(256, 4096)))
                new_f.write(f'{g}')


dic = {"txt": 5, "doc": 3}
function(dic, a=5, b=30, c=7, d=256)