"""Функция, которая принимает только 4 позиционных аргумента"""


def average():
    """Функция возвращает среднее арифметическое аргументов
    и самый большой аргумент за все время вызовов этой функции."""
    result_maximum = 0
    def inner_function(*args):
        length = len(args)
        maximum = max(args)
        nonlocal result_maximum
        if maximum > result_maximum:
            result_maximum = maximum
        return sum(args)/length, result_maximum
    return inner_function


X = average()
print(X(1, 5, 66))
print(X(1, 5, 4))
print(X(1, 200, 48))
