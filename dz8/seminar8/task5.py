#  Задача 5:
# Напишите функцию, которая 
#  - ищет json файлы в указанной директории
#  - сохраняет их содержимое в виде одноимённых pickle файлов.

import json
import pickle

def search_jsonfiles():
    file = 'third.json'
    with open(f'C:/Users/79995/Desktop/GEEK BRAINS/6.seminars/2semester/python2/hm/dz8/seminar8/third.json', 'r', encoding='utf-8') as readers_dir:
        list_direct = json.load(readers_dir)
        readers_dir.close()

    with open(f'C:/Users/79995/Desktop/GEEK BRAINS/6.seminars/2semester/python2/hm/dz8/seminar8/third.pickle', 'wb') as writes:
        writ_namefile = pickle.dump(writ_namefile, writes)        # в аргументы передать объект и файл
        writes.close()

search_jsonfiles()