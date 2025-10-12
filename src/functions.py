# Файл для хранения функций

from error import CalcError  # Импорт класса ошибок

# Функция для проверки на число
def is_number(tokens, i) -> bool:
    if (tokens[i].replace(".", "").isdigit() and
            tokens[i].count(".") <= 1): return True
    return False

# Функция для вычисления выражения внутри скобок
def calculate_brackets(tokens, i) -> list:
    count_brackets = 1  # Счётчик скобок
    lenght = 1  # Длина выражения внутри скобок -- нужна для рекурсивного спуска
    while count_brackets != 0:  # Пока скобочное выражение не закончилось --
        if tokens[i + lenght] == "(":  # -- получаем ноль и выходим из цикла,
            count_brackets += 1  # только если все скобки закрыты
        elif tokens[i + lenght] == ")":
            count_brackets -= 1
        lenght += 1  # Продолжаем перебирать токены пока не выйдем
    return [calculator(" ".join(tokens[i:i + lenght])), i + lenght - 1]
    # Функция calculator принимает на вход строку -- поэтому склеиваем список токенов и вычисляем значение

# Функция для обработки унарного плюса/минуса
def calculate_unary_number(tokens, i) -> list:
#     # Проверка на следующий токен:
#     # Если число -- домножить на унарный знак и добавить в стек
    if is_number(tokens, i + 1):
        if tokens[i] == "~":
            return [float(tokens[i + 1]) * (-1), i + 1]
        return [float(tokens[i + 1]), i + 1]
    # Если выражение в скобках -- обработать с помощью функции
    elif tokens[i + 1] == "(":
        calc_result = calculate_brackets(tokens, i + 1)
        if tokens[i] == "~":
            result = calc_result[0] * (-1)
        else:
            result = calc_result[0] * (-1)
        i = calc_result[1]
        return [result, i]
    # Если ещё один унарный знак -- вернуть его результат
    elif tokens[i + 1] in "~$":
        result = calculate_unary_number(tokens, i + 1)
        if tokens[i] == "~": return [result[0] * (-1), result[1]]
        return result
    else:
        raise CalcError("Нет числа после унарного минуса/плюса")

# Подсчёт выражения поданного на вход в RPN со скобками
def calculator(expression: str) -> float | int:
    expression = expression.strip()
    if not expression:
        raise CalcError("Пустое выражение")
    if expression.count("(") > expression.count(")"):
        raise CalcError(f"Не закрыто скобок: {expression.count("(") - expression.count(")")}")
    elif expression.count("(") < expression.count(")"):
        raise CalcError(f"Не открыто скобок: {expression.count(")") - expression.count("(")}")
    elif (expression.count("(") >= 1 and expression.count(")") >= 1
          and expression.index(")") < expression.index("(")):
        raise CalcError("Не все скобки открыты или закрыты")
    # Ошибки для проверки пустого ввода и скобок

    # Токенизация
    for i in "+-~$%*/()":
        expression = expression.replace(i, f" {i} ")

    expression = expression.replace("/  /", "//")
    expression = expression.replace("*  *", "**")

    tokens = list(expression.split())

    # Удаление незначащих скобок
    while tokens[0] == "(" and tokens[-1] == ")":
        tokens = tokens[1:-1]

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
            calc_result = calculate_brackets(tokens, i)
            stack.append(calc_result[0])
            i = calc_result[1]

        # Рекурсивный спуск для обработки унарного минуса/плюса
        elif tokens[i] in "~$":
            result = calculate_unary_number(tokens, i)
            stack.append(result[0])
            i = result[1]

        # Обработка операторов
        # Ошибка при недостатке чисел в стеке
        elif tokens[i] in ['+', '-', '*', '/', '//', '%', '**']:
            if len(stack) < 2:
                raise CalcError(f"Недостаточно операндов для оператора {tokens[i]}")

            else:
                elem_2 = stack.pop()
                elem_1 = stack.pop()

                if tokens[i] == '+':
                    result = elem_1 + elem_2
                elif tokens[i] == '-':
                    result = elem_1 - elem_2
                elif tokens[i] == '*':
                    result = elem_1 * elem_2
                elif tokens[i] == '**':
                    result = elem_1 ** elem_2
                # Обработка ошибок при различном делении на ноль
                elif tokens[i] == '/':
                    if elem_2 == 0: raise CalcError("Деление на ноль")
                    result = elem_1 / elem_2
                elif tokens[i] == '//':
                    if elem_2 == 0: raise CalcError("Целочисленное деление на ноль")
                    result = elem_1 // elem_2
                else:
                    # elif tokens[i] == '%': -- вариант того же условия, но на него пайчарм ругается
                    if elem_2 == 0: raise CalcError("Остаток от деления на ноль")
                    result = elem_1 % elem_2

            stack.append(float(result))  # -- результат
        else:
            raise CalcError(f"Неизвестный токен: '{tokens[i]}'")
        i += 1

    # Проверка на корректность вывода
    if len(stack) == 1:
        if stack[0] % 1 == 0:
            return int(stack[0])
        else:
            return stack[0]
    else:
        raise CalcError(f"Не хватает операторов: {stack} -- оставшиеся числа")