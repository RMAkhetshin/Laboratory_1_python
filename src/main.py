from calculator import calculator

# Точка входа в программу (приложение)
def main() -> None:
    expression = input()
    print(calculator(expression))

if __name__ == "__main__":
    main()