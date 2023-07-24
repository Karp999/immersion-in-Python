# Задача 1:
# Вспоминаем задачу 3 из прошлого семинара: мы сформировали текстовый файл 
# с псевдоименами и произведением чисел.
#  Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON. 
#  Имена пишите с большой буквы. 
#  Каждую пару сохраняйте с новой строки.

import json


def toJson():
    myDict = {}
    with open(f"C:/Users/79995/Desktop/GEEK BRAINS/6.seminars/2semester/python2/hm/dz8/seminar8/first.txt", "r", encoding="utf-8") as nf :
        while res := nf.readline():
            myList = res.replace("\n", "").upper().split(' | ')
            myDict[myList[0]] = myList[1]
        nf.close()
    print(myDict)
    with open(f"C:/Users/79995/Desktop/GEEK BRAINS/6.seminars/2semester/python2/hm/dz8/seminar8/first.json", 'w', encoding="utf-8") as f:
        result = json.dumps(myDict, indent=2, separators=(',', ':'), sort_keys=True)
        f.write(result)
        f.close()

toJson()