# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. 
# Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и 
# по оценкам всех предметов вместе взятых.

import csv
import json
from random import randint

myList = [{'Предмет' : 'Математика'},
          {'Предмет' : 'Русский язык'},
          {'Предмет' : 'Литература'},
          {'Предмет' : 'Английский'},
          {'Предмет' : 'Французский'}]

with open("subjects.csv", 'w', newline='', encoding='utf-8') as file:
    csv_write = csv.DictWriter(file, fieldnames=[*myList[0]])
    csv_write.writeheader()
    csv_write.writerows(myList)


class checking_Str:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
#        
        if not(value.isalpha() and value[0].isupper()):
            raise TypeError("Вводите только заглавные буквы!")
        else:
            setattr(instance, self.name, value)

class Student:
    name = checking_Str()
    surname = checking_Str()
    patronymic = checking_Str()

    def __init__(self, name:str, surname: str, patronymic :str, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self._myList = self.reading_subjects()
        self.performance = self.grades_and_average()
        self.json_saving()


    def reading_subjects(self):
        with open("subjects.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            myList = []
            for row in reader:
                myList.append(row["Предмет"])
        return myList

    def grades_and_average(self):
        gradeDict = {}
        for i in self._myList:
            x = randint(2, 5)
            y = randint(2, 5)
            z = randint(2, 5)
            iTest = randint(20, 100)
            gradeDict[i] = f"{x}, {y}, {z} \
                Средний балл - {round((x+y+z)/3, 2)},\
                Итоговое тестирование - {iTest}"
        return gradeDict

    def printSt(self):
        print()
        print(f'{self.surname} {self.name[0]}. {self.patronymic[0]} ')
        print(" "+';\n '.join([f'{key.capitalize()}: {value}' for key, value in self.performance.items()]))

    def json_saving(self):
        with open("students.json", 'a', encoding='utf-8') as json_f:
            json.dump(self.__dict__, json_f, indent=4, ensure_ascii=False)

stud1 = Student("Владислав", "Петров", "Александрович")
stud2 = Student("Анна", "Романова", "Валентиновна")
stud3 = Student("Феодора", "Журавлева", "Филипповна")
stud4 = Student("Лев", "Ильин", "Ильич")
stud5 = Student("Василиса", "Гавзова", "Александровна")

print()
stud1.printSt()
print()
stud2.printSt()
print()
stud3.printSt()
print()
stud4.printSt()
print()
stud5.printSt()
print()

# Файлы с предметами и студентами в папке dz12