# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и
# параметры для этого типа. Внутри класса создайте экземпляр на основе переданного
# типа и верните его из класса-фабрики.

from sem_tasks_5_6 import Birds, Fish, Mammals, Animals
class Fabric:
    def __init__(self, obj_class, *args, **kwargs):
        self.obj_class = obj_class
        if self.obj_class == Birds:
            self.object = Birds(*args, **kwargs)
        elif self.obj_class == Fish:
            self.object = Fish(*args, **kwargs)
        elif self.obj_class == Mammals:
            self.object = Mammals(*args, **kwargs)
        else:
            self.object = Animals(*args, **kwargs)

    def get_object(self):
        return self.object

print()
bear = Fabric(Mammals, True, 'Медведь', True).get_object()
print(f'Название: {bear.name}, хвост: {bear.tail}, спячка: {bear.specific()}')
print()
duck = Fabric(Birds, 73, 'Утка', True).get_object()
print(f'Название: {duck.name}, хвост: {duck.tail}, длина крыла: {duck.specific()}')
print()
pike = Fabric(Fish, 4, 'Щука', True).get_object()
print(f'Название: {pike.name}, хвост: {pike.tail}, глубина обитания: {pike.specific()}')
print()