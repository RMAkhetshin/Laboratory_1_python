from error import CalcError               # Импорт класса ошибок
from functions import calculate_brackets  # Импорт функции для вычисления выражения в скобках

# Подсчёт выражения поданного на вход в RPN со скобками
def calculator(expression: str) -> float | int:
    expression = expression.strip()
    if not expression:
        raise CalcError("Пустое выражение")
    if expression.count("(") > expression.count(")"):
        raise CalcError(f"Не закрыто скобок: {expression.count("(") - expression.count(")")}")
    elif expression.count("(") < expression.count(")"):
        raise CalcError(f"Не открыто скобок: {expression.count(")") - expression.count("(")}")
    elif expression.index(")") < expression.index("("):
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
    i = 0                   # <- переменная счётчик
    while i < len(tokens):  # Я не использую цикл for, чтобы быстрее
                            # проходиться по токенам и использовать только нужные мне.
                            # итерируемый токен -- tokens[i]

        # Добавление числа в стек
        if tokens[i].replace(".", "").isdigit() and tokens[i].count(".") <= 1:
            stack.append(float(tokens[i]))
        
        # Реккурсивный спуск для обработки выражения в скобках
        elif tokens[i] == "(":
            result = calculate_brackets(tokens, i)
            stack.append(result[0])
            i = result[1]
        
        # Реккурсивный спуск для обработки унарного минуса/плюса
        elif tokens[i] in "~$":
            # Проверка на следующий токен:
            # Если число -- домножить на унарный знак и добавить в стек
            if tokens[i + 1].replace(".", "").isdigit() and tokens[i + 1].count(".") <= 1:
                if tokens[i] == "~": stack.append(float(tokens[i]) * (-1))
                else: stack.append(float(tokens[i]))
            # Если выражение в скобках -- обработать с помощью функции
            elif tokens[i + 1] == "(":
                result = calculate_brackets(tokens, i + 1)
                if tokens[i] == "~": stack.append(result[0] * (-1))
                else: stack.append(result[0])
                i = result[1]
            else:
                raise CalcError("Нет числа после унарного минуса/плюса")

        # Обработка операторов
        # Ошибка при недостатке чисел в стеке
        elif tokens[i] in ['+', '-', '*', '/', '//', '%', '**']:
            if len(stack) < 2:
                raise CalcError(f"Недостаточно операндов для оператора {tokens[i]}")
            
            else:
                elem_2 = stack.pop()
                elem_1 = stack.pop()

                if tokens[i] == '+': result = elem_1 + elem_2
                elif tokens[i] == '-': result = elem_1 - elem_2
                elif tokens[i] == '*': result = elem_1 * elem_2
                elif tokens[i] == '**': result = elem_1 ** elem_2
                # Обработка ошибок при различном делении на ноль
                elif tokens[i] == '/':
                    if elem_2 == 0: raise CalcError("Деление на ноль")
                    result = elem_1 / elem_2
                elif tokens[i] == '//':
                    if elem_2 == 0: raise CalcError("Целочисленное деление на ноль")
                    result = elem_1 // elem_2
                elif tokens[i] == '%':
                    if elem_2 == 0: raise CalcError("Остаток от деления на ноль")
                    result = elem_1 % elem_2
            
            stack.append(float(result)) # -- результат 
        else:
            raise CalcError(f"Неизвестный токен: '{tokens[i]}'")
        i += 1

    # Проверка на корректность вывода
    if len(stack) == 1:
        if stack[0] % 1 == 0: return int(stack[0])
        else: return stack[0]
    else:
        raise CalcError(f"Не хватает операторов: {stack} -- оставшиеся числа")