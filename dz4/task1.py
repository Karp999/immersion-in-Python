# Задача №1:
# Напишите функцию для транспонирования матрицы.

print()
print("Исходная матрица: ")
print()

array_A = [[1,1,1,1,1], [3,3,3,3,3], [7,7,7,7,7],[8,8,8,8,8], [9,9,9,9,9]]
for i in array_A:
    print(i)
print()

def transposition(array_A):
    for i in range(len(array_A)):
        for j in range(i, len(array_A[i])):
            temp = array_A[i][j]
            array_A[i][j] = array_A[j][i]
            array_A[j][i] = temp
    return array_A


print("Новая матрица: ")
print()
array_A = transposition(array_A)
for i in array_A:
    print(i)
print()