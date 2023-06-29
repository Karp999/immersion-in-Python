# Задача №2: 
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

import fractions
# "числитель" - numerator буду сокращать как "num"
# "знаменатель" - denominator буду сокращать как "denom"

print('')
num_1 = int(input("Введите числитель первой дроби: ")) 
denom_1 = int(input("Введите знаменатель первой дроби: "))
print('')
num_2 = int(input("Введите числитель второй дроби: "))
denom_2 = int(input("Введите знаменатель второй дроби: "))
print('')

if denom_1 == denom_2:
    common_num = num_1 + num_2 # сумма числителей
    common_denom = denom_1 # сумма знаменателей, если они равны
else:
    common_num = (num_1 * denom_2) + (num_2 * denom_1) 
    # домножение на противоположные знаменатели, если они разные и сумма получившихся числителей
    common_denom = denom_1 * denom_2 # приводим к одному знаменателю, чтоб сложить дроби

print(f'Сумма дробей:  {common_num}/{common_denom}')
print(f'Произведение дробей:  {num_1 * num_2}/{denom_1 * denom_2}')
print('')

fraction_1 = fractions.Fraction(num_1, denom_1)
fraction_2 = fractions.Fraction(num_2, denom_2)
print('')

res_1 = fraction_1 + fraction_2
res_2 = fraction_1 * fraction_2

print(f'Проверка по модулю fractions: сумма = {res_1}, произведение = {res_2}')
print('')