# Задача №1:
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.
print('')
user_number = int(input("Введите целое число: "))
print('')

print("Вычисление при помощи функции hex(): ", hex(user_number))
str = ''
digits = '0123456789ABCDEF'
print('')

while user_number > 0:
    str = digits[user_number % 16] + str
    user_number = user_number // 16
 
print("Вычисление шестнадцатеричного числа при помощи цикла: ", str)
print('')

print('')