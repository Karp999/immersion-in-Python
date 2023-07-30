class exceptions(Exception):
    pass

class min_triangle_sides(exceptions):

    def __init__(self, param, value):
        self.param = param
        self.value = value
    
    def __str__(self):

        if self.param < self.value:
            print()
            return f'Сторона треугольника должна быть больше нуля!\n' \
            f'Заданное число {self.param} < {self.value}'
        elif self.param == self.value:
            print()
            return f'Сторона треугольника не может быть равна нулю!\n' \
            f'Заданное число {self.param} = {self.value}'

class triangle_error(exceptions):
    
    def __init__(self, value1: int, value2: int, value3: int):
        self.a = value1
        self.b = value2
        self.c = value3
    
    def __str__(self):
        print()
        print(f"Треугольник не существует!")

