"""Задание 1"""
from functools import wraps
from time import time, sleep


def average_time(num=0):
    """Декоратор, который считает среднее время работы функции."""
    def inner_decorator(function):
        count = {}
        name = function.__name__
        count[name] = 0
        list_answer = []

        @wraps(function)
        def wrapper(*args, **kwargs):
            nonlocal list_answer
            count[name] += 1
            start = time()
            result = function(*args, **kwargs)
            end = time()-start
            list_answer.append(end)
            if count[name] < num:
                answer = sum(list_answer) / count[name]
                print(f'Среднее время работы: {int(answer * 1000)} мс.')
            else:
                answer = sum(list_answer[-num:]) / num
                print(f'Среднее время работы: {int(answer * 1000)} мс.')
            return result

        return wrapper

    return inner_decorator


@average_time(num=2)
def func_task(time_for_sleep):
    """Функция для теста."""
    sleep(time_for_sleep)
    return time_for_sleep


@average_time(num=3)
def func(time_for_sleep):
    """Функция для теста."""
    sleep(time_for_sleep)
    return time_for_sleep


if __name__ == '__main__':
    func_task(3)
    func_task(7)
    func_task(1)

    func(1)
    func(2)
    func(1)
