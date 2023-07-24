# Домашнее задание:
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

from pathlib import Path
import os
import json
import csv
import pickle

def Size_folder(path):
    f_size = 0
    for file in Path(path).rglob('*'):
        if (os.path.isfile(file)):
            f_size += os.path.getsize(file)
    return f_size

def r_folder_traversal(path, level = 1):
    for j in (os.listdir(path)):
        file_size = os.path.getsize(path + '/' + j)
        f_size = Size_folder(path + '/' + j)
        path_file_or_folder = path + '/' + j
        if os.path.isfile(path_file_or_folder):
            list_data.append({
                'type': 'file',
                'name': j,
                'path': path,
                'size': file_size
            })

        else:
            list_data.append({
                'type': 'folder',
                'name': j,
                'path': path,
                'size': f_size
            })

    for i in os.listdir(path):
        if os.path.isdir(path + '/' + i):
            r_folder_traversal(path + '/' + i, level + 1)


def write_To_Files(list_data):
    with open('hulu.json', 'w') as f_json:
        json.dump(list_data, f_json, indent=2, ensure_ascii=False)
    with open('hulu.csv', 'w', newline='', encoding='utf-8') as f_csv:
        csv_write = csv.DictWriter(f_csv, fieldnames=[*list_data[0]])
        csv_write.writeheader()
        csv_write.writerows(list_data)
    with open('hulu.pickle', 'wb') as f_pickle:
        pickle.dump(list_data, f_pickle)


if __name__ == '__main__':
    path = 'C:/Users/79995/Desktop/GEEK BRAINS/6.seminars/2semester/python2/hm'
    list_data = []
    r_folder_traversal(path)
    write_To_Files(list_data)
    
# вложила в папку "dz8" файлы формата json, csv и pickle, которые получились