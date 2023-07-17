# Задача 1:
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import time

print()
class Date_checking:
    
    def date_validation(self, user_input):
        year_from_input = int(user_input[-4:])
        print()
        try:
            time.strptime(user_input, '%D.%M.%Y')
            self.year_validation(year_from_input)
            return True
        except ValueError:
            return False

    def year_validation(self, year):
        if (year % 4 == 0) \
                and (year % 100 != 0) \
                or (year % 400 == 0):
            print(f'{year} - год високосный')
            print()
        else:
            print(f'{year} - год не високосный')
            print()

if __name__ == '__main__':
    print(Date_checking().date_validation(input('Введите дату в формате DD.MM.YYYY: ')))
    print()