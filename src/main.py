# from src.power import power_function
# from src.constants import SAMPLE_CONSTANT


# def main() -> None:
#     """
#     Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
#     :return: Данная функция ничего не возвращает
#     """

#     target, degree = map(int, input("Введите два числа разделенные пробелом: ").split(" "))

#     result = power_function(target=target, power=degree)

#     print(result)

#     print(SAMPLE_CONSTANT)

# if __name__ == "__main__":
#     main()

import re
# expression = input()
text = "  12 + 3.5 * -2  "

TOKEN_RE = re.compile(r"""
\s*
(
  [+-]?\d+(?:\.\d+)?
  | [+\-*/]
)
""", re.VERBOSE)

for index, op_match in enumerate(TOKEN_RE.finditer(text)):
  print("# match is {0}, match is {1}".format(index, op_match))
  for group in op_match.groups():
    print("Finded group: ", group)

def expr():
    ...

def add():
    ...

def mul():
    ...

def pow():
    ...

def unary():
    ...

def primary():
    ...