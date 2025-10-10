# Калькулятор М3

class CalcError(Exception):
    # Класс для обработки ошибок калькулятора
    pass

def main_function(expression: str) -> float:
    # Главная функция программы -- подсчёт выражения в RPN
    if not expression:
        raise CalcError("Пустое выражение")
    if expression.count("(") > expression.count(")"):
        raise CalcError(f"Не закрыто {expression.count("(") - expression.count(")")} скобок")
    elif expression.count("(") < expression.count(")"):
        raise CalcError(f"Не открыто {expression.count(")") - expression.count("(")} скобок")
    # if

    for i in "+-%*/()":
        expression = expression.replace(i, f" {i} ")

    expression = expression.replace("/  /", "//")
    expression = expression.replace("*  *", "**")
    expression = expression.replace("(", "")
    expression = expression.replace(")", "")

    tokens = list(expression.split())

    stack = []
    for token in tokens:
        if token.replace(".", "").isdigit() and token.count(".") <= 1:
            stack.append(float(token))

        elif token in ['+', '-', '*', '/', '//', '%', '**']:
            if len(stack) < 2:
                raise CalcError(f"Недостаточно операндов для оператора {token}")
            
            else:
                element_2 = stack.pop()
                element_1 = stack.pop()

                if token == '+':
                    result = element_1 + element_2
                elif token == '-':
                    result = element_1 - element_2
                elif token == '*':
                    result = element_1 * element_2
                elif token == '/':
                    if element_2 == 0:
                        raise CalcError("Деление на ноль")
                    result = element_1 / element_2
                elif token == '//':
                    if element_2 == 0:
                        raise CalcError("Целочисленное деление на ноль")
                    result = element_1 // element_2
                elif token == '%':
                    if element_2 == 0:
                        raise CalcError("Остаток от деления на ноль")
                    result = element_1 % element_2
                elif token == '**':
                    result = element_1 ** element_2
            stack.append(float(result))

        else:
            raise CalcError(f"Неизвестный токен: '{token}'")

    if len(stack) == 1:
        return stack[0]
    # elif len(stack) > 1:
    else:
        raise CalcError(f"Не хватает операторов: {stack} -- оставшиеся числа")