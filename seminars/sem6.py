# Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).
import sys as s

import random as rn

import math as mt

import time as tm

from sys import argv as ar

from random import randint as rd

from math import sqrt as sq

from time import time as t

# print(rd(0, 10))

# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”. Если число угадано, возвращается истина, а если попытки исчерпаны - ложь

# def function(a, b, c):
#    n = rd(a, b)
#    print(n)
#    while c > 0:
#       chislo = int(input('Введите число: '))
#       if chislo > n:
#          print('Число меньше')
#          c -= 1
#       elif chislo < n:
#          print('Число больше')
#          c -= 1
#       else:
#          print('Угадали число')
#          return True
#          break
#    print('Не угадали число')
#    return False


# function(0, 10, 3)

# Улучшаем задачу 2. Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

# if __name__ == '__main__':
#    flname, *param = ar
#    # function(*(int(n) for n in param))
#    print(function(*(int(n) for n in param)))
#    print(flname)

# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

def zagadka(zag, otg, popit):
   print(zag)
   count = 1
   while count <= popit:
      otvet = input('Ваш ответ: ').lower()
      if otvet in otg:
         print(f'Угадали c {count} попытки')
         return count
      else:
         print('Попробуйте еще раз')
         count += 1
   print('Не угадали')
   return 0


myDict = {'Идет шуршит':['шурашанчик'],
              'В кармане на П начинается': ['путылка'],
              'В кармене на Ы начинается': ['ышо одна путылка']}
for i in myDict:
   zagadka(i, myDict[i], 3)

zagadka('Висит груша, нельзя скушать?',['лампочка', 'лампа', 'лампомпулечка'], 3)


def archiv():
   myDict = {'Идет шуршит': ['шурашанчик'],
             'В кармане на П начинается': ['путылка'],
             'В кармене на Ы начинается': ['ышо одна путылка']}