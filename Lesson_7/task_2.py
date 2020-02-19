"""Задание 2"""
from functools import wraps
from time import sleep, time


def timed(func):
    """Декоратор метода класса."""
    @wraps(func)
    def decorated_func(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time() - start
        print("{}: {}".format(func.__name__, end))
        return result
    return decorated_func


def time_methods(*args):
    """Декоратор класса."""
    def inner_decorator(specific_class):
        method_list = [func for func in dir(specific_class) if func in args]
        for i in method_list:
            decorated_a = timed((getattr(specific_class, i)))
            setattr(specific_class, i, decorated_a)
        return specific_class
    return inner_decorator


@time_methods('inspect', 'finalize')
class Spam:
    """Класс по заданию."""
    def __init__(self, value):
        self.value = value

    def inspect(self):
        """Sleep"""
        sleep(self.value)

    def func(self):
        """return value"""
        return self.value


if __name__ == '__main__':
    INSTANCE = Spam(2)
    INSTANCE.inspect()
    INSTANCE.func()
