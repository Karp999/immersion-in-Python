# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
# Напишите к ним классы исключения с выводом подробной информации. 
# Поднимайте исключения внутри основного кода. 
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

from exceptions import min_triangle_sides, triangle_error

class Triangle:

    def __init__(self, a: int, b: int, c: int) -> None:
        if a > 0:
            self.a = a
        else:
            raise min_triangle_sides(a, 0)
        if b > 0:
            self.b = b
        else:
            raise min_triangle_sides(b, 0)
        if c > 0:
            self.c = c
        else:
            raise min_triangle_sides(c, 0)
        
    def checking_sides(self):

        check1 = self.a + self.b
        check2 = self.a + self.c
        check3 = self.b + self.c
        if (check1 < self.c or check2 < self.b or check3 < self.a):
            raise triangle_error(self.a, self.b, self.c)
        else:
            if (a == b and b == c and c == a):
                print()
                print("Результат: треугольник ABC является равносторонним.")
            elif (a == b or b == c or c == a):
                print()
                print("Результат: треугольник ABC является равнобедренным.")
            else:
                print()
                print("Результат: треугольник ABC является разносторонним.")


if __name__ == "__main__":
    print()
    user_request = f"Введите длину стороны треугольника "
    try:
        a = int(input(user_request + "AB треугольника ABC: "))
        print()
        b = int(input(user_request + "BC треугольника ABC: "))
        print()
        c = int(input(user_request + "AC треугольника ABC: "))
    except ValueError as v:
        print(f"Ошибка! Необходимо ввести число: {v}")

    abc = Triangle(a, b, c)
    abc.checking_sides()
print()