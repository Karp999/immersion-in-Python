import pathlib

nameOfFile = input('Желаемое имя файла ->> ')
count = input('кол-во цифр в порядковом номере ->> ')
extOld = input('расширение файла ->> ')
extNew = input('новое расширение ->> ')

def numNum(number:int, count:int):
    sNum = '' + str(number)
    for i in range(count):
        sNum = str(0)+sNum
    return sNum



def renameFiles(nameOfFile:str, count:int, extOld:str, extNew:str):
    p = pathlib.Path('dz7/')
    temp = []
    for i in p.iterdir():
        temp.append(i.name)
    print(temp)
    number = 0
    for i in range(len(temp)):
        name = temp[i].split('.')
        if name[1] == extOld:
            number +=1
            oldName = 'dz7/'+name[0]+'.'+extOld
            z = pathlib.Path(oldName)
            newName = 'dz/'+nameOfFile+ numNum(number, count) + '.' +extNew
            n = pathlib.Path(newName)
            z.rename(n)

path = 'C:/Users/79995/Desktop/GEEK BRAINS/6.seminars/2semester/python2/hm/dz7/'
# nameOfFile ='jojo'
# count = 3
# extOld = 'txt'
# extNew = 'cvc'
renameFiles(nameOfFile, count, extOld, extNew)

#Переименование файлов. Задаем желаемое имя, количество цифр для нумерации, старое и новое расширение