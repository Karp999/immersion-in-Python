# Задание №7
# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from os import chdir
from pathlib import Path

def sort_file(dict_file_extension, dir_name):
    if isinstance(dir_name, str):
        dir_name = Path(dir_name)
    else:
        dir_name = dir_name
    chdir(dir_name)
    for key in dict_file_extension:
        a = Path(key)
        if not a.is_dir():
            a.mkdir(parents=True)

    p = Path(Path().cwd())
    for obj in p.iterdir():
        for key in dict_file_extension:
            if obj.suffix in dict_file_extension[key]:
                obj.replace(p / key / obj.name)

put = 'C:\Users\79995\Desktop\GEEK BRAINS\6.seminars\2 semester 2023\python2\hm'
dict_file_extension = {'video': ['.mov', '.avi', '.doc', '.mp4'], 'docum': ['.txt']}
sort_file(dict_file_extension, put)

