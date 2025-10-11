# Функция для вычисления выражения внутри скобок
from calculator import calculator

def calculate_brackets(tokens, i) -> list:
    count_brackets = 1                     # Счётчик скобок
    lenght = 1                             # Длина выражения внутри скобок -- нужна для рекурсивного спуска
    while count_brackets != 0:             # Пока скобочное выражение не закончилось
        if tokens[i + lenght] == "(":      # Получаем ноль и выход из цикла,
            count_brackets += 1            # только если все скобки закрыты
        elif tokens[i + lenght] == ")":    
            count_brackets -= 1            
        lenght += 1                        # Продолжаем перебирать токены пока не выйдем
    return [calculator(" ".join(tokens[i:i + lenght])), i + lenght - 1]
    # Функция calculator принимает на вход строку -- поэтому склеиваем список токенов и вычисляем значение