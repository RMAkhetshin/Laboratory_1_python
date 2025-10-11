from my_M3 import calculator


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    expression = input()

    print(calculator(expression))

if __name__ == "__main__":
    main()