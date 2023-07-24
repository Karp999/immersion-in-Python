# Задача 2:
# Напишите функцию, которая в бесконечном цикле:
#  - запрашивает имя, 
#  - личный идентификатор 
#  - уровень доступа (от 1 до 7). 
#  После каждого ввода добавляйте новую информацию в JSON файл. 
#  Пользователи группируются по уровню доступа.
#  Идентификатор пользователя выступает ключом для имени. 
#  Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. 
#  При перезапуске функции уже записанные в файл данные должны сохраняться.

import json


def getAccessLevel():
    accessLevels = ['1', '2', '3', '4', '5', '6', '7']

    with open('second.json', 'r', encoding='utf-8') as read_access:
        myDict = json.load(read_access)                             # прочитать данные из файла
        print(myDict)
        read_access.close()

        while True:                                                                    # запусить бесконечный цикл: пока словарь есть...
            ident = input("введите личный идентификатор: ")
            if ident in myDict.keys() :                                        # если есть идентиф-р в ключах словаря, написать сообщение
                print("идентификатор уже используется")
            else :
                while True:
                    access = input(f"введите уровень доступа с {min(accessLevels)} по {max(accessLevels)} : ")
                    if access not in accessLevels :
                        print ("некорректный ввод")
                    else :
                        myDict[ident] = access
                        sortedDict = dict(sorted(myDict.items(), key=lambda item: item[1], reverse=True))  # если reverse=True, то элементы числового списка отсорт по убыванию 
                        print(sortedDict)

                        with open('second.json', 'w', encoding="utf-8") as write_access:
                            new_entry = json.dumps(sortedDict, indent=2, separators=(',', ':'))
                            write_access.write(new_entry)
                            write_access.close()
                            break
                break

getAccessLevel()