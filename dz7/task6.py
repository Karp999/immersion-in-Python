# Задача 6:
# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from random import *

DIC1 = 'abcdefghijklm'
DIC2 = 'nopqrstuvwxyz'

def function(dic, a=5, b=30, c=7, d=256):
    for key in dic:
        for _ in range(dic[key]):
            name = ""
            for i in range(randint(6, 30)):
                name += choice(DIC1)
                if len(name) >= 30: break
                name += choice(DIC2)
            name = name + '.' + key
            if Path(name).is_file():
                continue
            with open(name, 'w', encoding='utf-8') as new_f:
                g = bytes(randint(0, 255) for i in range(randint(256, 4096)))
                new_f.write(f'{g}')


dic = {"txt": 5, "doc": 3}
function(dic, a=5, b=30, c=7, d=256)


def dir(text):    # создание директории
    if isinstance(text, str):
        a = Path(text)  # преобразование в class 'pathlib.WindowsPath'
    else:
        a = text
    if not a.is_dir():
        a.mkdir(parents=True)
    chdir(a)
    function(dic, a=5, b=30, c=7, d=256)


dir('Sem7')