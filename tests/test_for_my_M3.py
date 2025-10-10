# import unittest
# from src.my_M3 import main_function

# if __name__ == "__main__":
#     # Тестируем без input() для надежности
#     test_cases = [
#         "3 4 +",           # 7
#         "3 4 2 * +",       # 11
#         "5 1 2 + 4 * + 3 -" # 14
#     ]
    
#     for test in test_cases:
#         try:
#             result = main_function(test)
#             print(f"{test} = {result}")
#         except Exception as e:
#             print(f"{test} -> Ошибка: {e}")

# import sys
# import os

# # Добавляем папку src в путь поиска Python
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# from src.my_M3 import main_function

# import sys
# import os

# # Получаем абсолютный путь к корневой папке проекта
# project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# src_path = os.path.join(project_root, 'src')

# # Добавляем путь к src в sys.path
# if src_path not in sys.path:
#     sys.path.insert(0, src_path)


from src.my_M3 import main_function

# Ваши тесты
def test_basic_operations():
    """Тест базовых операций"""
    assert main_function("3 4 +") == 7
    assert src.my_M3.main_function("5 1 -") == 4
    assert src.my_M3.main_function("2 3 *") == 6
    assert src.my_M3.main_function("10 2 /") == 5
    # print("✓ Все базовые тесты пройдены")

def test_complex_expressions():
    """Тест сложных выражений"""
    assert src.my_M3.main_function("3 4 2 * +") == 11  # 3 + 4*2
    assert src.my_M3.main_function("5 1 2 + 4 * + 3 -") == 14  # 5 + (1+2)*4 - 3
    # print("✓ Сложные выражения работают")
