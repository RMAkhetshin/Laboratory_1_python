# Файл для хранения функций

from error import CalcError  # Импорт класса ошибок
from CONSTANTS import *      # Импорт возможных операций и констант

# Функция для токенизации
def tokenize(expression: str) -> tuple:
    for i in OPERATION_SYMBOLS:
        expression = expression.replace(i, f" {i} ")

    expression = expression.replace("/  /", "//")
    expression = expression.replace("*  *", "**")

    tokens = tuple(expression.split())
    return tokens

# Функция для проверки на число
def is_number(tokens, i) -> bool:
    try:
        _number = float(tokens[i])
        return True
    except ValueError:
        return False

# Функция для вычисления выражения внутри скобок
def calculate_brackets(tokens, i) -> tuple:
    count_brackets = 1                     # Счётчик скобок
    lenght = 0                             # Длина выражения внутри скобок
    while (count_brackets != 0 or
          (i + lenght == len(tokens))):    # Пока скобочное выражение не закончилось -- считаем открывающие и закрывающие скобки
        if tokens[i + lenght] == "(":      # когда получаем ноль -- выходим из цикла,
            count_brackets += 1            
        elif tokens[i + lenght] == ")":
            count_brackets -= 1
        lenght += 1                        # Продолжаем перебирать токены пока не выйдем
    if i + lenght == len(tokens):
        raise CalcError(f"Не закрыто скобок: {count_brackets}")
    return (calculator(" ".join(tokens[i:i + lenght - 1])), i + lenght - 1)
    # Функция calculator принимает на вход строку -- поэтому склеиваем список токенов и вычисляем значение

# Функция для обработки унарного плюса/минуса
def calculate_unary_number(tokens, i) -> tuple:
    # Проверка на следующий токен:
    # Если число -- домножить на унарный знак и добавить в стек
    if is_number(tokens, i + 1):
        if tokens[i] == "~":
            return [float(tokens[i + 1]) * (-1), i + 1]
        return [float(tokens[i + 1]), i + 1]
    # Если выражение в скобках -- обработать с помощью функции
    elif tokens[i + 1] == "(":
        brackets_result = calculate_brackets(tokens, i + 1)
        if tokens[i] == "~":
            result = brackets_result[0] * (-1)
        else:
            result = brackets_result[0]
        i = brackets_result[1]
        return (result, i)
    # Если ещё один унарный знак -- вернуть его результат
    elif tokens[i + 1] in BINARY_OPERATIONS:
        unary_result = calculate_unary_number(tokens, i + 1)
        if tokens[i] == "~": return [unary_result[0] * (-1), unary_result[1]]
        return unary_result
    else:
        raise CalcError("Нет числа после унарного минуса/плюса")

# Подсчёт выражения поданного на вход в RPN со скобками
def calculator(expression: str) -> float | int:
    expression = expression.strip()
    # Ошибка для проверки пустого ввода и скобок
    if not expression:
        raise CalcError("Пустое выражение")
    
    # Токенизация
    tokens = tokenize(expression)

    # Реализация через стек:
    stack = []
    i = 0  # <- переменная счётчик
    while i < len(tokens):  # Я не использую цикл for, чтобы быстрее
                            # проходиться по токенам и использовать только нужные мне.
                            # итерируемый токен -- tokens[i]

        # Добавление числа в стек
        if is_number(tokens, i):
            stack.append(float(tokens[i]))

        # Рекурсивный спуск для обработки выражения в скобках
        elif tokens[i] == "(":
            calc_result = calculate_brackets(tokens, i + 1)
            stack.append(calc_result[0])
            i = calc_result[1]
        elif tokens[i] == ")":
            raise CalcError("Не для каждой закрывающей функции есть открывающая")

        # Рекурсивный спуск для обработки унарного минуса/плюса
        elif tokens[i] in UNARY_OPERATIONS:
            result = calculate_unary_number(tokens, i)
            stack.append(result[0])
            i = result[1]

        # Обработка операторов
        # Ошибка при недостатке чисел в стеке
        elif tokens[i] in BINARY_OPERATIONS:
            if len(stack) < 2:
                raise CalcError(f"Недостаточно операндов для оператора {tokens[i]}")
            else:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                stack.append(float(BINARY_OPERATIONS[tokens[i]](operand_1, operand_2)))
            #     match tokens[i]:
            #         case "+": binary_result = operand_1 + operand_2
            #         case "+": binary_result = operand_1 + operand_2
            #         case "+": binary_result = operand_1 + operand_2
            #         case "+": binary_result = operand_1 + operand_2
            #         # Обработка ошибок при различном делении на ноль
            #         case "/":
            #             if operand_2 == 0: raise CalcError(f"Деление на ноль")
            #             binary_result = operand_1 / operand_2
            #         case "//":
            #             if operand_2 == 0: raise CalcError("Целочисленное деление на ноль")
            #             binary_result = operand_1 // operand_2
            #         case "%":
            #             if operand_2 == 0: raise CalcError("Остаток от деления на ноль")
            #             binary_result = operand_1 % operand_2

            # stack.append(float(binary_result))  # -- результат
        else:
            raise CalcError(f"Неизвестный токен или не окрыта скобка: '{tokens[i]}'")
        i += 1

    # Проверка на корректность вывода
    if len(stack) == 1:
        if stack[0] % 1 == 0:
            return int(stack[0])
        else:
            return stack[0]
    else:
        raise CalcError(f"Не хватает операторов: {stack} -- оставшиеся числа")