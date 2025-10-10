from src.my_M3 import main_function


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    expression = input()

    print(main_function(expression))

if __name__ == "__main__":
    main()

# import re
# # expression = input()
# text = "  12 + 3.5 * -2  "

# TOKEN_RE = re.compile(r"\s*(\d+(?:\.\d+)?|\*\*|//|[%()+\-*/])")
# token = tuple[str, float | None]

# for index, op_match in enumerate(TOKEN_RE.finditer(text)):
#   print("# match is {0}, match is {1}".format(index, op_match))
#   for group in op_match.groups():
#     print("Finded group: ", group)


# def tokenize(expression: str) -> list:
#     if not expression or not expression.strip():
#         print("Пустой ввод")
    
#     pos = 0
#     out: list[token] = []

#     while pos < len(expression):
#         m = TOKEN_RE.match(expression, pos)
#         if not m:
#             print(f"Некорректный ввод около: '{expression[pos:]}'")

#         t = m.group(1)
#         pos = m.end()

#         if t[0].isdigit():
#             out.append(("NUM", float(t)))
#         else:
#             out.append((t, None))

#     out.append(("EOF", None))
#     return out

# def expr():
#     ...

# def add():
#     ...

# def mul():
#     ...

# def pow():
#     ...

# def unary():
#     ...

# def primary():
#     ...