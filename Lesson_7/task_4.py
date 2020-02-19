"""Задание 4"""
from functools import wraps
from inspect import getfullargspec


def type_of_args(func):
    """Декоратор, который проверяет тип аргументов."""

    @wraps(func)
    def wrapper(*args):
        dictionary = func.__annotations__
        params = getfullargspec(func)[0]
        params.append('return')
        dict_for_error = list(dictionary.keys())
        for param in params:
            if param not in dict_for_error:
                try:
                    raise TypeError
                except TypeError:
                    return "Error"
        count = -1
        del dictionary['return']
        for key, value in dictionary.items():
            count += 1
            if value is not type(args[count]):
                return 'Не верный тип аргумента - {}.'.format(key)
        return ''
    return wrapper


@type_of_args
def repeater(num: int, numb: int) -> int:
    """Тест функция."""
    return num * numb


A = repeater(5, 'f')
print(A)
