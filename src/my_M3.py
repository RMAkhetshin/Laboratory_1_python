# Калькулятор М3

class CalcError(Exception):
    # Класс для обработки ошибок калькулятора
    pass

# def remove_correct_brackets(tokens):
#     i = 0
#     sum_ops = 0
#     sum_elems = 0
#     while i != -1:
#         if tokens[i + 1] == ")":
#             ...
#         elif tokens[i + 1] == "(":
#             return remove_correct_brackets(tokens[i:])
#         else:
#             i += 1
#     ...

# def calculate_brackets(tokens):
    # "( 3 (4 5 -) *) 6 -"
    # for i, token in enumerate(tokens):
    #     count_brackets = 1
    #     lenght = 1
    #     while count_brackets != 0:
    #         if tokens[i + lenght] == "(":
    #             count_brackets += 1
    #         elif tokens[i + lenght] == ")":
    #             count_brackets -= 1
    #         lenght += 1
    #     print(" ".join(tokens[i:i + lenght + 1]))
    #     return calculator(" ".join(tokens[i:i + lenght + 1]))

def calculator(expression: str):
    # Подсчёт выражения поданного на вход в RPN со скобками
    expression = expression.strip()
    if not expression:
        raise CalcError("Пустое выражение")
    if expression.count("(") > expression.count(")"):
        raise CalcError(f"Не закрыто {expression.count("(") - expression.count(")")} скобок")
    elif expression.count("(") < expression.count(")"):
        raise CalcError(f"Не открыто {expression.count(")") - expression.count("(")} скобок")
    elif expression.index(")") < expression.index("("):
        raise CalcError("Не все скобки открыты или закрыты")
    
    for i in "+-~$%*/()":
        expression = expression.replace(i, f" {i} ")

    expression = expression.replace("/  /", "//")
    expression = expression.replace("*  *", "**")

    tokens = list(expression.split())

    while tokens[0] == "(" and tokens[-1] == ")":
        tokens = tokens[1:-1]

    print(tokens)

    stack = []
    i = 0
    # переменная счётчик
    while i < len(tokens):
    # я не использую цикл for, чтобы быстрее проходиться по токенам и использовать только нужные мне
    # итерируемый токен -- tokens[i]
        if tokens[i].replace(".", "").isdigit() and tokens[i].count(".") <= 1:
            stack.append(float(tokens[i]))
        # добавление числа в стек

        elif tokens[i] == "(":
            # stack.append(calculate_brackets(tokens[i:]))
            count_brackets = 1
            lenght = 1
            while count_brackets != 0:
                if tokens[i + lenght] == "(":
                    count_brackets += 1
                elif tokens[i + lenght] == ")":
                    count_brackets -= 1
                    # next_i = i + lenght
                lenght += 1
            print(" ".join(tokens[i:i + lenght]), i, lenght)
            stack.append(calculator(" ".join(tokens[i:i + lenght])))
            i += lenght - 1

        elif tokens[i] in ['+', '-', '*', '/', '//', '%', '**']:
            if len(stack) < 2:
                raise CalcError(f"Недостаточно операндов для оператора {tokens[i]}")
            
            else:
                element_2 = stack.pop()
                element_1 = stack.pop()

                if tokens[i] == '+':
                    result = element_1 + element_2
                elif tokens[i] == '-':
                    result = element_1 - element_2
                elif tokens[i] == '*':
                    result = element_1 * element_2
                elif tokens[i] == '/':
                    if element_2 == 0:
                        raise CalcError("Деление на ноль")
                    result = element_1 / element_2
                elif tokens[i] == '//':
                    if element_2 == 0:
                        raise CalcError("Целочисленное деление на ноль")
                    result = element_1 // element_2
                elif tokens[i] == '%':
                    if element_2 == 0:
                        raise CalcError("Остаток от деления на ноль")
                    result = element_1 % element_2
                elif tokens[i] == '**':
                    result = element_1 ** element_2
            stack.append(float(result))

        elif tokens[i] in "~$":
            "3 4 ~ ( 4 2 - ) - *"
            "3 4 - ~ 5 +"
            stack.append(calculator())
            

        else:
            raise CalcError(f"Неизвестный токен: '{tokens[i]}'")
        
        i += 1

    if len(stack) == 1:
        if stack[0] % 1 == 0:
            return int(stack[0])
        else:
            return stack[0]
    # elif len(stack) > 1:
    else:
        raise CalcError(f"Не хватает операторов: {stack} -- оставшиеся числа")