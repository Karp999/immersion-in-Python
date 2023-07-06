# Задача 3:
# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# Сама задача: Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег



# константы-условия:
CASH_DIVISIBLE = 50
LOW_LIMIT_WITHDRAWAL = 30
UP_LIMIT_WITHDRAWAL = 600
PERCENT_FOR_CASH = 0.015
THIRD_PERCENT = 0.03
WEALTH_TAX = 0.1

operation = True
balance = 0

# Меню
def Menu() -> str:
    print()
    print('Для снятия наличных введите "1" : ')
    print('Для внесения наличных введите "2" : ')
    print('Для завершения работы с терминалом введите "3" : ')
    print()
    return input()
    

# Получение данных от пользователя: 
def Cash_input() -> int:
    cash = 0
    divisibility = True
    while divisibility:
        cash = int(input('Введите сумму: '))
        print()
        if cash % CASH_DIVISIBLE == 0:
            divisibility = False
        else:
            print(f'Сумма должна быть кратна: {CASH_DIVISIBLE} !')
    return cash

# Логика внесения наличных
def Depositing(current_balance: int) -> int:
    cash = Cash_input()
    print(current_balance, '+', cash)
    print()
    current_balance += cash
    control('Внесение наличных ->', str(cash))
    return current_balance

# Логика снятия наличных
def Withdrawal(balance: int) -> int:
    cash = Cash_input()
    percent = 0
    if LOW_LIMIT_WITHDRAWAL <= balance * PERCENT_FOR_CASH < UP_LIMIT_WITHDRAWAL:
        percent = balance * PERCENT_FOR_CASH
    elif balance * PERCENT_FOR_CASH < LOW_LIMIT_WITHDRAWAL:
        percent = LOW_LIMIT_WITHDRAWAL
    else:
        percent = UP_LIMIT_WITHDRAWAL
    if balance + percent >= cash:
        print(balance, '-', percent, '-', cash)
        balance -= percent + cash
        control('Снятие наличных', str(cash) + ' процент за операцию ' + str(percent))
    else:
        print('Сумма списания превышает баланс!!!')
    return balance

# Проверка на "богатство" для снятия налога на богатство
def is_reach(balance: int) -> int:
    if balance >= 5000000:
        print('Снятие налога на богатство.')
        print()
        print(balance, '-', balance * WEALTH_TAX)
        print()
        balance -= balance * WEALTH_TAX
        control('Снятие налога на богатство', str(balance * WEALTH_TAX))
        print('Текущий баланс равен : ', balance)
        print()
    return balance


# Сохранение операций в список
def control(operation: str, money: str):
    global list_control
    list_control.append([operation, money])


count = 0
list_control = []

# Основная логика меню и вызов соответствующих выбору пользователя функций 
while operation:
    count += 1
    balance = is_reach(balance)
    user_choice = Menu()
    if user_choice == '1':
        balance = Withdrawal(balance)
    elif user_choice == '2':
        balance = Depositing(balance)
    elif user_choice == '3':
        operation = False
    else:
        print('Некорректный ввод, попробуйте снова!!!')
    if count % 3 == 0:
        print('Начисление процента! ')
        print(balance, '+', balance * THIRD_PERCENT)
        balance += balance * THIRD_PERCENT
        control('Пополнение за третью операцию: ', str(balance * THIRD_PERCENT))
    print('Текущий баланс равен: ', balance)
print(list_control)