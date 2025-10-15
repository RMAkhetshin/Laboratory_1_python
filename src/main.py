from functions import calculator

# Точка входа в программу (приложение)
def main() -> None:
    expression = input("Выражение принимается в обратной польской записи (для выхода введи q)\n")
    while expression != "q":
        print(calculator(expression))
        expression = input("Выражение принимается в обратной польской записи (для выхода введи q)\n")

if __name__ == "__main__":
    main()