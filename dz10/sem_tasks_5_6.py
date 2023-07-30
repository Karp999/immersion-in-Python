# Задание 5:
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
# Задание 6:
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animals:
    def __init__(self, name, tail):
        self.name = name
        self.tail = tail


class Fish(Animals):
    def __init__(self, deep, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.deep = deep

    def specific(self):
        if self.deep < 5:
            return ' Речная/озерная'
        elif 5 < self.deep < 20:
            return 'Морская'
        return 'Океанская'


class Birds(Animals):
    def __init__(self, wingspan, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wingspan = wingspan

    def specific(self):
        wing_length = self.wingspan * 0.45
        return wing_length


class Mammals(Animals):
    def __init__(self, hibernate, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hibernate = hibernate

    def specific(self):
        if self.hibernate:
            return 'Впадает в спячку'
        return 'Не впадает в спячку'


if __name__ == '__main__':
    print()
    bear = Mammals(True, 'Медведь', True)
    print(f'Название: {bear.name}, хвост: {bear.tail}, спячка: {bear.specific()}')
    print()
    duck = Birds(73, 'Утка', True)
    print(f'Название: {duck.name}, хвост: {duck.tail}, длина крыла: {duck.specific()}')
    print()
    pike = Fish(4, 'Щука', True)
    print(f'Название: {pike.name}, хвост: {pike.tail}, глубина обитания: {pike.specific()}')
    print()
