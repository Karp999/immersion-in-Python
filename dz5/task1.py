# Задача №1: 
# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def file_extension(path: str) -> tuple:
    path, name = path.rsplit('\\', 1)
    name, extension = name.split('.')
    return path, name, extension

print()
separation_extension = r'C:\Users\79995\Desktop\GEEK BRAINS\6.seminars\2 semester 2023\python2\hm\dz5\cat.jpg'
print(file_extension(separation_extension))
print()