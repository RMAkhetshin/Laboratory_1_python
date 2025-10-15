from error import CalcError

# Функции для операций
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def pow(a, b):
    return a ** b
def div(a, b):
    if b == 0: raise CalcError("Деление на ноль")
    return a / b
def intdiv(a, b):
    if b == 0: raise CalcError("Целочисленное деление на ноль")
    return a // b
def ostdiv(a, b):
    if b == 0: raise CalcError("Остаток от деления на ноль")
    return a % b

OPERATION_SYMBOLS = ("(", ")", "+", "-", "$", "~", "%", "*", "/")
UNARY_OPERATIONS = ("~", "$")
BINARY_OPERATIONS = {'+': add, '-': sub, '*': mul,
                    '/': div, '//': intdiv, '%': ostdiv, '**': pow}