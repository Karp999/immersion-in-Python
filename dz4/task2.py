# Задача №2: 
# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def f_dict(**arguments):
    new_dict = {}
    for keys, values in arguments.items():
        if isinstance(values, (list, dict, set, bytearray)):
            values = str(values)
        new_dict[values] = keys
    return new_dict


print(f_dict(genre = 'fairy tale', writers = {'Pushkin': 7, 'Andersen': 200}, publication_dates = ['1800-е',
      '1810-е', '1820-е', '1830-е']))