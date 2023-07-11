# Задача №3:
# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def Fibonacci_nums(n: int) -> list[int]:
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

print()
print('Числа Фибоначчи: ')
print()
print(*(Fibonacci_nums(20)))
print()