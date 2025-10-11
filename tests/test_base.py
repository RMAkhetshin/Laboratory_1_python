from src.calculator import calculator

# Тесты на операции
def test_operations():
    assert calculator("3 4 +") == 7
    assert calculator("5 10 -") == -5
    assert calculator("6 7 *") == 42
    assert calculator("10 4 /") == 2.5
    assert calculator("10 2 **") == 100
    assert calculator("34 16 %") == 2
    assert calculator ("23 // 5") == 4

# Некорректный ввод:
def test_uncorrect_input():
    assert calculator("         4  3 **      3 -     ") == 61
    assert calculator("(((((((3 5 7 - *)))))))") == -6
    assert calculator("     "), "Пустое выражение"
    assert calculator("6 7 ) 4 5 -( + *"), "CalcError: Не все скобки открыты или закрыты"
    assert calculator("23 5 (3 4 -) - * ( 2 4 -"), "Не закрыто скобок: 1"
    assert calculator(" 2 3 -) 4 *))") == "Не открыто скобок: 2"

# Тесты на унарные знаки и скобки:
def test_unar_and_brackets():
    assert calculator("10 ~5 -") == 15
    assert calculator("3 4 ~ ( 4 2 - ) - *") == 18
    assert calculator("3 4 - ~ 5 +") == -6
    assert calculator("( 3 (4 5 -) *) 6 - ") == -9