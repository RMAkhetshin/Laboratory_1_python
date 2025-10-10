from my_M3 import main_function


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    expression = input()

    print(main_function(expression))

if __name__ == "__main__":
    main()